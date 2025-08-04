# First working version of the game, for now only coin toss.

from coin_toss import CoinToss


player_input = int(input("Heads [1] or Tails [2]: "))
player_guess = "Heads" if player_input == 1 else "Tails"


game = CoinToss()
coin_result = game.play()  

print(f"Your coin: {player_guess}")
print(f"Coin landed on: {coin_result}")

if player_guess == coin_result:
    print("You win!")
else:
    print("You lose.")
