"""
Question utils functions
"""

import pathlib
from random import choice
from typing import List

p = pathlib.Path(__file__).parent.parent.joinpath('README.md')


def get_file_list():
    with open(p, 'rb') as f:
        file_list = [line.rstrip() for line in f.readlines()]
    return file_list


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


def get_answered_questions(question_list: List[List[bytes]]) -> list:
    """Dont let the type hint confuse you, problem of not using classes.

     It takes the result of get_question_list(file_list)

     Returns a list of questions that are answered.
     """

    t = []

    for q in question_list:

        index = 0

        for i in q:
            if b'</summary>' in i:
                index = q.index(i)

        if q[index+1: len(q) - 1]:
            t.append(q)

    return t


def get_challenges_count() -> int:
    challenges_path = pathlib.Path(__file__).parent.parent.joinpath('exercises').glob('*.md')
    return len(list(challenges_path))


# WIP WAITING FEEDBACK
def get_random_question(question_list: List[List[bytes]], with_answer=False):
    if with_answer:
        return choice(get_answered_questions(question_list))
    return choice(question_list)


"""Use this question_list. Unless you have already opened/worked/need the file, then don't or
you will end up doing the same thing twice.

eg:

#my_dir/main.py

from scripts import question_utils

print(question_utils.get_answered_questions(question_utils.question_list)

>> 123

"""

question_list = get_question_list(get_file_list())
