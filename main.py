import json
import random
import tkinter as tk
from tkinter import messagebox, simpledialog
from source_code.scoring import Scoring
from source_code.bonus import Timer


def load_questions_from_file(filename):
    """ Loading the JSON file containing the questions """
    with open(filename, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    return questions


def filter_questions_by_difficulty(questions, difficulty):
    """ Filtering the questions by difficulty """
    return [q for q in questions if q.get('difficulty') == difficulty]


def select_questions(questions, difficulty, count=5):
    """ Selecting the questions by difficulty """
    filtered_questions = filter_questions_by_difficulty(questions, difficulty)
    selected_questions = random.sample(filtered_questions, count)
    return selected_questions


class QuizApp:
    """ Main application"""

    def __init__(self, root):
        self.root = root
        self.root.title("Culture Quiz")
        self.root.state('zoomed')

        # Couleur de fond principale
        self.root.configure(bg="#f0f0f0")

        self.questions = load_questions_from_file('source_code/database.json')
        self.selected_questions = []
        self.current_question_index = 0
        self.scoring = Scoring()
        self.answered = False
        self.leaderboard_page = 0
        self.score_saved = False
        self.difficulty = ""
        self.timer = None
        self.time_left = 15  # Temps en secondes
        self.streak = 0  # Ajout de la variable de streak

        # Créer un conteneur principal pour centrer les éléments avec place
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Charger l'image (logo)
        self.logo_image = tk.PhotoImage(file="source_code/logoquiz.png")  # Remplace par le chemin de ton image

        # Afficher l'image du logo avec un positionnement centré (relx 0.5 pour centrer horizontalement)
        self.logo_label = tk.Label(self.root, image=self.logo_image, bg="#f0f0f0")
        self.logo_label.place(relx=0.5, rely=0.3,
                              anchor=tk.CENTER)  # relx=0.5 permet de centrer horizontalement, rely=0.3 pour ajuster verticalement

        # Style du label de difficulté
        self.difficulty_label = tk.Label(self.main_frame, text="Choisissez la difficulté :", font=("Helvetica", 16),
                                         bg="#f0f0f0", fg="#333")
        self.difficulty_label.pack(pady=10)

        # Frame pour contenir les boutons de difficulté côte à côte
        self.difficulty_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.difficulty_frame.pack(pady=10)

        self.difficulty_buttons = []
        # Ajout des couleurs spécifiques pour chaque bouton
        button_colors = {
            'Easy': '#4CAF50',  # Vert
            'Medium': '#FF9800',  # Jaune/Orange
            'Hard': '#F44336'  # Rouge
        }

        for i, difficulty in enumerate(['Easy', 'Medium', 'Hard']):
            # Utilisation des couleurs spécifiques pour chaque difficulté
            btn = tk.Button(self.difficulty_frame, text=difficulty.capitalize(), font=("Helvetica", 14), width=15,
                            bg=button_colors[difficulty], fg="white", activebackground="#005f73",
                            activeforeground="white",
                            relief="raised", bd=4, command=lambda d=difficulty: self.start_quiz(d))
            btn.grid(row=0, column=i, padx=10)
            self.difficulty_buttons.append(btn)

    def start_quiz(self, difficulty):
        """Start the quiz with the selected difficulty"""
        self.difficulty = difficulty
        self.selected_questions = select_questions(self.questions, difficulty)
        self.current_question_index = 0
        self.scoring = Scoring()

        for btn in self.difficulty_buttons:
            btn.grid_forget()

        self.difficulty_label.pack_forget()

        # Style du label de question
        self.question_label = tk.Label(self.main_frame, text="", font=("Helvetica", 16), wraplength=600, bg="#f0f0f0",
                                       fg="#333")
        self.question_label.pack(
            pady=(100, 20))  # Ajout d'un padding top plus important pour éloigner les questions du logo

        # Style du label de score, du chronomètre et de la streak
        self.score_timer_streak_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.score_timer_streak_frame.pack(pady=10)

        self.score_label = tk.Label(self.score_timer_streak_frame, text=f"Score: {self.scoring.get_score()}",
                                    font=("Helvetica", 14), bg="#f0f0f0", fg="#333")
        self.score_label.pack(side=tk.LEFT, padx=10)

        self.timer_label = tk.Label(self.score_timer_streak_frame, text=f"Temps restant: {self.time_left}",
                                    font=("Helvetica", 14), bg="#f0f0f0", fg="#333")
        self.timer_label.pack(side=tk.LEFT, padx=10)

        self.streak_label = tk.Label(self.score_timer_streak_frame, text=f"Streak: {self.streak}",
                                     font=("Helvetica", 14), bg="#f0f0f0", fg="#333")
        self.streak_label.pack(side=tk.LEFT, padx=10)

        self.timer = Timer(self.root, self.time_left, self.timer_label)
        self.timer.next_question = self.next_question

        # Frame pour contenir les options côte à côte
        self.options_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.options_frame.pack(pady=10)

        self.options = []
        for i in range(4):
            # Style des boutons d'options, côte à côte
            btn = tk.Button(self.options_frame, text="", font=("Helvetica", 14), width=25, bg="#e7e7e7", fg="#333",
                            activebackground="#d4d4d4", activeforeground="#333", relief="solid", bd=2,
                            command=lambda i=i: self.check_answer(i))
            btn.grid(row=0, column=i, padx=5)
            self.options.append(btn)

        # Style du bouton "Suivant"
        self.next_button = tk.Button(self.main_frame, text="Suivant", font=("Helvetica", 14), fg="black",
                                     activebackground="#45a049", activeforeground="white", relief="solid", bd=2,
                                     command=self.next_question)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        """Load questions from the database """
        if self.current_question_index < len(self.selected_questions):
            question_data = self.selected_questions[self.current_question_index]
            self.question_label.config(text=question_data['question'])

            for i, option in enumerate(question_data['options']):
                self.options[i].config(text=option)

            self.scoring.start_question()
            self.timer.start_timer()

    def check_answer(self, selected_index):
        """Check if selected question is correct"""
        if self.answered:
            return

        question_data = self.selected_questions[self.current_question_index]
        correct_answer = question_data['answer']

        if self.scoring.check_answer(correct_answer, selected_index):
            self.options[selected_index].config(bg="#4CAF50", fg="white")
            self.streak += 1  # Incrémenter la streak si la réponse est correcte
        else:
            self.options[selected_index].config(bg="#F44336", fg="white")
            correct_index = ord(correct_answer) - ord('A')
            self.options[correct_index].config(bg="#4CAF50", fg="white")
            self.streak = 0  # Réinitialiser la streak si la réponse est incorrecte

        self.answered = True
        self.next_button.config(state=tk.NORMAL)
        self.score_label.config(text=f"Score: {self.scoring.get_score()}")
        self.streak_label.config(text=f"Streak: {self.streak}")  # Mettre à jour le label de la streak

    def next_question(self):
        """Go to the next question"""
        self.timer.cancel_timer()
        self.answered = False
        for btn in self.options:
            btn.config(bg="#e7e7e7", fg="#333")
        self.current_question_index += 1
        self.load_question()
        if self.current_question_index >= len(self.selected_questions):
            self.show_end_screen()

    def save_score(self, name, score, difficulty):
        """Save the score to a file"""
        try:
            with open("leaderboard.json", "r") as f:
                leaderboard = json.load(f)
        except FileNotFoundError:
            leaderboard = []

        leaderboard.append({"name": name, "score": score, "difficulty": difficulty})
        leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)

        with open("leaderboard.json", "w") as f:
            json.dump(leaderboard, f)

    def show_end_screen(self):
        """Show the end screen with leaderboard and buttons"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.end_screen_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.end_screen_frame.place(relx=0.5, rely=0.65, anchor=tk.CENTER)  # Ajustement de la valeur de rely

        self.end_screen_label = tk.Label(self.end_screen_frame, text="Classement :", font=("Helvetica", 16),
                                         bg="#f0f0f0", fg="#333")
        self.end_screen_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.leaderboard_frame = tk.Frame(self.end_screen_frame, bg="#f0f0f0")
        self.leaderboard_frame.grid(row=1, column=0, columnspan=3, pady=10)
        self.leaderboard_frame.grid_propagate(False)  # Empêche le cadre de s'adapter à la taille de son contenu
        self.leaderboard_frame.grid_rowconfigure(0, weight=1)  # Définit la hauteur du cadre

        self.leaderboard_label = tk.Label(self.leaderboard_frame, text="", font=("Helvetica", 14), bg="#f0f0f0",
                                          fg="#333")
        self.leaderboard_label.pack()

        self.prev_button = tk.Button(self.end_screen_frame, text="Précédent", font=("Helvetica", 14), bg="#e7e7e7",
                                     fg="#333", activebackground="#d4d4d4", activeforeground="#333", relief="solid",
                                     bd=2, command=self.prev_leaderboard_page)
        self.prev_button.grid(row=2, column=0, padx=10)

        self.next_button = tk.Button(self.end_screen_frame, text="Suivant", font=("Helvetica", 14), bg="#e7e7e7",
                                     fg="#333", activebackground="#d4d4d4", activeforeground="#333", relief="solid",
                                     bd=2, command=self.next_leaderboard_page)
        self.next_button.grid(row=2, column=2, padx=10)

        self.name_label = tk.Label(self.end_screen_frame, text="Entrez votre pseudo :", font=("Helvetica", 14),
                                   bg="#f0f0f0", fg="#333")
        self.name_label.grid(row=3, column=0, pady=20)

        self.name_entry = tk.Entry(self.end_screen_frame, font=("Helvetica", 14))
        self.name_entry.grid(row=3, column=1, pady=20)

        self.save_button = tk.Button(self.end_screen_frame, text="Enregistrer le score", font=("Helvetica", 14),
                                     bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white",
                                     relief="solid", bd=2, command=self.save_player_score)
        self.save_button.grid(row=3, column=2, padx=10, pady=20)

        self.quit_button = tk.Button(self.end_screen_frame, text="Quitter", font=("Helvetica", 14), bg="#F44336",
                                     fg="white", activebackground="#d32f2f", activeforeground="white", relief="solid",
                                     bd=2, command=self.root.quit)
        self.quit_button.grid(row=5, column=1, padx=10, pady=10)

        self.update_leaderboard()

    def update_leaderboard(self):
        """Update the leaderboard label"""
        try:
            with open("leaderboard.json", "r") as f:
                leaderboard = json.load(f)
        except FileNotFoundError:
            leaderboard = []

        leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)
        start_index = self.leaderboard_page * 10
        end_index = start_index + 10
        leaderboard_page = leaderboard[start_index:end_index]

        leaderboard_text = ""
        for i, entry in enumerate(leaderboard_page):
            leaderboard_text += f"{start_index + i + 1}. {entry['name']} - {entry['score']} - {entry['difficulty']}\n"

        self.leaderboard_label.config(text=leaderboard_text)

    def prev_leaderboard_page(self):
        """Go to the previous page of the leaderboard"""
        if self.leaderboard_page > 0:
            self.leaderboard_page -= 1
            self.update_leaderboard()

    def next_leaderboard_page(self):
        """Go to the next page of the leaderboard"""
        try:
            with open("leaderboard.json", "r") as f:
                leaderboard = json.load(f)
        except FileNotFoundError:
            leaderboard = []

        if self.leaderboard_page < len(leaderboard) // 10:
            self.leaderboard_page += 1
            self.update_leaderboard()

    def save_player_score(self):
        """Save the player's score and update the leaderboard"""
        if not self.score_saved:
            name = self.name_entry.get()
            if name:
                self.save_score(name, self.scoring.get_score(), self.difficulty)
                self.update_leaderboard()
                self.name_entry.delete(0, tk.END)
                self.score_saved = True
                self.save_button.config(state=tk.DISABLED)
            else:
                messagebox.showwarning("Pseudo manquant", "Veuillez entrer un pseudo.")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
