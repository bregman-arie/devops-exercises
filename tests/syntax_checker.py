"""
Testing suite for https://github.com/bregman-arie/devops-interview-questions
written by surister

Even though both check_details_tag and check_summary_tags are practically the
same, due to readability and functionality it was decided to be split like
that.

Usage:
$ python tests/syntax_checker.py

"""

import pathlib

p = pathlib.Path(__file__).parent.parent.joinpath('README.md')

with open(p, 'rb') as f:
    file_list = [line.rstrip() for line in f.readlines()]

errors = []


def count_details(file_list):
    """
    Counts the total amount of <details> and </details>

    Used for debugging purpose, not meant to be used in actual tests
    """
    details_final_count = 0
    details_count = 0

    for line_number, line in enumerate(file_list):
        if b'<details>' in line:
            details_count += 1
        if b'</details>' in line:
            details_final_count += 1

    return details_count, details_final_count


def check_details_tag(file_list):
    """
    Check whether the structure:
    <details>
    ...
    </details>

    Is correctly followed, if not generates an error.

    """

    after_detail = False
    error = False
    err_message = ''
    for line_number, line in enumerate(file_list):
        if b'<details>' in line and b'</details>' in line:
            pass
        else:
            if b'<details>' in line and after_detail:
                error = True
            if b'</details>' in line and not after_detail:
                err_message = 'Missing opening detail tag'
                error = True

            if b'<details>' in line:
                after_detail = True

            if b'</details>' in line and after_detail:
                err_message = 'Missing closing detail tag'
                after_detail = False

            if error:
                raise Exception(f'{err_message} at line {line_number -1}')


def check_summary_tag(file_list):
    """
    Check whether the structure:
    <summary>
    ...
    </summary>

    Is correctly followed, if not generates an error.

    """

    after_detail = False
    error = False
    err_message = ''
    for line_number, line in enumerate(file_list):
        if b'<summary>' in line and b'</summary>' in line:
            pass
        else:
            if b'<summary>' in line and after_detail:
                error = True
            if b'</summary>' in line and not after_detail:
                err_message = 'Missing opening detail tag'
                error = True

            if b'<summary>' in line:
                after_detail = True

            if b'</summary>' in line and after_detail:
                err_message = 'Missing closing detail tag'
                after_detail = False

            if error:
                raise Exception(f'{err_message} at line {line_number -3}')


if __name__ == '__main__':
    check_details_tag(file_list)
    check_summary_tag(file_list)
    print("tests passed successfully")
