# defining a QuizMaker class to handle quiz creation
class QuizMaker:
    def __init__(self, filename):
        self.filename = filename
        print("Quiz Creator!")


# define a function to save question, options, and answer to a file
    def save_question(self, question, options, answer):
        with open(self.filename, "a") as file:
            file.write(f"Question: {question}\n")
            file.write(f"a. {options['a']}\n")
            file.write(f"b. {options['b']}\n")
            file.write(f"c. {options['c']}\n")
            file.write(f"d. {options['d']}\n")
            file.write(f"Answer: {answer}\n")
            file.write("---\n")

# display the welcome message and run the loop to collect user input
# loop: ask for question, options (a-d), and the correct answer
# save the question to file and ask if the user wants to continue or stop
# Making the quiz program ready to use.