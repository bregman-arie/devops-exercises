"""
Testing suite for https://github.com/bregman-arie/devops-interview-questions
written by surister

Even though both check_details_tag and check_summary_tags are practically the
same, due to readability and functionality it was decided to be split like
that.

Usage:
$ python tests/syntax_lint.py

"""

import sys

p = sys.argv[1]


errors = []


def count_details(file_list):
    """
    Counts the total amount of <details> and </details>

    Used for debugging purpose, not meant to be used in actual tests
    """
    details_final_count = 0
    details_count = 0

    for line_number, line in enumerate(file_list):
        if b"<details>" in line:
            details_count += 1
        if b"</details>" in line:
            details_final_count += 1

    return details_count == details_final_count


def count_summary(file_list):
    """
    Counts the total amount of <details> and </details>

    Used for debugging purpose, not meant to be used in actual tests
    """
    details_final_count = 0
    details_count = 0

    for line_number, line in enumerate(file_list):
        if b"<summary>" in line:
            details_count += 1
        if b"</summary>" in line:
            details_final_count += 1

    return details_count == details_final_count


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
    err_message = ""
    for line_number, line in enumerate(file_list):
        if b"<details>" in line and b"</details>" in line:
            pass
        else:
            if b"<details>" in line and after_detail:
                err_message = f"Missing closing detail tag round line {line_number - 1}"
                error = True
            if b"</details>" in line and not after_detail:
                err_message = f"Missing opening detail tag round line {line_number - 1}"
                error = True

            if b"<details>" in line:
                after_detail = True

            if b"</details>" in line and after_detail:
                after_detail = False

            if error:
                errors.append(err_message)

        error = False


def check_summary_tag(file_list):
    """
    Check whether the structure:
    <summary>
    ...
    </summary>

    Is correctly followed, if not generates an error.

    """

    after_summary = False
    error = False
    err_message = ""
    for idx, line in enumerate(file_list):
        line_number = idx + 1
        if b"<summary>" in line and b"</summary>" in line:
            if after_summary:
                err_message = f"Missing closing summary tag around line {line_number}"
                error = True

        else:
            if b"<summary>" in line and after_summary:
                err_message = f"Missing closing summary tag around line {line_number}"
                error = True
            if b"</summary>" in line and not after_summary:
                err_message = f"Missing opening summary tag around line {line_number}"
                error = True

            if b"<summary>" in line:
                after_summary = True

            if b"</summary>" in line and after_summary:
                after_summary = False

        if error:
            errors.append(err_message)

        error = False


def check_md_file(file_name):
    with open(p, "rb") as f:
        file_list = [line.rstrip() for line in f.readlines()]
    check_details_tag(file_list)
    check_summary_tag(file_list)


if __name__ == "__main__":
    print(f"..........Checking {p}..........")
    check_md_file(p)
    if errors:
        print(f"{p} failed", file=sys.stderr)
        for error in errors:
            print(error, file=sys.stderr)
        exit(1)

    print("Tests passed successfully.")
