import os
player1 = input("Player 1 : Enter rock paper or scissor").strip().lower()
os.system("cls")
player2 = input("Player 2 : Enter rock paper or scissor").strip().lower()
os.system("cls")
if player1 == player2:
    print("It's a tie")
elif (player1 == "rock" and player2 == "scissor") or (player1 == "paper" and player2 == "rock") or (player1 == "scissor" and player2 == "paper"):
    print("Player 1 wins")
elif (player2 == "rock" and player1 == "scissor") or (player2 == "paper" and player1 == "rock") or (player2 == "scissor" and player1 == "paper"):
    print("Player 2 wins")
else:
    print("Invalid input.")
