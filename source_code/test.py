import unittest
from unittest.mock import patch

from question import filter_questions_by_difficulty, select_questions


class TestQuestionFunctions(unittest.TestCase):

    def setUp(self):
        self.sample_questions = [
            {"question": "Easy question 1", "difficulty": "easy"},
            {"question": "Easy question 2", "difficulty": "easy"},
            {"question": "Medium question 1", "difficulty": "medium"},
            {"question": "Medium question 2", "difficulty": "medium"},
            {"question": "Hard question 1", "difficulty": "hard"},
            {"question": "Hard question 2", "difficulty": "hard"}
        ]

    def test_filter_questions_by_difficulty(self):
        easy_questions = filter_questions_by_difficulty(self.sample_questions, 'easy')
        self.assertEqual(len(easy_questions), 2)
        self.assertTrue(all(q['difficulty'] == 'easy' for q in easy_questions))

        medium_questions = filter_questions_by_difficulty(self.sample_questions, 'medium')
        self.assertEqual(len(medium_questions), 2)
        self.assertTrue(all(q['difficulty'] == 'medium' for q in medium_questions))

        hard_questions = filter_questions_by_difficulty(self.sample_questions, 'hard')
        self.assertEqual(len(hard_questions), 2)
        self.assertTrue(all(q['difficulty'] == 'hard' for q in hard_questions))

    @patch('random.sample')
    def test_select_questions(self, mock_sample):
        mock_sample.side_effect = lambda x, y: x[:y]

        selected_questions = select_questions(self.sample_questions, easy_count=1, medium_count=1, hard_count=1)
        self.assertEqual(len(selected_questions), 3)
        self.assertEqual(selected_questions[0]['difficulty'], 'easy')
        self.assertEqual(selected_questions[1]['difficulty'], 'medium')
        self.assertEqual(selected_questions[2]['difficulty'], 'hard')


if __name__ == '__main__':
    unittest.main()
