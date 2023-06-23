# Arquivo: main.py
from tkinter import Tk, Label, Button, Text, Scrollbar
from game_recommendation_system import GameRecommendationSystem
from user_input import get_user_inputs, clear_screen, get_user_inputs_id

# Uso da classe GameRecommendationSystem
data_url = 'https://drive.google.com/uc?export=download&id=1SdCK7a5E9_vQKTEmMtEROrq-LBsKlTPE'

game_system = GameRecommendationSystem(data_url)
clear_screen()

try:
    game_system.preprocess_data()

    # Obter inputs do usuário
    title, genre, top_n, price, release_date, platforms = get_user_inputs()
    clear_screen()

    # Obter recomendações com base nos inputs do usuário
    recommendations = game_system.get_game_recommendations(title=title, genre=genre, top_n=top_n, price=price, release_date=release_date, platforms=platforms)

    # Criar janela com os resultados
    window = Tk()
    window.title("Game Recommendation System")
    window.geometry("600x400")

    title_label = Label(window, text="Recomendações de Jogos", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    recommendations_text = Text(window, height=20, width=70)
    scrollbar = Scrollbar(window, command=recommendations_text.yview)
    recommendations_text.configure(yscrollcommand=scrollbar.set)

    recommendations_text.insert("end", str(recommendations))
    recommendations_text.configure(state="disabled")
    recommendations_text.pack(padx=20, pady=10)
    scrollbar.pack(side="right", fill="y")

    game_id = get_user_inputs_id()

    # Obter detalhes do jogo com base no ID fornecido pelo usuário
    game_details = game_system.get_game_details(game_id)

    details_label = Label(window, text="Detalhes do Jogo", font=("Arial", 16, "bold"))
    details_label.pack(pady=10)

    details_text = Text(window, height=10, width=70)
    details_text.insert("end", str(game_details))
    details_text.configure(state="disabled")
    details_text.pack(padx=20, pady=10)

    window.mainloop()

except ValueError as e:
    print("Ocorreu um erro:", str(e))
