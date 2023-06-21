from game_recommendation_system import GameRecommendationSystem

# Uso da classe GameRecommendationSystem
data_url = 'https://drive.google.com/uc?export=download&id=1SdCK7a5E9_vQKTEmMtEROrq-LBsKlTPE'

game_system = GameRecommendationSystem(data_url)

try:
    game_system.preprocess_data()

    # Solicitar inputs do usuário
    genre = input("Digite o gênero desejado (ou deixe em branco para não filtrar por gênero): ")
    top_n = int(input("Digite o número de recomendações desejado (ou deixe em branco para o valor padrão): ") or game_system.TOP_N_RECOMMENDATIONS)

    # Obter recomendações com base nos inputs do usuário
    recommendations = game_system.get_game_recommendations(genre=genre, top_n=top_n)
    print(recommendations)

    print("=====================================================================================")
    game_id = int(input("Digite o ID (appid) do jogo para obter detalhes: "))

    # Obter detalhes do jogo com base no ID fornecido pelo usuário
    game_details = game_system.get_game_details(game_id)
    print(game_details)
except ValueError as e:
    print("Ocorreu um erro:", str(e))
except Exception as e:
    print("Ocorreu um erro não esperado:", str(e))

