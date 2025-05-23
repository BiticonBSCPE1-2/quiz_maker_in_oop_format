# define a function to save question, options, and answer to a file
def questions(filename, question, options, answer):
    with open(filename, "a") as file:
        file.write(f"Question: {question}\n")
        file.write(f"a. {options['a']}\n")
        file.write(f"b. {options['b']}\n")
        file.write(f"c. {options['c']}\n")
        file.write(f"d. {options['d']}\n")
        file.write(f"Answer: {answer}\n")
        file.write("---\n")

# display a title and set the output filename
print("Quiz Creator!")
filename = "quiz_bank.txt"

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
    questions(filename, question, options, answer)
    print("Question added to quiz_bank.txt")

    print("\nEnter '1' to stop adding questions or press any key to continue.")
    stop = input()
    if stop == '1':
        print("\n All questions saved to quiz_bank.txt.")
        break