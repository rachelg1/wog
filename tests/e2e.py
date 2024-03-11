from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service(url):
    driver = webdriver.Chrome()
    driver.get(url)
    score = driver.find_element(By.ID, 'score').text
    print(score)
    return 1 <= int(score) <= 1000


def main_function(url):
    result = test_scores_service(url)
    if result:
        return 0
    else:
        return -1
