import Utils
import os


def add_score(diff):
    if os.path.exists(Utils.SCORES_FILE_NAME):
        # print("Yes")
        f = open(Utils.SCORES_FILE_NAME, 'r')
        current_number = int(f.read())
        f = open(Utils.SCORES_FILE_NAME, 'w')
        f.write(str(current_number + ((diff * 3) + 5)))
    else:
        f = open(Utils.SCORES_FILE_NAME, 'x')
        # f.write(str(0))
        f = open(Utils.SCORES_FILE_NAME, 'w')
        f.write(str((diff * 3) + 5))

