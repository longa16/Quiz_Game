import json
import random


def load_questions_from_file(filename):
    """ Loading the JSON file containing the questions """
    with open(filename, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    return questions


def filter_questions_by_difficulty(questions, difficulty):
    """ Filtering the questions by difficulty"""
    return [q for q in questions if q.get('difficulty') == difficulty]


def select_questions(questions, easy_count=5, medium_count=5, hard_count=5):
    """ Selecting the questions by difficulty """
    easy_questions = filter_questions_by_difficulty(questions, 'easy')
    medium_questions = filter_questions_by_difficulty(questions, 'medium')
    hard_questions = filter_questions_by_difficulty(questions, 'hard')

    selected_easy = random.sample(easy_questions, easy_count)
    selected_medium = random.sample(medium_questions, medium_count)
    selected_hard = random.sample(hard_questions, hard_count)

    # Combiner les questions
    selected_questions = selected_easy + selected_medium + selected_hard

    return selected_questions


questions = load_questions_from_file('database.json')
