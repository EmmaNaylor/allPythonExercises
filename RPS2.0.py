import rpsmodule

scores = [0, 0]
accept = ["rock", "paper", "scissors", "r", "p", "s"]
options = ["rock", "paper", "scissors"]
rulesDict = {"rock": "smashes scissors", "paper": "wraps rock", "scissors": "cut paper"}

# prompt the user to enter r/p/s
rpsmodule.rules()

# runs until computer or user reaches a score of 3
while scores[0] + scores[1] < 3:

    # take user choice
    userChoice = rpsmodule.user_select(possibilities=accept, choices=options)

    # ask computer to generate a random int between 0-3
    compChoice = rpsmodule.comp_select(options)

    # compare the computer's choice with the user's choice
    status = rpsmodule.compare(user=userChoice, comp=compChoice)

    # update the scores based on status returned by compare function
    # display whether the user won/drew/lost against the computer
    scoreUpdate = rpsmodule.scoring(current_scores=scores, who_won=status,
                                    user=userChoice, comp=compChoice, reason=rulesDict)

# display the winner
rpsmodule.winner(final=scores)
