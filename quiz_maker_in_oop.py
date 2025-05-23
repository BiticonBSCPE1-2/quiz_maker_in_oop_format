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
    def start(self):
        print("Quiz Creator!")

# loop: ask for question, options (a-d), and the correct answer
        while True:
            question = input("\nEnter your quiz question: ")
            options = {}
            for letter in ['a', 'b', 'c', 'd']:
                options[letter] = input(f"Enter option {letter}: ")

            while True:
                answer = input("Enter the correct answer (a/b/c/d): ").lower()
                if answer in ['a', 'b', 'c', 'd']:
                    break
                else:
                    print("Please enter a, b, c, or d.")

# save the question to file and ask if the user wants to continue or stop
            self.save_question(question, options, answer)
            print("Question added to quiz_bank.txt")

            stop = input("\nEnter '1' to stop adding questions or press any key to continue: ")
            if stop == '1':
                print("\nAll questions saved to quiz_bank.txt.")
                break

# Making the quiz program ready to use.
quiz = QuizMaker("quiz_bank.txt")
quiz.start()