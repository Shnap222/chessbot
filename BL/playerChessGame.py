from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from .Interface import seleniumChessPlayer
from .Interface import Ichessplayer

import time

LOGIN_URL = r"https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/"


class PlayerChessGame(Ichessplayer.ChessPlayer, seleniumChessPlayer.SeleniumChessPlayer):

    def __init__(self, driver_service_path: str, page: str, username, password):
        self.username = username
        self.password = password
        super().__init__(service_path=driver_service_path, page=page)

    def run(self):
        self.login()
        self.start_match()
        # self.move_piece("//div[@class='piece wp square-82']","//div[contains(@class,'square-83')]")
        while True:
            time.sleep(10)

    def wait_for_move(self):
        pass

    def get_rid_of_trial_popup(self):
        if self.driver.find_element(By.XPATH, "//div[@class='modal-trial-modal']").is_displayed():
            self.driver.find_element(By.XPATH, "//div[@class='icon-font-chess x ui_outside-close-icon']").click()

    def move_piece(self, piece, end_place):
        self.action.click(self.driver.find_element(By.XPATH, piece)).perform()
        self.action.click(self.driver.find_elements(By.XPATH, end_place)[-1]).perform()

    def login(self):
        self.get_page(LOGIN_URL)
        self.driver.find_element(By.ID, "username").send_keys(self.username)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.ID, "login").click()

    def start_match(self):
        self.get_page()
        self.get_rid_of_trial_popup()
