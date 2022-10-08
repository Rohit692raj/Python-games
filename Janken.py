import random
def getchoice():
    player_choice = input("Enter your choice [ Rocks Paper Scissors\n")
    list1 = ["Rocks", "Paper", "Scissors"]
    computer_choice = random.choice(list1)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices
def check_win(player,computer):
    if player == computer:
        return "its a tie"
    else:
        if player == "Rocks" and computer == "Scissors":
            return "player wins"
        elif player == "Scissors" and computer == "Rocks":
            return "computer wins"
        elif player == "Rocks" and computer == "Paper":
            return "computer wins"
        elif player == "Paper" and computer == "Rocks":
            return "player wins"
        elif player == "Paper" and computer == "Scissors":
            return "computer wins"
        elif player == "Scissors" and computer == "Paper":
            return "player wins"
        else:
            return "valid arguments"
chocies = getchoice()
print(chocies)
player = chocies["player"]
computer = chocies["computer"]

win = check_win(player,computer)
print(win)


