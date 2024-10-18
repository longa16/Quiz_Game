from source_code.question import *

import tkinter as tk
from tkinter import messagebox
import random
from main import select_questions, load_questions_from_file


class QuizApp:
    """ Main application"""
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x400")

        self.questions = load_questions_from_file('source_code/database.json')
        self.selected_questions = select_questions(self.questions)

        self.current_question_index = 0

        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=500)
        self.question_label.pack(pady=20)

        self.options = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Arial", 12), width=20, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.options.append(btn)

        self.next_button = tk.Button(self.root, text="Suivant", font=("Arial", 12), command=self.next_question)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        """Load questions from the database """
        if self.current_question_index < len(self.selected_questions):
            question_data = self.selected_questions[self.current_question_index]
            self.question_label.config(text=question_data['question'])

            for i, option in enumerate(question_data['options']):
                self.options[i].config(text=option)

    def check_answer(self, selected_index):
        """Check if selected question is correct"""
        question_data = self.selected_questions[self.current_question_index]
        correct_answer = question_data['answer']

        # Si la réponse est correcte
        if correct_answer == chr(ord('A') + selected_index):
            messagebox.showinfo("Bonne réponse", "Bonne réponse !")
        else:
            messagebox.showinfo("Mauvaise réponse", f"Mauvaise réponse ! La bonne réponse était {correct_answer}.")

        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        """Go to the next question"""
        self.current_question_index += 1
        self.load_question()
        if self.current_question_index >= len(self.selected_questions):
            self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
