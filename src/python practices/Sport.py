sport = input("Enter a sport: ")
player1_score = int(input("Enter player 1 score: "))
player2_score = int(input("Enter player 2 score: "))

if sport.lower() == "basketball":
    if player1_score == player2_score:
        print("The game is a draw")
    elif player1_score > player2_score:
        print("Player 1 won")
    else:
        print("Player 2 won")

elif sport.lower() == "golf":
    if player1_score == player2_score:
        print("The game is a draw")
    elif player1_score > player2_score:
        print("Player 1 wins")
    else:
        print("player 2 wins")

else:
    print("unknown sport")