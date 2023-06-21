from datetime import datetime
import pandas as pd

def load_data():
    url = 'https://drive.google.com/uc?export=download&id=1SdCK7a5E9_vQKTEmMtEROrq-LBsKlTPE'
    data = pd.read_csv(url, dtype={'id': str}, low_memory=False)
    return data

def preprocess_data(data):
    data['positive_ratings'] = pd.to_numeric(data['positive_ratings'], errors='coerce')
    data['negative_ratings'] = pd.to_numeric(data['negative_ratings'], errors='coerce')
    data.dropna(subset=['positive_ratings', 'negative_ratings'], inplace=True)
    return data

def calculate_mean_rating(data):
    mean_rating = data['positive_ratings'].mean()
    return mean_rating

def calculate_score(row, mean_rating, m):
    v = row['positive_ratings']
    r = row['negative_ratings']
    return (v / (v + m) * r) + (m / (m + v) * mean_rating)

def filter_games(data, m):
    filtered_games = data[data['positive_ratings'] >= m].copy()
    return filtered_games

def get_game_recommendations(data, filtered_games, title=None, genre=None, top_n=60, price=None, release_date=None, platforms=None):
    games = filtered_games.copy()

    if title:
        games = games[games['name'].str.contains(title, case=False)]
    if genre:
        games = games[games['genres'].str.contains(genre, case=False)]
    if price is not None:
        games = games[games['price'] <= price]
    if release_date is not None:
        release_date = datetime.strptime(release_date, '%Y-%m-%d').date()
        games = games[pd.to_datetime(games['release_date']).dt.date >= release_date]
    if platforms:
        games = games[games['platforms'].str.contains(platforms, case=False)]

    games = games.sort_values('score', ascending=False)
    recommendations = games[['name', 'price']].head(top_n)
    return recommendations

#================================================================================

data = load_data()
data = preprocess_data(data)
m = data['positive_ratings'].quantile(0.70)
filtered_games = filter_games(data, m)
mean_rating = calculate_mean_rating(data)
filtered_games['score'] = filtered_games.apply(calculate_score, args=(mean_rating, m), axis=1)

recommendations = get_game_recommendations(data, filtered_games, genre='Action')
print(recommendations)