"""Main page of quiz-game app"""
import sqlite3
import time

from source_code.player import Player
from source_code.questions import Questions


def menu():
    """Menu of the quiz-game app"""
    pseudo = input("Enter your pseudo : ")
    score = 0
    player = Player(pseudo, score)
    print("Hello", player.pseudo)
    print("\n Welcome to quiz-game app \n"
          "1 create a question\n"
          "2 history\n"
          "3 sport\n"
          "4 science\n"
          "5 exit\n")

    time.sleep(1)

    while True:
        choice = int(input("Choose a category: "))

        if choice == 1:
            category = input("What category would you like to: ")
            title = input("What is your title?: ")
            answer = input("What is your answer?: ")
            difficulty = input("What is the level of difficulty?: ")
            questions = Questions(category, title, answer, difficulty)

        elif choice == 2:
            print("History category")
        elif choice == 3:
            print("Sport category")
        elif choice == 4:
            print("Science category")
        elif choice == 5:
            print("Good Bye ;)")
            break
        else:
            print("Error, change it.")

        time.sleep(1)


connection = sqlite3.connect('quiz.db')
cursor = connection.cursor()

connection.close()

if __name__ == "__main__":
    menu()
