import time
import json
from selenium.webdriver.common.by import By

from driver import TestDriver


def find_question(driver):
    question = driver.find_element(By.XPATH, r'//div[@class="qusetion-box"]').text
    return question


def find_answers(driver):
    try:
        answers = driver.find_elements(By.XPATH, r'//div[@class="select-left pull-left options-w"]/div')
        answers = [[i.find_element(By.XPATH, r'./span[1]').text, i.find_element(By.XPATH, r'./span[2]').text] for i in
                   answers]
    except:
        answers = driver.find_elements(By.XPATH, r'//div[@class="select-left pull-left options-w check-box"]/div')
        answers = [[i.find_element(By.XPATH, r'./span[1]').text, i.find_element(By.XPATH, r'./span[2]').text] for i in
                   answers]
    return json.dumps(answers, ensure_ascii=False)


def find_right_answer(driver):
    right_answer = driver.find_element(By.XPATH, r'//div[@class="right-ans"]/b/span').text
    return right_answer


if __name__ == "__main__":
    f = open("test.txt", "a+", encoding="utf-8")
    url = "https://www.kaoshibao.com/online/?paperId=858210&sequence=1"
    my_driver = TestDriver()
    my_driver.init_browser(url)
    q = find_question(my_driver.browser.driver)
    time.sleep(1)
    ans = find_answers(my_driver.browser.driver)
    time.sleep(1)
    r_a = find_right_answer(my_driver.browser.driver)
    line = "\t".join([q, ans, r_a]) + "\n"
    f.write(line)
    for i in range(500):
        my_driver.browser.driver.find_element(By.XPATH, r'//div[@class="next-preve"]/button[2]/span').click()
        q = find_question(my_driver.browser.driver)
        time.sleep(1)
        ans = find_answers(my_driver.browser.driver)
        time.sleep(1)
        r_a = find_right_answer(my_driver.browser.driver)
        line = "\t".join([q, ans, r_a]) + "\n"
        f.write(line)
        print(line)
    f.close()



