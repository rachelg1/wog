from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service():
    driver = webdriver.Chrome()
    driver.get(r"http://localhost:5000")
    score = driver.find_element(By.ID, 'score')


# def main_function():
test_scores_service()


