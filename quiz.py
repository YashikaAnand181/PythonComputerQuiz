print("HEY! WELCOME TO MY COMPUTER QUIZ")

play=input("Do you want to play? ")
if play.lower() !="yes":
    print("You have quit")
    quit()

print("Great! Let's play ")
score=0

ques=input("Name the acid found in Tomato? ")
if ques.lower()=="oxalic acid":
    print("Correct!")
    score +=1
else:
    print('Incorrect!')
ques1=input("What is the pH value of our body? ")
if ques1.lower()=="7.40":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
ques2=input("What is the chemical formula of water? ")
if ques2.lower()=="h2o":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
ques3=input("What many atoms are there in two molecules of water? ")
if ques3.lower()=="6":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
ques4=input("What is the material get deposited on iron when exposed to air? ")
if ques4.lower()=="rust":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You have got " + str(score) + " questions correct.")
print("Your score is" ,score)


