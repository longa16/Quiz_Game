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
