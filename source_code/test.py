import pytest
from source_code.player import Player
from source_code.questions import Questions


@pytest.fixture
def player():
    """Create a fixture for all the test for the player class"""
    return Player("Sputnik", 200)


@pytest.fixture
def question():
    """Create a fixture for all the test for the question class"""
    return Questions("Science", "what is the capital of France",
                     "Paris", "easy")


def test_question_information(question):
    """information question Test"""
    assert question.category == "Science"
    assert question.title == "what is the capital of France"
    assert question.difficulty == "easy"
    assert question.answer == "Paris"


def test_player_information(player):
    """player information Test"""
    assert player.pseudo == "Sputnik"
    assert player.score == 200
