# import the random library to shuffle questions
import random

# load the questions from file
class QuizRunner:
    def __init__(self, filename):
        self.filename = filename
        self.questions = self.load_questions()
        self.score = 0

    def load_questions(self):
        with open(self.filename, "r") as file:
            content = file.read()
        blocks = content.strip().split("---\n")
        questions = []
        for block in blocks:
            lines = block.strip().split("\n")
            if len(lines) >= 6:
                questions.append(lines)
        return questions
    
# load the questions and shuffle the questions randomly
    def start_quiz(self):
        random.shuffle(self.questions)

# set the initial score to 0 and a welcome message to the user
        self.score = 0
        print("Welcome to the Quiz Game!")

# go through each question and ask the user and its answer
        for question in self.questions:
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
                self.score += 1
            else:
                print("Wrong! The correct answer is", correct_answer + ".\n")

            # ask the user if they want to continue
            continue_quiz = input("Do you want to continue? (yes/no): ").strip().lower()
            if continue_quiz != "yes":
                print("Thanks for playing!")
                break

# show the final score after the quiz ends
        print(f"\nFinal score: {self.score} out of {len(self.questions)}")

# Making the quiz program ready to use.
quiz = QuizRunner("quiz_bank.txt")
quiz.start_quiz()
