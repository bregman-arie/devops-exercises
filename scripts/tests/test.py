import unittest
import pathlib

from scripts.main import get_answered_questions, get_question_list


def open_test_case_file(n: int):
    p = pathlib.Path(rf'D:\PycharmProjects\devops-interview-questions\scripts\tests\testcase{n}.md')

    with open(p, 'rb') as f:
        file_list = [line.rstrip() for line in f.readlines()]
    return file_list


class QuestionCount(unittest.TestCase):
    solutions = (

    )

    def test_count_case_1(self):
        raw_list = open_test_case_file(1)
        question_list = get_question_list(raw_list)
        answers = get_answered_questions(question_list)

        self.assertEqual(len(question_list), 21)
        self.assertEqual(answers, 2)

    def test_count_case_2(self):
        pass