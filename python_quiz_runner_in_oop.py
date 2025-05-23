# import the random library to shuffle questions
import random

# load the questions from file
def load_questions(filename):
    with open(filename, "r") as file:
        content = file.read()
    blocks = content.strip().split("---\n")
    questions = []
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) >= 6:
            questions.append(lines)
    return questions

# set the filename and load the questions
filename = "quiz_bank.txt"
questions = load_questions(filename)

# shuffle the questions randomly
random.shuffle(questions)

# set the initial score to 0 and a welcome message to the user
score = 0
print("Welcome to the Quiz Game!")

# go through each question and ask the user and its answer
for question in questions:
    print("\n" + question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    print(question[4])

    answer = input("Your answer (a/b/c/d): ").strip().lower()
    correct_answer = question[5].split(": ")[1].strip().lower()

    # check if the answer is correct and update the score
    if answer == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is", correct_answer + ".\n")

    # ask the user if they want to continue
    continue_quiz = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_quiz != "yes":
        print("Thanks for playing!")
        break

# show the final score after the quiz ends
print(f"\nFinal score: {score} out of {len(questions)}")