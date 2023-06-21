from datetime import datetime
import pandas as pd
import io
from functools import lru_cache

import requests


class GameRecommendationSystem:
    QUANTILE = 0.70
    TOP_N_RECOMMENDATIONS = 5

    def __init__(self, data_url):
        self.data = self.load_data(data_url)
        self.m = self.calculate_threshold()

    @lru_cache(maxsize=None)
    def load_data(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = pd.read_csv(io.BytesIO(response.content), dtype={'appid': int}, low_memory=False)
            return data
        except requests.exceptions.RequestException as e:
            raise ValueError("Erro ao carregar os dados: {}".format(e))

    def preprocess_data(self):
        self.data['positive_ratings'] = pd.to_numeric(self.data['positive_ratings'], errors='coerce')
        self.data['negative_ratings'] = pd.to_numeric(self.data['negative_ratings'], errors='coerce')
        self.data.dropna(subset=['positive_ratings', 'negative_ratings'], inplace=True)

    def calculate_mean_rating(self):
        mean_rating = self.data['positive_ratings'].mean()
        return mean_rating

    def calculate_score(self, row, mean_rating):
        v = row['positive_ratings']
        r = row['negative_ratings']
        return (v / (v + self.m) * r) + (self.m / (self.m + v) * mean_rating)

    def calculate_threshold(self):
        return self.data['positive_ratings'].quantile(self.QUANTILE)

    def filter_games(self):
        filtered_games = self.data[self.data['positive_ratings'] >= self.m].copy()
        return filtered_games

    @lru_cache(maxsize=None)
    def get_game_recommendations(self, title=None, genre=None, top_n=None, price=None, release_date=None, platforms=None):
        if top_n is not None and (not isinstance(top_n, int) or top_n <= 0):
            raise ValueError("O valor de 'top_n' deve ser um número inteiro positivo.")

        filtered_games = self.filter_games()

        if title:
            filtered_games = filtered_games[filtered_games['name'].str.contains(title, case=False)]
        if genre:
            filtered_games = filtered_games[filtered_games['genres'].str.contains(genre, case=False)]
        if price is not None:
            filtered_games = filtered_games[filtered_games['price'] <= price]
        if release_date is not None:
            release_date = datetime.strptime(release_date, '%Y-%m-%d').date()
            filtered_games = filtered_games[pd.to_datetime(filtered_games['release_date']).dt.date >= release_date]
        if platforms:
            filtered_games = filtered_games[filtered_games['platforms'].str.contains(platforms, case=False)]

        mean_rating = self.calculate_mean_rating()
        filtered_games['score'] = filtered_games.apply(self.calculate_score, args=(mean_rating,), axis=1)

        recommendations = filtered_games.sort_values('score', ascending=False)[['appid','name']].head(top_n or self.TOP_N_RECOMMENDATIONS)
        return recommendations

    def get_game_details(self, game_id):
        game = self.data[self.data['appid'] == game_id]
        return game
