import random

scores = [0, 0]
options = ["r", "p", "s"]
compChoice = ""
rulesDict = {"rock": "smashes scissors", "paper": "wraps rock", "scissors": "cut paper"}


# function to call rules of the game
def rules():
    print("""You are playing rock, paper scissors\n
    To play, please enter r for rock, p for paper or s for scissors
    Remember: Rock smashes Scissors, Paper wraps Rock, Scissors cuts Paper!
    \n*****************************************************\n\n""")

def user_choice(choices):
    print("Rock, paper, scissors... ")
    entry = ""
    while entry not in choices:
        entry = input("please enter 'r', 'p' or 's' to play ")
    else:
        return entry

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

def scoring(onthedoors, whowon):
    if whowon == "You win!":
        onthedoors[0] = onthedoors[0]+1
        print(f"You played: {choiceConfirm} \nThe computer played: {compChoice}\n{choiceConfirm.capitalize()} {rulesDict[choiceConfirm]}!\n{status}")
    elif whowon == "The Computer wins!":
        onthedoors[1] = onthedoors[1]+1
        print(f"You played: {choiceConfirm} \nThe computer played: {compChoice}\n{compChoice.capitalize()} {rulesDict[compChoice]}!\n{status}")
    print(f"\nThe scores are:\nYour score: {scores[0]}\nComputer score: {scores[1]}\n")
    return onthedoors


def winner():
    if scores[0] > scores[1]:
        print("You're the winner! Congratulations!")
    else:
        print("Oh dear you lose... looks like the computer got the best of you this time.")


# prompt the user to enter r/p/s
rules()

# runs until computer or user reaches a score of 3
while scores[0] + scores[1] < 3:

    yourChoice = user_choice(choices=options)

    # convert the value into rock/paper/scissors respectively
    choiceConfirm = check_choice(yourChoice)

    # ask computer to generate a random int between 0-3
    compNum = random.choice(options)

    # convert the computer's choice into rock/paper/scissors
    compChoice = check_choice(compNum)

    # compare the computer's choice with the user's choice
    status = compare(user=choiceConfirm, comp=compChoice)

    # update the scores based on status returned by compare function
    # display whether the user won/drew/lost against the computer
    scoreUpdate = scoring(onthedoors=scores, whowon=status)


#display the winner
winner()
