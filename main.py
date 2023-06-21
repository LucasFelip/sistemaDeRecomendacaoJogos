from game_recommendation_system import GameRecommendationSystem

# Uso da classe GameRecommendationSystem
data_url = 'https://drive.google.com/uc?export=download&id=1SdCK7a5E9_vQKTEmMtEROrq-LBsKlTPE'

game_system = GameRecommendationSystem(data_url)

try:
    game_system.preprocess_data()
    recommendations = game_system.get_game_recommendations(genre='Action')
    print(recommendations)

    game_id = 10
    game_details = game_system.get_game_details(game_id)
    print(game_details)
except ValueError as e:
    print("Ocorreu um erro:", str(e))
except Exception as e:
    print("Ocorreu um erro não esperado:", str(e))
