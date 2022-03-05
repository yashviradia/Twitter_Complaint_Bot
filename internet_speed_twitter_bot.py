from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

PROMISED_DOWN = 150
PROMISED_UP = 10
ACCOUNT_NAME = os.environ.get("YOUR_ACCOUNT_NAME")
ACCOUNT_PASSWORD = os.environ.get("YOUR_ACCOUNT_PASSWORD")

chrome_driver_path = os.environ.get("YOUR_CHROME_DRIVER_PATH")
DRIVER = webdriver.Chrome(service=Service(chrome_driver_path))
DRIVER.maximize_window()
DRIVER.implicitly_wait(5)


class InternetSpeedTwitterBot:
    # checking the speed of the internet
    def __init__(self):
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        DRIVER.get("https://www.speedtest.net/")
        go_button = DRIVER.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")

        time.sleep(30)
        go_button.click()

        time.sleep(60)
        self.up = DRIVER.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span")
        self.down = DRIVER.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")

        upload_speed = self.up.text
        download_speed = self.down.text

        print(upload_speed)
        print(download_speed)

    def tweet_at_provider(self):
        DRIVER.get("https://twitter.com/i/flow/login")

        username_input = DRIVER.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input")
        username_input.send_keys(ACCOUNT_NAME)

        proceed_button = DRIVER.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span")
        proceed_button.click()

        password_input = DRIVER.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password_input.send_keys(ACCOUNT_PASSWORD)

        login_button = DRIVER.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/span/span")
        login_button.click()

        time.sleep(2)

        if (int(self.up.text) < PROMISED_UP) and (int(self.down.text) < PROMISED_DOWN):
            twitter_space = DRIVER.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
            twitter_space.send_keys(f"Hey Internet Provider, why is my internet speed \n{self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")

            tweet_button = DRIVER.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div")
            tweet_button.click()