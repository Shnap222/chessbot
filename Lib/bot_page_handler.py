from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Bot_Page():

    def __init__(self):
        ser = Service(r"C:\Program Files (x86)\chromedriver99.exe")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.driver.implicitly_wait(5)

    def start(self):
