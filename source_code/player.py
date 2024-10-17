import sqlite3



class Player:
    """Represents a player
    Attributes:
        pseudo (str): The pseudo of the player
        score (str): The score of the player"""

    def __init__(self, pseudo, score):
        self.pseudo = pseudo
        self.score = score

    def print_player_info(self):
        print(self.pseudo, self.score)

    def insert_player_database(self):
        conn = sqlite3.connect('quiz.db')
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO qu_user (pseudo, score) 
            VALUES (?, ?)
        ''', (self.pseudo, self.score))
        conn.commit()
        conn.close()



