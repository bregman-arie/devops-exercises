import unittest
from pathlib import Path
from typing import List
from scripts.question_utils import get_answered_questions, get_question_list


def open_test_case_file(n: int) -> List[bytes]:
    tests_path = Path(__file__).parent.joinpath()

    with open(f'{tests_path}/testcases/testcase{n}.md', 'rb') as f:
        file_list = [line.rstrip() for line in f.readlines()]
    return file_list


class QuestionCount(unittest.TestCase):

    def test_case_1(self):
        raw_list = open_test_case_file(1)
        question_list = get_question_list(raw_list)
        answers = get_answered_questions(question_list)

        self.assertEqual(len(question_list), 11)
        self.assertEqual(len(answers), 3)

    def test_case_2(self):
        raw_list = open_test_case_file(2)
        question_list = get_question_list(raw_list)
        answers = get_answered_questions(question_list)

        self.assertEqual(len(question_list), 16)
        self.assertEqual(len(answers), 11)
