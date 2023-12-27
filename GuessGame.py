from random import randint


def generate_number(difficulty):
    return randint(1, difficulty)


def get_guess_from_user(difficulty):
    return int(input(f"Choose a number between 1 to {difficulty} "))


def play(diff):
    secret_number = generate_number(diff)
    #print(secret_number)
    number_from_user = get_guess_from_user(diff)
    #print(number_from_user)
    if secret_number == number_from_user:
        return True
    else:
        return False




