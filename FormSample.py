

firstName = str(input ("please enter your First name: "))
lastName = str(input("Please enter your Last name: "))
Age = int(input("What is your age? "))
DOB = "3/19/2008"


def AgeIsValid(ageToCheck) :
    if isinstance(ageToCheck, int):
        return True
    else:
        return False

message = "Sorry, please try entering our site when you are 18 or older."
 
if AgeIsValid(Age):
    print(f"Age successfully validated - value entered is: {Age}.")
else:
    print("Incorrect Input: please ensure you enter a valid integer value for your age.")

if (Age >= 18):
    message = "Welcome to our site!"

if (type(firstName) != str) or (type(lastName) != str) :
    print("Incorrect input: Please ensure your First and Last names are valid strings.\n\n")
else:
    print(f"First and Last names successfully validated. The name entered was \'{firstName} {lastName}\'.\n\n")
 
print(f"Hello {firstName} {lastName}, I see that your date of birth is {DOB} and your age is {Age}.")
print (message + "\n\n")