age = 20

if age >= 18:
    print("You are eligible to vote")
    ####if
    age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    
    #####
    marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
    #####
    age = 22
citizen = True

if age >= 18:
    if citizen == True:
        print("Eligible to vote")
    else:
        print("Citizenship required")
else:
    print("Age is below 18")