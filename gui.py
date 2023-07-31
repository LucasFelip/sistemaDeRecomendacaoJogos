import tkinter as tk
from tkinter import messagebox
from user_input import get_user_inputs, get_user_inputs_id
from game_recommendation_system import GameRecommendationSystem

class GameRecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Recomendação de Jogos")
        self.game_system = None

        # Criar os elementos da interface
        self.title_label = tk.Label(root, text="Título:")
        self.title_entry = tk.Entry(root)

        self.genre_label = tk.Label(root, text="Gênero:")
        self.genre_entry = tk.Entry(root)

        self.top_n_label = tk.Label(root, text="Número de recomendações:")
        self.top_n_entry = tk.Entry(root)

        self.price_label = tk.Label(root, text="Preço máximo:")
        self.price_entry = tk.Entry(root)

        self.release_date_label = tk.Label(root, text="Data de lançamento (AAAA-MM-DD):")
        self.release_date_entry = tk.Entry(root)

        self.platforms_label = tk.Label(root, text="Plataformas:")
        self.platforms_entry = tk.Entry(root)

        self.recommend_button = tk.Button(root, text="Recomendar", command=self.get_recommendations)

        # Posicionar os elementos na interface
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        self.genre_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.genre_entry.grid(row=1, column=1, padx=5, pady=5)

        self.top_n_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.top_n_entry.grid(row=2, column=1, padx=5, pady=5)

        self.price_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.price_entry.grid(row=3, column=1, padx=5, pady=5)

        self.release_date_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.release_date_entry.grid(row=4, column=1, padx=5, pady=5)

        self.platforms_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        self.platforms_entry.grid(row=5, column=1, padx=5, pady=5)

        self.recommend_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

    def get_recommendations(self):
        try:
            # Obter os inputs do usuário
            title = self.title_entry.get()
            genre = self.genre_entry.get()
            top_n = int(self.top_n_entry.get()) if self.top_n_entry.get() else None
            price = float(self.price_entry.get()) if self.price_entry.get() else None
            release_date = self.release_date_entry.get() if self.price_entry.get() else None
            platforms = self.platforms_entry.get()

            # Carregar e preparar o sistema de recomendação
            data_path = 'Tratamento/steam.csv'
            self.game_system = GameRecommendationSystem(data_path)
            self.game_system.preprocess_data()

            # Obter as recomendações com base nos inputs do usuário
            recommendations = self.game_system.get_game_recommendations(
                title=title,
                genre=genre,
                top_n=top_n,
                price=price,
                release_date=release_date,
                platforms=platforms
            )

            # Mostrar as recomendações em uma caixa de mensagem
            if recommendations.empty:
                messagebox.showinfo("Recomendações", "Nenhum jogo encontrado com os critérios informados.")
            else:
                recommendations_text = "Recomendações:\n" + recommendations.to_string(index=False)
                messagebox.showinfo("Recomendações", recommendations_text)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = GameRecommendationApp(root)
    root.mainloop()
