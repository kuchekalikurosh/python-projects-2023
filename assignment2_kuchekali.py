# 15 Feburary 2023
# Kurosh Kuchekali

#ask question loop
#collects inputs and does outputs
def askQuestion():
    name = input("What's your name?\n")
    question = input("What's your question?\n")
    while question != "bye":
        print("Hey " + name + "! What kind of question is '" + question + "'?\n")
        question = input("What's your question?\n")
    print("*END OF PROGRAM*")
    
#defining the main fucntion
#the inital program starts from here
def main():
    startMsg = "Assignment 2: Kurosh Kuchekali\n"
    print(startMsg)

    #inital game message
    print("* * The Wizard Game * *\nOk, let's get started!\n")

    print("Do you want to talk to the Wizard? (Yes or No)")
    playGame = input()

    if playGame != "Yes":
        print("\nThe Wizard wants you to go away now!\n*END OF PROGRAM*\n")
    if playGame == "Yes":
        print("\nThe Wizard will see you now.\n")
        askQuestion()
main()