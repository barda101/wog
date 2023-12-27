from random import randint
import sys
import os
import time


# def clear():
#     import os
#     os.system('cls')


def generate_sequence(difficulty):
    game_list = []
    for i in range(difficulty):
        game_list.append(randint(1, 101))
    return game_list


def get_list_from_user(difficulty):
    user_list = []
    for i in range(difficulty):
        user_list.append(int(input(f"Enter the {i+1} number: ")))
    return user_list


def is_list_equal(list_1, list_2):
    if sorted(list_1) == sorted(list_2):
        return True
    else:
        return False


def play(diff):
    local_game = generate_sequence(diff)
    print(local_game, end='', flush=True)
    time.sleep(0.7)
    print('\r', end='', flush=True)
    print("Remember? Now Try:")
    # print(local_game)
    local_user = get_list_from_user(diff)
    return is_list_equal(local_game, local_user)

