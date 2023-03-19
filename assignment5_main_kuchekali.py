import assignment5_module_kuchekali

# 13 March 2023
# Kurosh Kuchekali

#main fucntion, pretty much the same as before
def main():
    print("Assignment 5: Kurosh Kuchekali\n")
    print("* * The Wizard Game * *\nOk, let's get started\n")
    
    playGame = input("Do you want to talk to the Wizard? (Yes or No)\n")
    
    if playGame.lower().strip() != "yes":
        print("The Wizard wants you to go away now!\n*END OF PROGRAM*\n")
    else:
        print("The Wizard will see you now.\n")
        #calling a function in a module
        assignment5_module_kuchekali.askQuestion()
#runs the mains
if __name__ == "__main__":
    main()
