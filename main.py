from game_recommendation_system import GameRecommendationSystem
from user_input import get_user_inputs, clear_screen, get_user_inputs_id

# Uso da classe GameRecommendationSystem
data = 'Tratamento/steam.csv'

game_system = GameRecommendationSystem(data)
clear_screen()

try:
    game_system.preprocess_data()

    # Obter inputs do usuário
    title, genre, top_n, price, release_date, platforms = get_user_inputs()
    clear_screen()

    # Obter recomendações com base nos inputs do usuário
    recommendations = game_system.get_game_recommendations(title=title, genre=genre, top_n=top_n, price=price, release_date=release_date, platforms=platforms)
    print(recommendations)
except ValueError as e:
    print("Ocorreu um erro:", str(e))