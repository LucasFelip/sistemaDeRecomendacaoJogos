import pandas as pd

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

def get_game_recommendations(data, filtered_games, title=None, genre=None, top_n=50, price=None, release_date=None, platforms=None):
    games = filtered_games.copy()

    if title:
        games = games[games['name'].str.contains(title, case=False)]
    if genre:
        games = games[games['genres'].str.contains(genre, case=False)]
    if price is not None:
        games = games[games['price'] <= price]
    if release_date is not None:
        release_date = pd.to_datetime(release_date, format='%Y-%m-%d', errors='coerce')
        games = games[pd.to_datetime(games['release_date']).dt.date >= release_date.date()]
    if platforms:
        games = games[games['platforms'].str.contains(platforms, case=False)]

    games = games.sort_values('score', ascending=False)
    recommendations = games[['name', 'price', 'release_date', 'platforms', 'genres', 'positive_ratings', 'negative_ratings', 'score']].head(top_n)

    return recommendations

