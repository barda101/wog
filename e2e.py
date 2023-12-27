from selenium import webdriver
from time import sleep


def test_score_service():
    mydriver = webdriver.Chrome()
    mydriver.get("http://127.0.0.1:5001")
    user_score = int(mydriver.find_element("id", "score").text)
    if 1 <= user_score <= 1000:
        return True
    else:
        return False


def main_function():
    if test_score_service():
        return 0
    else:
        return -1


print(main_function())


