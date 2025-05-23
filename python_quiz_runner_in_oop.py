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
# show the final score after the quiz ends
# Making the quiz program ready to use.