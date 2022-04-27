from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from SeleniumUtils import Utils

from BL import botChessGame, playerChessGame

CHESS_MAIN_URL = "https://www.chess.com/play/online"
CHESS_BOT_URL = "https://www.chess.com/play/computer"

USERNAME = "spiff3690"
PASSWORD = "Password1!"


def main():
    driver.get(CHESS_BOT_URL)
    ok_button = driver.find_element(By.XPATH,
                                    '//button[@class="ui_v5-button-component ui_v5-button-primary ui_v5-button-large ui_v5-button-full"]')
    ok_button.click()
    bot_level__button = driver.find_elements(By.XPATH, '//div[@class="bot-component"]')
    bot_level__button[-1].click()
    slider = driver.find_element(By.XPATH, '//input[@class="slider-input"]')
    move.click_and_hold(slider).move_by_offset(450, 0).perform()
    start_button = driver.find_element(By.XPATH,
                                       '//button[@class="ui_v5-button-component ui_v5-button-primary ui_v5-button-large selection-menu-button"]')
    start_button.click()
    start_button = driver.find_element(By.XPATH,
                                       '//button[@class="ui_v5-button-component ui_v5-button-primary ui_v5-button-large ui_v5-button-full"]')
    start_button.click()


if __name__ == '__main__':
    # ser = Service(r"C:\Program Files (x86)\chromedriver99.exe")
    # op = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(service=ser, options=op)
    # driver.implicitly_wait(5)
    # move = ActionChains(driver)
    # main()
    bot_player = botChessGame.BotChessGame(r"C:\Program Files (x86)\chromedriver99.exe", CHESS_BOT_URL)
    playerChessGame.PlayerChessGame(r"C:\Program Files (x86)\chromedriver99.exe", CHESS_MAIN_URL, username=USERNAME,
                                    password=PASSWORD, bot_player=bot_player).start()
