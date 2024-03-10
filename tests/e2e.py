from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service():
    driver = webdriver.Chrome()
    driver.get(r"http://localhost:5000")
    score = driver.find_element(By.ID, 'score').text
    print(score)
    return 1 >= int(score) >= 1000


def main_function():
    result = test_scores_service()
    if result:
        return 0
    else:
        return -1
