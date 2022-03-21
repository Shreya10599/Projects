#QUIZ GAME

print("Welcome to the quiz")

playing=input("Do you want to continue playing the game? ") #Add a space

if playing.lower() != "yes":
    quit()

#check if the users said yes

if playing != "yes":
    quit() #Quit is a command that ends the program

print("Okay, let's begin playing")

score=0

answer=input("What is the HTML tag for bolding a text? ")

if answer.lower() == "<b>":
    print("correct!")
    score+=1
else: 
    print("Sorry, Incorrect!")

answer= input("What is the tag used for making bulleted lists? ")

if answer.lower()== "<ul>":
    print("correct!")
    score+=1
else:
    print("sorry!Incorrect")
answer= input("What is the tag without ending tag? ")

if answer.lower()== "<br>":
    print("correct!")
    score+=1
else:
    print("sorry!Incorrect")
answer= input("What is the tag for superscript? ")

if answer.lower()== "<sup>":
    print("correct!")
    score+=1
else:
    print("sorry!Incorrect")

answer= input("What is the tag used for including hyperlinks? ")

if answer.lower()== "<a>":
    print("correct!")
    score+=1
else:
    print("sorry!Incorrect")

answer= input("What is the tag used for making numbered lists? ")

if answer.lower()== "<ol>":
    print("correct!")
    score+=1
else:
    print("sorry!Incorrect")
answer= input("What is the tag used for making containers")

if answer.lower()== "<div>":
    print("correct!")
    score+=1
else:
    print("sorry!Incorrect")

answer= input("What does HTML stand for")

if answer.lower()=="Hyper Text MarkUp Language":
    print("correct!")
    score+=1
else:
    print("Sorry!Incorrect")

print("You got " + str(score) + " Questions correct!!!")
print("You got " + str((score/8)*100) + "%")


