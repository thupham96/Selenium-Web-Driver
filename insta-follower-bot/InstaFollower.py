from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


class InstaFollower():
    def __init__(self):
        chrome_driver_path = "/Users/thuan/PycharmProjects/pythonProject/chromedriver_win32"
        service = Service(executable_path=chrome_driver_path)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service, options=options)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(username)
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        submit_button.click()
        time.sleep(5)

    def find_followers(self, account):
        self.driver.get(f"https://www.instagram.com/{account}/following/")
        time.sleep(5)
        scrollable_popup = self.driver.find_element(By.CLASS_NAME, '_aano')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.XPATH, "//*[contains(@class, '_aacw') and contains(@class, '_aad6') and contains(@class, '_aade')]")
        for follow in follow_buttons:
            print(follow.text)
            if follow.text == "Follow":
                try:
                    follow.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    print("Skip")

        self.driver.quit()
