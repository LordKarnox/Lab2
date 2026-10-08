"""
Program: Main program
Author: Pattharasittha Deevech
Purpose: Run a 2 player coin match game.
Starer code: None
Date: October 8, 2026
"""



from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    play = input("Do you want to toss the coins? (y/n)").strip()

    while play.lower() == "y":
        print("Tossing...")
        player1.toss_coin()
        player2.toss_coin()
        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed: {player1.get_coin_side()}")
        print(f"{player2.get_name()} tossed: {player2.get_coin_side()}")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print(f"It's a match! {player1.get_name()} wins a coin and {player2.get_name()} loses a coin.")
        else:
            player1.lose_coin()
            player2.win_coin()
            print(f"No match! {player2.get_name()} wins a coin and {player1.get_name()} loses a coin.")


        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

        if player1.get_wallet() == 0:
            print(f"Game Over! {player1.get_name()} has no coins left and loses.")
            break
        elif player2.get_wallet() == 0:
            print(f"Game Over! {player2.get_name()} has no coins left and loses.")
            break
         
        play = input("Do you want to toss the coins again? (y/n)").strip()

    print("Final Scores")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    if player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} wins the game!")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"{player2.get_name()} wins the game!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()