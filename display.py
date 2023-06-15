import tkinter as tk
from tkinter import ttk


def display_recommendations(recommendations):
    root = tk.Tk()
    root.title("Recomendações de Jogos")

    table = ttk.Treeview(root)
    table["columns"] = list(recommendations.columns)
    table["show"] = "headings"

    for column in recommendations.columns:
        table.heading(column, text=column)

    for row in recommendations.itertuples(index=False):
        table.insert("", "end", values=list(row))

    table.pack(expand=True, fill="both")

    root.mainloop()




