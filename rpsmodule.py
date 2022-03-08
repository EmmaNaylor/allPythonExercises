import random

# function to call rules of the game


def rules():
    print("""You are playing rock, paper scissors\n
    Today's game is best out of 3!
    To play, please enter r for rock, p for paper or s for scissors
    Remember: Rock smashes Scissors, Paper wraps Rock, Scissors cuts Paper!
    \n*****************************************************\n\n""")


# function to accept user input


def user_select(possibilities, choices):
    print("Rock, paper, scissors... ")
    entry = ""
    while entry not in possibilities:
        entry = input("please enter 'r', 'p' or 's' to play: ")
    if entry not in choices:
        user_entry = convert_choice(entry)
        return user_entry
    else:
        return entry

# function to accept user input


def comp_select(choices):
    comp_num = random.choice(choices)
    return comp_num


# function to convert single letter choice to full length choice


def convert_choice(choice):
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


# function to alter scores based on outcome of comparison function


def scoring(current_scores, who_won, user, comp, reason):
    if who_won == "You win!":
        current_scores[0] = current_scores[0]+1
        print(f"""\nYou played: {user} \nThe computer played: {comp}
        \n{user.capitalize()} {reason[user]}!\n{who_won}""")
    elif who_won == "The Computer wins!":
        current_scores[1] = current_scores[1]+1
        print(f"""\nYou played: {user} \nThe computer played: {comp}
        \n{comp.capitalize()} {reason[comp]}!\n{who_won}""")
    else:
        print(f"""\nYou played: {user} \nThe computer played: {comp}
                \nIt's a tie!""")
    print(f"\nThe scores are:\nYour score: {current_scores[0]}\nComputer score: {current_scores[1]}\n")
    return current_scores


# function to call the overall winner of the game


def winner(final):
    if final[0] > final[1]:
        print("You're the winner! Congratulations!")
    else:
        print("Oh dear you lose... looks like the computer got the best of you this time.")
