"""
Meant to be used like this:

python scripts/update_question_number.py

"""
import pathlib
from scripts.question_utils import get_question_list, get_challenges_count

LINE_FLAG = b":bar_chart:"

p = pathlib.Path(__file__).parent.parent.joinpath('README.md')


with open(p, 'rb') as f:
    file = f.readlines()


file_list = [line.rstrip() for line in file]

question_list = get_question_list(file_list)
question_count = len(question_list)
total_count = question_count + get_challenges_count()
print(question_count)
print(get_challenges_count())
print(total_count)
for line in file:
    if LINE_FLAG in line:
        file[file.index(line)] = b':bar_chart: &nbsp;There are currently **%s** questions\r\n' %\
                                 str(total_count).encode()
        break

with open(p, 'wb') as f:
    f.writelines(file)
