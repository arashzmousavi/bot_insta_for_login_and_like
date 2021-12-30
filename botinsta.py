from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time


class Bot:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox()
        self.username = username
        self.password = password

    def Login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        driver.implicitly_wait(10)
        # name
        driver.find_element_by_name("username").send_keys(username)
        # password
        driver.find_element_by_name("password").send_keys(password)
        # button 1
        driver.find_element_by_css_selector('button[type="submit"]').click()
        driver.implicitly_wait(10)
        # button 2
        driver.find_element_by_class_name("cmbtv").click()
        # button 3
        driver.find_element_by_class_name("aOOlW").click()

    def Like(self):
        driver = self.driver
        driver.get("your page for like")
        time.sleep(5)
        # post
        driver.find_element_by_class_name("v1Nh3").click()

        i = 1
        while i <= 5:
            time.sleep(3)
            if driver.find_elements_by_name("Unlike"):
                time.sleep(3)
                driver.find_element_by_class_name("l8mY4").click()
            elif driver.find_elements_by_name("like"):
                time.sleep(3)
                driver.find_elements_by_css_selector(
                    'button[type="button"]').click()
                time.sleep(3)
                driver.find_element_by_class_name("l8mY4").click()
            i += 1


username = "your page"
password = "your password page"
test = Bot(username, password)
test.Login()
test.Like()
