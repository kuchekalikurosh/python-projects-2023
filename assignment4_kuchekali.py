# 28 Feburary 2023
# Kurosh Kuchekali
# based on assignment 3

#ask question loop
#collects inputs and does outputs
def askQuestion():
    name = input("What's your name?\n")
    numOfQuestion = input("How many questions do you want to ask the Wizard?\n")

    #checks if the input for numOfQuestion is numberical
    #if the input is not numerical, else statement initiates
    if numOfQuestion.isnumeric():
        print("Hey " + name + ", you want to ask the Wizard " + numOfQuestion + " questions.\n")
        numOfQuestion = int(numOfQuestion)
        processQuestion(numOfQuestion)
    else:
        print("Error: " + numOfQuestion + " is not a valid number!\n* END OF PROGRAM *")

#process questions
def processQuestion(f_numOfQuestionsInt):
    f_numOfQuestionsInt += 1

    for x in range (1, f_numOfQuestionsInt, 1):
        question = input("What is your question?\n")
        if question.lower().strip() == "bye":
            print("* END OF PROGRAM *\n")
            break
        else:
            message = getAnswer(question)
            print(message)
    print("You may ask no more questions!\n")

#function that takes a string and sees if it matches with a condition
#if it does not match a condition, then print the generic message
def getAnswer(f_question):
    f_question = str(f_question)
    if f_question.lower().startswith("who"):
        message = "Who, who...isn't that the sound that an owl makes?\n"
    elif f_question.lower().startswith("what"):
        message = "What is the meaning of life?\n"
    elif f_question.lower().startswith("how"):
        message = "How do you do?\n"
    else:
        message = "I don't know\n"
    return "The Wizard answers: " + message

#defining the main fucntion
#the inital program starts from here
def main():
    startMsg = "Assignment 4: Kurosh Kuchekali\n"
    print(startMsg)

    #inital game message
    print("* * The Wizard Game * *\nOk, let's get started!\n")

    playGame = input("Do you want to talk to the Wizard? (Yes or No)")

    #.lower() changes the string to all lowercased characters
    #removes spaces within the input
    if playGame.lower().strip() != "yes":
        print("\nThe Wizard wants you to go away now!\n*END OF PROGRAM*\n")
    else:
        print("\nThe Wizard will see you now.\n")
        askQuestion()
main()