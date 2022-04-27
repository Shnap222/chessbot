from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from .Interface import seleniumChessPlayer
from .Interface import Ichessplayer

import time


class BotChessGame(Ichessplayer.ChessPlayer, seleniumChessPlayer.SeleniumChessPlayer):

    def __init__(self, driver_service_path: str, page: str):
        super().__init__(service_path=driver_service_path, page=page)

    def run(self):
        self.start_match()
        self.move_piece("//div[@class='piece wp square-82']", "//div[contains(@class,'square-83')]")
        print(self.wait_for_move())

    def wait_for_move(self):
        # todo make it work
        get_last_move = self.driver.find_elements(By.XPATH, "//div[contains(@class,'highlight')]")
        print("last_move")
        print(get_last_move)

        get_highlighted_moves = get_last_move

        while get_last_move == get_highlighted_moves or len(get_highlighted_moves) != 2:
            time.sleep(0.1)
            get_highlighted_moves = self.driver.find_elements(By.XPATH, "//div[contains(@class,'highlight')]")
            print(get_last_move[0].get_attribute('class') == get_highlighted_moves[0].get_attribute('class'))
            print(get_last_move[0].get_attribute('class'))
            print(get_highlighted_moves[0].get_attribute('class'))
            print(get_highlighted_moves)

        return get_highlighted_moves

    def move_piece(self, piece: str, end_place: str):
        self.action.click(self.driver.find_element(By.XPATH, piece)).perform()
        self.action.click(self.driver.find_elements(By.XPATH, end_place)[-1]).perform()

    def start_match(self):
        self.get_page()

        ok_button = self.driver.find_element(By.XPATH,
                                             '//button[@class="ui_v5-button-component ui_v5-button-primary ui_v5-button-large ui_v5-button-full"]')
        ok_button.click()
        bot_level__button = self.driver.find_elements(By.XPATH, '//div[@class="bot-component"]')
        bot_level__button[-1].click()
        slider = self.driver.find_element(By.XPATH, '//input[@class="slider-input"]')
        self.action.click_and_hold(slider).move_by_offset(450, 0).perform()
        start_button = self.driver.find_element(By.XPATH,
                                                '//button[@class="ui_v5-button-component ui_v5-button-primary ui_v5-button-large selection-menu-button"]')
        start_button.click()
        start_button = self.driver.find_element(By.XPATH,
                                                '//button[@class="ui_v5-button-component ui_v5-button-primary ui_v5-button-large ui_v5-button-full"]')
        start_button.click()
