import sqlite3


class Questions:
    """Represent a question.
    Attributes:
        category (str): The category of the question.
        title (str): The title of the question.
        answer (str): The answer of the question.
        difficulty (str): The difficulty of the question"""

    def __init__(self, category, title, answer, difficulty):
        """Initialize a question"""
        self.difficulty = difficulty
        self.category = category
        self.title = title
        self.answer = answer

    def print_questions(self):
        """Print the questions"""
        print(self.category, self.title, self.answer, self.difficulty)

    def create_question(self):
        """Create a new question"""
        conn = sqlite3.connect('quiz.db')
        cur = conn.cursor()
        cur.execute('''
                    INSERT INTO questions (title, answer, category, difficulty )  
                    VALUES (?, ?, ?, ? )
                ''', (self.title, self.answer, self.category, self.difficulty))
        conn.commit()
        conn.close()
