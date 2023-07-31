import tkinter as tk
from tkinter import ttk
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

        # Tabela para exibir as recomendações
        self.recommendations_table = ttk.Treeview(root, columns=("Nome", "Preço", "Data de Lançamento", "Plataformas", "Gêneros"))
        self.recommendations_table.heading("Nome", text="Nome")
        self.recommendations_table.heading("Preço", text="Preço")
        self.recommendations_table.heading("Data de Lançamento", text="Data de Lançamento")
        self.recommendations_table.heading("Plataformas", text="Plataformas")
        self.recommendations_table.heading("Gêneros", text="Gêneros")

        self.recommendations_table.column("#0", width=0)
        self.recommendations_table.column("Nome", anchor=tk.W, width=230)
        self.recommendations_table.column("Preço", anchor=tk.CENTER, width=100)
        self.recommendations_table.column("Data de Lançamento", anchor=tk.CENTER, width=120)
        self.recommendations_table.column("Plataformas", anchor=tk.W, width=150)
        self.recommendations_table.column("Gêneros", anchor=tk.W, width=350)

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

        self.recommendations_table.grid(row=7, column=0, columnspan=2, padx=5, pady=10)

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

            # Limpar a tabela antes de adicionar as novas recomendações
            self.recommendations_table.delete(*self.recommendations_table.get_children())

            # Adicionar as recomendações na tabela
            for index, row in recommendations.iterrows():
                self.recommendations_table.insert("", "end", text="", values=(
                    row['Nome'],
                    row['Preço'],
                    row['Data de Lançamento'],
                    row['Plataformas'],
                    row['Gêneros']
                ))

        except ValueError as e:
            messagebox.showerror("Erro", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = GameRecommendationApp(root)
    root.mainloop()
