import random
import optparse
import os


def main():
    """Reads through README.md for question/answer pairs and adds them to a
    list to randomly select from and quiz yourself.
    Supports skipping quesitons with no documented answer with the -s flag
    """
    parser = optparse.OptionParser()
    parser.add_option("-s", "--skip", action="store_true",
                      help="skips questions without an answer.",
                      default=False)
    options, args = parser.parse_args()

    with open('README.md', 'r') as f:
        text = f.read()

    questions = []

    while True:
        question_start = text.find('<summary>') + 9
        question_end = text.find('</summary>')
        answer_end = text.find('</b></details>')

        if answer_end == -1:
            break

        question = text[question_start: question_end].replace('<br>', '').replace('<b>', '')
        answer = text[question_end + 17: answer_end]
        questions.append((question, answer))
        text = text[answer_end + 1:]

    num_questions = len(questions)

    while True:
        try:
            question, answer = questions[random.randint(0, num_questions)]

            if options.skip and not answer.strip():
                continue
            os.system("clear")
            print(question)
            print("...Press Enter to show answer...")
            input()
            print('A: ', answer)
            print("... Press Enter to continue, Ctrl-C to exit")
            input()

        except KeyboardInterrupt:
            break

    print("\nGoodbye! See you next time.")


if __name__ == '__main__':
    main()
