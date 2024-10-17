import tkinter as tk
from tkinter import messagebox
from source_code.player import Player
from source_code.questions import Questions


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        # Variables d'état
        self.pseudo = tk.StringVar()
        self.difficulty = tk.StringVar()
        self.category = tk.StringVar()
        self.title = tk.StringVar()
        self.answer = tk.StringVar()
        self.player = None

        # Interface de démarrage
        self.create_start_interface()

    def create_start_interface(self):
        """Crée l'interface de démarrage."""
        self.clear_interface()

        # Entrée pour le pseudo
        tk.Label(self.root, text="Enter your pseudo:").pack()
        tk.Entry(self.root, textvariable=self.pseudo).pack()

        # Bouton pour démarrer le jeu
        tk.Button(self.root, text="Start Game", command=self.start_game).pack(pady=10)

    def start_game(self):
        """Démarre le jeu après que l'utilisateur ait entré son pseudo."""
        pseudo = self.pseudo.get()
        if pseudo:
            self.player = Player(pseudo, 0)
            Player.insert_player_database(self.player)
            self.choose_difficulty_interface()
        else:
            messagebox.showerror("Error", "Please enter a pseudo.")

    def choose_difficulty_interface(self):
        """Crée l'interface pour choisir la difficulté."""
        self.clear_interface()

        tk.Label(self.root, text=f"Hello {self.player.pseudo}, choose difficulty:").pack()

        # Sélection de la difficulté
        difficulties = [("Easy", "easy"), ("Medium", "medium"), ("Hard", "hard")]
        for text, value in difficulties:
            tk.Radiobutton(self.root, text=text, variable=self.difficulty, value=value).pack()

        tk.Button(self.root, text="Next", command=self.show_categories_interface).pack(pady=10)

    def show_categories_interface(self):
        """Affiche le menu de sélection de catégories."""
        self.clear_interface()

        tk.Label(self.root, text="Choose a category:").pack()

        # Boutons pour les différentes catégories
        tk.Button(self.root, text="Create a question", command=self.create_question_interface).pack()
        tk.Button(self.root, text="History", command=lambda: self.show_category("History")).pack()
        tk.Button(self.root, text="Sport", command=lambda: self.show_category("Sport")).pack()
        tk.Button(self.root, text="Science", command=lambda: self.show_category("Science")).pack()

        # Option pour quitter
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

    def show_category(self, category):
        """Affiche un message avec la catégorie choisie."""
        messagebox.showinfo("Category", f"You selected {category} category.")

    def create_question_interface(self):
        """Crée une interface pour ajouter une nouvelle question."""
        self.clear_interface()

        tk.Label(self.root, text="Create a new question").pack(pady=10)

        tk.Label(self.root, text="Category:").pack()
        tk.Entry(self.root, textvariable=self.category).pack()

        tk.Label(self.root, text="Title:").pack()
        tk.Entry(self.root, textvariable=self.title).pack()

        tk.Label(self.root, text="Answer:").pack()
        tk.Entry(self.root, textvariable=self.answer).pack()

        tk.Label(self.root, text="Difficulty:").pack()
        tk.Entry(self.root, textvariable=self.difficulty).pack()

        tk.Button(self.root, text="Create", command=self.create_question).pack(pady=10)

    def create_question(self):
        """Enregistre la question créée par l'utilisateur."""
        category = self.category.get()
        title = self.title.get()
        answer = self.answer.get()
        difficulty = self.difficulty.get()

        if category and title and answer and difficulty:
            question = Questions(category, title, answer, difficulty)
            Questions.create_question(question)
            messagebox.showinfo("Success", "Question created successfully!")
            self.show_categories_interface()
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    def clear_interface(self):
        """Efface tous les widgets de l'interface."""
        for widget in self.root.winfo_children():
            widget.destroy()


def run_app():
    """Lance l'application Tkinter."""
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_app()
