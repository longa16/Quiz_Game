import tkinter as tk
from tkinter import messagebox
import time


# Fonction appelée lorsqu'une catégorie est sélectionnée
def category_choice(category):
    if category == "science":
        messagebox.showinfo("Catégorie", "Vous avez choisi la catégorie Science.")
    elif category == "history":
        messagebox.showinfo("Catégorie", "Vous avez choisi la catégorie Histoire.")
    elif category == "sport":
        messagebox.showinfo("Catégorie", "Vous avez choisi la catégorie Sport.")


# Fonction pour quitter l'application
def exit_app():
    response = messagebox.askyesno("Quitter", "Voulez-vous vraiment quitter ?")
    if response:
        root.quit()


# Création de la fenêtre principale
root = tk.Tk()
root.title("Quiz Game App")
root.geometry("300x250")

# Texte d'accueil
welcome_label = tk.Label(root, text="Bienvenue dans Quiz-Game App", font=("Arial", 14))
welcome_label.pack(pady=20)

# Choix de la catégorie
category_label = tk.Label(root, text="Choisissez une catégorie :", font=("Arial", 12))
category_label.pack(pady=10)

# Bouton pour la catégorie Science
science_button = tk.Button(root, text="Science", font=("Arial", 12), command=lambda: category_choice("science"))
science_button.pack(pady=5)

# Bouton pour la catégorie Histoire
history_button = tk.Button(root, text="Histoire", font=("Arial", 12), command=lambda: category_choice("history"))
history_button.pack(pady=5)

# Bouton pour la catégorie Sport
sport_button = tk.Button(root, text="Sport", font=("Arial", 12), command=lambda: category_choice("sport"))
sport_button.pack(pady=5)

# Bouton pour quitter l'application
exit_button = tk.Button(root, text="Quitter", font=("Arial", 12), command=exit_app)
exit_button.pack(pady=20)

# Lancement de la boucle principale de l'interface
root.mainloop()
