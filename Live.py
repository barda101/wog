import GuessGame, MemoryGame, CurrencyRouletteGame, Score

vals = []


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\nhere you can find many cool games to play.")


def load_game():
    while True:
        try:
            game = int(input("""
            Please choose a game to play:
                1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
                2. Guess Game - guess a number and see if you chose like the computer
                3. Currency Roulette - try and guess the value of a random amount of USD in ILS
            ----> """))
        except ValueError:
            print("Please enter a valid number 1-3")
            continue
        if game in range(1, 4):
            vals.append(game)
            break
        else:
            print("The number must be in the range 1-3")

    while True:
        try:
            diff = int(input("Please choose game difficulty from 1 to 5: "))
        except ValueError:
            print("Please enter a valid number 1-5")
            continue
        if diff in range(1, 6):
            vals.append(diff)
            break
        else:
            print("The number must be in the range 1-5")
    print(vals)
    return vals


def start():
    welcome(input("Enter your name: "))
    temp = load_game()
    game_diff = (temp[0], temp[1])
    print(game_diff)
    if game_diff[0] == 1:
        if MemoryGame.play(game_diff[1]):
            print("Win")
            Score.add_score(game_diff[1])
        else:
            print("Loss")
    elif game_diff[0] == 2:
        if GuessGame.play(game_diff[1]):
            print("Win")
            Score.add_score(game_diff[1])
        else:
            print("Loss")
    elif game_diff[0] == 3:
        if CurrencyRouletteGame.play(game_diff[1]):
            print("Win")
            Score.add_score(game_diff[1])
        else:
            print("Loss")


