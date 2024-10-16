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
        print(self.category, self.title, self.answer, self.difficulty)
