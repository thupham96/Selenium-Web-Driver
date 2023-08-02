import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = None
        self.go_button = None
        chrome_driver_path = "/Users/thuan/PycharmProjects/pythonProject/chromedriver_win32"
        self.service = Service(executable_path=chrome_driver_path)
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.down = ""
        self.up = ""
        self.max_duration = 180
        self.finish_loading = False

    def get_internet_speed(self):
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.get("https://www.speedtest.net/")
        self.go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        self.go_button.click()
        start_time = time.time()

        while not self.finish_loading and time.time() - start_time < self.max_duration:
            time.sleep(5)
            self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
            self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
            if self.down != "—" and self.up != "—":
                self.finish_loading = True
                print(self.down)
                print(self.up)

        self.driver.quit()

    def tweet_at_provider(self, username, password, promised_down, promised_up):
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.get("https://twitter.com")
        time.sleep(5)
        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        sign_in_button.click()
        time.sleep(5)
        username_input_box = self.driver.find_element(By.NAME, "text")
        username_input_box.send_keys(username)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        next_button.click()
        time.sleep(5)
        password_input_box = self.driver.find_element(By.NAME, "password")
        password_input_box.send_keys(password)
        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        log_in_button.click()
        time.sleep(5)
        message = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {promised_down}down/{promised_up}up?"
        data_content_box = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-ltr")
        data_content_box.send_keys(message)
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        post_button.click()
