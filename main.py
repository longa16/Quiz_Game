"""Main page of quiz-game app"""

import time


def menu():
    """Menu of the quiz-game app"""
    print("\n Welcome to quiz-game app \n"
          "choose a category : \n "
          "1 science\n"
          "2 history\n"
          "3 sport\n"
          "4 exit\n")

    time.sleep(1)

    while True:
        choice = int(input("Choose a category: "))

        if choice == 1:
            print("Science category")
        elif choice == 2:
            print("History category")
        elif choice == 3:
            print("Sport category")
        elif choice == 4:
            print("Good Bye ;)")
            break
        else:
            print("Error, change it.")

        time.sleep(1)


if __name__ == "__main__":
    menu()
