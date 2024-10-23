import time

class Scoring:
    def __init__(self):
        self.score = 0
        self.consecutive_correct_answers = 0
        self.question_start_time = time.time()

    def check_answer(self, correct_answer, selected_index):
        if correct_answer == chr(ord('A') + selected_index):
            self.score += 10
            self.consecutive_correct_answers += 1

            # Bonus pour les réponses rapides
            time_taken = time.time() - self.question_start_time
            if time_taken < 2:
                self.score += 10
            elif time_taken < 5:
                self.score += 8
            elif time_taken < 10:
                self.score += 5

            # Bonus pour les séries de bonnes réponses
            if self.consecutive_correct_answers >= 3:
                self.score += self.consecutive_correct_answers - 2

            return True
        else:
            self.consecutive_correct_answers = 0
            return False

    def get_score(self):
        return self.score

    def start_question(self):
        self.question_start_time = time.time()
