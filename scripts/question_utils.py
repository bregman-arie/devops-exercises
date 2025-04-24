"""
Question utils functions
"""

import pathlib
from random import choice
from typing import List
import re

README_PATH = pathlib.Path(__file__).parent.parent / "README.md"
EXERCISES_PATH = pathlib.Path(__file__).parent.parent / "exercises"

DETAILS_PATTERN = re.compile(r"<details>(.*?)</details>", re.DOTALL)
SUMMARY_PATTERN = re.compile(r"<summary>(.*?)</summary>", re.DOTALL)
B_PATTERN = re.compile(r"<b>(.*?)</b>", re.DOTALL)


def get_file_content() -> str:
    with README_PATH.open("r", encoding="utf-8") as f:
        return f.read()


def get_question_list(file_content: str) -> List[str]:
    details = DETAILS_PATTERN.findall(file_content)
    return [
        SUMMARY_PATTERN.search(detail).group(1)
        for detail in details
        if SUMMARY_PATTERN.search(detail)
    ]


def get_answered_questions(file_content: str) -> List[str]:
    details = DETAILS_PATTERN.findall(file_content)
    answered = []
    for detail in details:
        summary_match = SUMMARY_PATTERN.search(detail)
        b_match = B_PATTERN.search(detail)
        if (
                summary_match
                and b_match
                and summary_match.group(1).strip()
                and b_match.group(1).strip()
        ):
            answered.append(summary_match.group(1))
    return answered


def get_answers_count() -> List[int]:
    file_content = get_file_content()
    answered = get_answered_questions(file_content)
    all_questions = get_question_list(file_content)
    return [len(answered), len(all_questions)]


def get_challenges_count() -> int:
    return len(list(EXERCISES_PATH.glob("*.md")))


def get_random_question(question_list: List[str], with_answer: bool = False) -> str:
    if with_answer:
        return choice(get_answered_questions(get_file_content()))
    return choice(get_question_list(get_file_content()))


"""Use this question_list. Unless you have already opened/worked/need the file, then don't or
you will end up doing the same thing twice.
eg:
# my_dir/main.py
from scripts import question_utils

print(
    question_utils.get_answered_questions(
        question_utils.get_question_list(
            question_utils.get_file_content()
        )
    )
)
>> 123
"""

if __name__ == "__main__":
    import doctest

    doctest.testmod()
