"""
Usage:

$ python scripts/get_answered_questions.py

Writes the number of answered questions to STDOUT

"""


import pathlib
from sys import stdout
from typing import List

p = pathlib.Path(__file__).parent.parent.joinpath('README.md')

with open(p, 'rb') as f:
    file_list = [line.rstrip() for line in f.readlines()]


def get_question_list(file_list: List[bytes]) -> list:

    questions_list = []
    temp = []
    after_summary_tag = False

    for line in file_list:
        if line.startswith(b'<details>'):
            temp.append(line)
            after_summary_tag = True

        elif after_summary_tag and line != b'' and b'</details>' not in line:
            temp.append(line)

        elif after_summary_tag and b'</details>' in line:
            temp.append(line)
            after_summary_tag = False

            questions_list.append(temp)
            temp = []

    return questions_list


def get_answered_questions(question_list: List[List[bytes]]) -> int:
    c = 0
    for q in question_list:
        index = 0
        for i in q:
            if b'</summary>' in i:
                index = q.index(i)
        if q[index+1: len(q) - 1]:
            c += 1
    return c


if __name__ == '__main__':
    question_list = get_question_list(file_list)
    n_answers = get_answered_questions(question_list)
    stdout.write(str(n_answers))
