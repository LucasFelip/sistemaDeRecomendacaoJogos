from data_loader import load_data
from data_preprocessing import preprocess_data
from display import display_recommendations
from game_recommendations import calculate_mean_rating, calculate_score, filter_games, get_game_recommendations
import tkinter as tk

# Carregar os dados
data = load_data()
data = preprocess_data(data)
m = data['positive_ratings'].quantile(0.70)
filtered_games = filter_games(data, m)
mean_rating = calculate_mean_rating(data)
filtered_games['score'] = filtered_games.apply(calculate_score, args=(mean_rating, m), axis=1)

def search_button_click():
    title = entry_title.get()
    genre = entry_genre.get()
    price = float(entry_price.get()) if entry_price.get() else None
    release_date = entry_release_date.get()
    platforms = entry_platforms.get()

    recommendations = get_game_recommendations(data, filtered_games, title=title, genre=genre, top_n=10, price=price,
                                               release_date=release_date, platforms=platforms)
    print(recommendations)
    display_recommendations(recommendations)


# Criar a interface gráfica
root = tk.Tk()
root.title("Recomendação de Jogos")

# Labels e entry boxes para os critérios de busca
label_title = tk.Label(root, text="Título do Jogo:")
entry_title = tk.Entry(root)
label_genre = tk.Label(root, text="Gênero do Jogo:")
entry_genre = tk.Entry(root)
label_price = tk.Label(root, text="Preço Máximo:")
entry_price = tk.Entry(root)
label_release_date = tk.Label(root, text="Data de Lançamento (YYYY-MM-DD):")
entry_release_date = tk.Entry(root)
label_platforms = tk.Label(root, text="Plataformas:")
entry_platforms = tk.Entry(root)

# Botão de busca
search_button = tk.Button(root, text="Buscar", command=search_button_click)

# Posicionar os elementos na interface
label_title.grid(row=0, column=0, sticky="e")
entry_title.grid(row=0, column=1)
label_genre.grid(row=1, column=0, sticky="e")
entry_genre.grid(row=1, column=1)
label_price.grid(row=2, column=0, sticky="e")
entry_price.grid(row=2, column=1)
label_release_date.grid(row=3, column=0, sticky="e")
entry_release_date.grid(row=3, column=1)
label_platforms.grid(row=4, column=0, sticky="e")
entry_platforms.grid(row=4, column=1)
search_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
