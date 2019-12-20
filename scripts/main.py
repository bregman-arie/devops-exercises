import pathlib

p = pathlib.Path(__file__).parent.parent.joinpath('README.md')

with open(p, 'rb') as f:
    file_list = [line.rstrip() for line in f.readlines()]

details_final_count = 0
details_count = 0
print(len(file_list))
for q in file_list:
    if b'<details>' in q:
        details_count += 1
    if b'</details>' in q:
        details_final_count += 1
print(details_count, details_final_count)

# TODO Checkear que tenemos mismo numero de details tabs, aunque esto no asegura al 100%  que esta bien formateado.
# Una vez que tenemos un número par, podemos más o menos estar seguros de que la cosa va bien, y hacer ya entonces
# el checkeo de las demás tags.
# Problema: No obtenemos el lugar de donde esta mal el details, entonces; hacerlo.
# IDEA: comprobar que despues de un detail va un /detail y mas o menos supongo que podremos acotar, hacer pruebas.


def get_question_list(f):

    questions_list = []
    temp = []
    after_summary_tag = False

    for line in f:
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


def get_answered_questions(question_list) -> int:
    c = 0
    for q in question_list:
        index = 0
        for i in q:
            if b'</summary>' in i:
                index = q.index(i)
        if q[index+1: len(q) - 1]:
            # print(q[2: len(q) - 1], '-->', q)
            c += 1
    return c


def check_even_tags(question_list):
    summary_count = 0
    details_count = 0
    # details count not necessary cus we already have that checked beforehand
    for q in question_list:
        print(q)
        for l in q:
            print(l)
            if b'<details>' in l:
                details_count += 1
            if b'<summary>' in l:
                summary_count += 1
            if b'</details>' in l:
                details_count += 1
            if b'</summary>' in l:
                summary_count += 1
            print(summary_count, details_count)
        if summary_count != 2 or details_count != 2:
            raise Exception(f'You are missing a tag in {q}')
        details_count = 0
        summary_count = 0


# check_even_tags(get_question_list(file_list))


# if __name__ == '__main__':
#     q_list = get_question_list(file_list)
#     print(len(q_list))
#     print(get_answered_questions(q_list))
