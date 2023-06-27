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
    def load_data(self, data_url):
        try:
            data = pd.read_csv(data_url)
            return data
        except requests.exceptions.RequestException as e:
            raise ValueError("Erro ao carregar os dados: {}".format(e))

    def preprocess_data(self):
        self.data['Avaliações Positivas'] = pd.to_numeric(self.data['Avaliações Positivas'], errors='coerce')
        self.data['Avaliações Negativas'] = pd.to_numeric(self.data['Avaliações Negativas'], errors='coerce')
        self.data.dropna(subset=['Avaliações Positivas', 'Avaliações Negativas'], inplace=True)

    def calculate_mean_rating(self):
        mean_rating = self.data['Avaliações Positivas'].mean()
        return mean_rating

    def calculate_score(self, row, mean_rating):
        v = row['Avaliações Positivas']
        r = row['Avaliações Negativas']
        return (v / (v + self.m) * r) + (self.m / (self.m + v) * mean_rating)

    def calculate_threshold(self):
        return self.data['Avaliações Positivas'].quantile(self.QUANTILE)

    def filter_games(self):
        filtered_games = self.data[self.data['Avaliações Positivas'] >= self.m].copy()
        return filtered_games

    @lru_cache(maxsize=None)
    def get_game_recommendations(self, title=None, genre=None, top_n=None, price=None, release_date=None, platforms=None):
        if top_n is not None and (not isinstance(top_n, int) or top_n <= 0):
            raise ValueError("O número de recomendações deve ser um número inteiro positivo.")

        filtered_games = self.filter_games()

        if title:
            filtered_games = filtered_games[filtered_games['Nome'].str.contains(title, case=False)]
        if genre:
            filtered_games = filtered_games[filtered_games['Gêneros'].str.contains(genre, case=False)]
        if price is not None:
            filtered_games = filtered_games[filtered_games['Preço'] <= price]
        if release_date is not None:
            release_date = datetime.strptime(release_date, '%Y-%m-%d').date()
            filtered_games = filtered_games[pd.to_datetime(filtered_games['Data de Lançamento']).dt.date >= release_date]
        if platforms:
            filtered_games = filtered_games[filtered_games['Plataforma'].str.contains(platforms, case=False)]

        mean_rating = self.calculate_mean_rating()
        filtered_games['score'] = filtered_games.apply(self.calculate_score, args=(mean_rating,), axis=1)

        recommendations = filtered_games.sort_values('score', ascending=False)[['Nome']].head(top_n or self.TOP_N_RECOMMENDATIONS)
        return recommendations

    def get_game_details(self, game_id):
        game = self.data[self.data['appid'] == game_id]
        return game[['Nome', 'Preço', 'Data de Lançamento', 'Plataforma', 'Gêneros']]