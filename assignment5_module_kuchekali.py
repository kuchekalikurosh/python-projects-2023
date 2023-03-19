import random
#import random allows us to use the shuffle function to shuffle the lists

# 13 March 2023
# Kurosh Kuchekali

#this is where the number of questions is gathered
def askQuestion():
    name = input("What's your name?\n")
    numOfQuestions = input("How many questions do you want to ask the Wizard?\n")
    
    #checks if the input is a number
    if numOfQuestions.isnumeric():
        print("Hey " + name + ", you want to ask the Wizard " + numOfQuestions + " questions.\n")
        numOfQuestions = int(numOfQuestions)
        processQuestions(numOfQuestions)
    else:
        print("Error: (" + numOfQuestions + ") is not a valid number.\n*END OF PROGRAM*")

#gets the number of questions users want to ask to answer each question
def processQuestions(f_numOfQuestionsInt):
    #flag is used to break out of the loop once a file was found, otherwise it will keep looping
    fileFlag = 1
    while fileFlag == 1:
        filename = input("Enter the file name here:\n")
        try:
            open(filename, "r")
            fileFlag = 0
        except IOError:
            print("Error: " + filename + " not found.\n")
    
    f_numOfQuestionsInt += 1
    #keeps asking questions until max number is reached or if user says "bye"
    #this is the main loop in which answers are printed as well
    for x in range(1, f_numOfQuestionsInt, 1):
        question = input("What's your question?\n")
        if question.lower().strip() == "bye":
            print("* END OF PROGRAM *")
            exit()
        else:
            firstWord = getFirstWord(question)
            message = getAnswer(firstWord, filename)
            print(message)
    print("You may not ask any more questions!\n")
    
#gets the first word of the question and returns which word that was according to if statements 
def getFirstWord(f_question):
    f_question = f_question.lower()
    if "who" in f_question:
        firstWord = "who"
    elif "what" in f_question:
        firstWord = "what"
    elif "how" in f_question:
        firstWord = "how"
    elif "why" in f_question:
        firstWord = "why"
    elif "when" in f_question:
        firstWord = "when"
    elif "where" in f_question:
        firstWord = "where"
    else:
        firstWord = "I don't know"
    return firstWord

#this function opens the file to read and gets a random answer depending on what the first word is
def getAnswer(f_firstWord, f_filename):
    #these two lists are needed to get the answers
    answersList = []
    lineList = []
    #while the file is open
    with open(f_filename, "r") as infile:
        #reads all of the file until there is nothing left to read
        for line in infile:
            #splits the string when it reads "*"
            lineList = line.split("*")
            #stores the first word before the split on the line list at index 0
            line_keyword = lineList[0]
            #stores the answer relating to the word after the split on the line list at index 1
            line_answer = lineList[1]
            #makes sure the keyword is lowercased
            line_keyword = line_keyword.lower()
            
            #if the keywords match, then append the answer into the answerList
            if line_keyword == f_firstWord:
                answersList.append(line_answer)
        #finds the total number of entries in the list
        listCount = len(answersList)
        #if there is something in the list, then it shuffles the list
        #it then stores the answer from the list into message
        if listCount > 0:
            random.shuffle(answersList)
            message = "The Wizard answers: " + answersList[0] + "\n"
        #if there is nothing on the list, this answer is stored instead
        else:
            message = "The Wizard answers: I don't know\n"
    #returns the message
    return message