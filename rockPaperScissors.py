import random

userScore = 0
compScore = 0
options = ["r", "p", "s"]
yourChoice = ""
userChoice = ""
compChoice = ""


# function to call rules of the game
def rules():
    print("""You are playing rock, paper scissors\n
    To play, please enter r for rock, p for paper or s for scissors
    Remember: Rock smashes Scissors, Paper wraps Rock, Scissors cut Paper!
    \n*****************************************************\n\n""")

# function to convert single letter choice to full length choice
def check_choice(choice):
    if choice == "r":
        return "rock"
    elif choice == "p":
        return "paper"
    else:
        return "scissors"

# function to compare user's choice with computer's choice
def compare(user, comp):
    if user == comp:
        return "It's a draw!"
    else:
        if user == "rock":
            if comp == "scissors":
                return "You win!"
            else:
                return "The Computer wins!"
        elif user == "paper":
            if comp == "rock":
                return "You win!"
            else:
                return "The Computer wins!"
        else:
            if comp == "paper":
                return "You win!"
            else:
                return "The Computer wins!"


# prompt the user to enter r/p/s
rules()

# runs until computer or user reaches a score of 3
while userScore < 3 and compScore < 3:

    firstChoice = input("Rock, paper, scissors... ")
    try:
        yourChoice = firstChoice[0].lower()
        if yourChoice not in options:
            print("I didn't recognise that entry... please try again ")
    except IndexError:
        print("please enter 'r', 'p' or 's' to play")
        continue

    # convert the value into rock/paper/scissors respectively
    userChoice = check_choice(yourChoice)

    # ask computer to generate a random int between 0-3
    compNum = random.choice(options)

    # convert the computer's choice into rock/paper/scissors
    compChoice = check_choice(compNum)

    # compare the computer's choice with the user's choice
    status = compare(userChoice, compChoice)
    
    # alter scores based on status returned by compare function (may be able to be a function - but issues caused by local/global in first attempt)
    if status == "You win!":
        userScore += 1
    elif status == "The Computer wins!":
        compScore += 1

    # display whether the user won/drew/lost against the computer
    print(f"You played: {userChoice} \nThe computer played: {compChoice}\n{status}")
    print(f"\nThe scores are:\nYour score: {userScore}\nComputer score: {compScore}\n")
