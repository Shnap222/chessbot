from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

from .Interface import seleniumChessPlayer
from .Interface import Ichessplayer

import time

LOGIN_URL = r"https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/"


class PlayerChessGame(Ichessplayer.ChessPlayer, seleniumChessPlayer.SeleniumChessPlayer):

    def __init__(self, driver_service_path: str, page: str, username, password, bot_player):
        self.username = username
        self.password = password
        self.bot_player = bot_player
        self.bot_player.start()
        super().__init__(service_path=driver_service_path, page=page)

    def run(self):
        self.login()
        # self.start_match()
        # while True:
        #     print(self.wait_for_move())
        #     self.bot_player.move_piece(*self.wait_for_move())
        #     self.move_piece(*self.bot_player.wait_for_move())




    def wait_for_move(self):
        get_last_move = self.driver.find_elements(By.XPATH, "//div[contains(@class,'highlight')]")
        get_highlighted_moves = []
        while get_last_move == get_highlighted_moves:
            time.sleep(0.1)
            get_highlighted_moves = self.driver.find_elements(By.XPATH, "//div[contains(@class,'highlight')]")

        return get_highlighted_moves[0].get_attribute('class')



    def get_rid_of_trial_popup(self):
        try:
            popup_up = self.driver.find_element(By.XPATH, "//div[@class='modal-trial-modal']").is_displayed()
            if self.driver.find_element(By.XPATH, "//div[@class='modal-trial-modal']").is_displayed():
                self.driver.find_element(By.XPATH, "//div[@class='icon-font-chess x ui_outside-close-icon']").click()
        except:
            return

    def move_piece(self, piece, end_place):
        self.action.click(self.driver.find_element(By.XPATH, piece)).perform()
        self.action.click(self.driver.find_elements(By.XPATH, end_place)[-1]).perform()

    def login(self):
        self.get_page(LOGIN_URL)
        self.driver.find_element(By.ID, "username").send_keys(self.username)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.ID, "login").click()

    def set_unranked_black(self):
        self.driver.find_element(By.XPATH, "//button/span[contains(text(),'Custom Game')]").click()
        select = Select(self.driver.find_element(By.XPATH, "//select[@data-cy ='custom-game-option-color']"))
        select.select_by_value('2')
        self.driver.find_element(By.XPATH,
                                 '//button[@class="ui_v5-button-component ui_v5-button-primary custom-game-options-play-button"]').click()

    def start_match(self):
        self.get_page()
        self.get_rid_of_trial_popup()
        self.set_unranked_black()
        # self.driver.find_element()
