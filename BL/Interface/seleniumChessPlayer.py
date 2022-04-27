from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import threading

from . import Ichessplayer


class SeleniumChessPlayer(threading.Thread):

    def __init__(self, service_path: str, page: str):
        self.page = page
        ser = Service(service_path)
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.driver.implicitly_wait(5)
        self.action = ActionChains(self.driver)
        super().__init__()

    def get_page(self, page: str = ""):
        self.driver.get(page if page else self.page)

    def start_match(self):
        pass

    def move_piece(self, piece, end_place):
        pass
