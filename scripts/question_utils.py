"""
Question utils functions
"""

import pathlib
from random import choice
from typing import List
import re

p = pathlib.Path(__file__).parent.parent.joinpath("README.md")


def get_file_list():
    file_list = ""
    with open(p, "rb") as f:
        for line in f.readlines():
            file_list += line.rstrip().decode()
    return file_list


def get_question_list(file_list: List[str]) -> list:
    file_list = re.findall("<details>(.*?)</details>", file_list)
    questions_list = []
    for i in file_list:
        q = re.findall(r"<summary>(.*?)</summary>", i)[0]
        questions_list.append(q)
    return questions_list


def get_answered_questions(question_list: List[str]) -> list:
    t = []
    question_list = re.findall("<details>(.*?)</details>", question_list)
    for i in question_list:
        q = re.findall(r"<summary>(.*?)</summary>", i)
        if q and q[0] == "":
            continue
        a = re.findall(r"<b>(.*?)</b>", i)
        if a and a[0] == "":
            continue
        else:
            t.append(q[0])
    return t


def get_answers_count() -> List:
    """
    Return [answer_questions,all_questions] ,PASS complete. FAIL incomplete.
    >>> get_answers_count()
    [463, 463]
    """
    ans_questions = get_answered_questions(get_file_list())
    len_ans_questions = len(ans_questions)
    all_questions = get_question_list(get_file_list())
    len_all_questions = len(all_questions)
    return [len_ans_questions, len_all_questions]


def get_challenges_count() -> int:
    challenges_path = (
        pathlib.Path(__file__).parent.parent.joinpath("exercises").glob("*.md")
    )
    return len(list(challenges_path))


# WIP WAITING FEEDBACK
def get_random_question(question_list: List[str], with_answer=False):
    if with_answer:
        return choice(get_answered_questions(question_list))
    return choice(get_question_list(question_list))


"""Use this question_list. Unless you have already opened/worked/need the file, then don't or
you will end up doing the same thing twice.
eg:
#my_dir/main.py
from scripts import question_utils
print(question_utils.get_answered_questions(question_utils.question_list)
>> 123
 # noqa: E501
"""

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # print(get_question_list(get_file_list()))
    # print(get_answered_questions(get_file_list()))
    # print(get_random_question(get_file_list(),True))
    # print(get_random_question(get_file_list(),False))
