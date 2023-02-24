# 1 Feburary 2023
# Kurosh Kuchekali

startMSG = "Assignment 1: Kurosh Kuchekali\n"
print(startMSG)

#inputs
inName = input("Enter your name here: ")
inAge = input("Enter your age here: ")
inSleep = input("Enter average hours of sleep here: ")

#converts string data into int data so it can be used for calculations
inAge = int(inAge)
inSleep = int(inSleep)

sleepcalc = (inSleep / 24) * inAge
#converts int data for string data so it can be printed
sleepcalc = str(sleepcalc)

#final output
print("Hey " + inName + "," + "\n")
print("You have been unconscious for " + sleepcalc + " years!")