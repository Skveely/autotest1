import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

def test_open_shorts(driver):
# Открыть ссылку
    driver.get("https://yandex.by/")
# Найти строку поиска
    search_box = driver.find_element(By.NAME, "text")
    time.sleep(5)
# Ввести "YouTube"
    search_query = "YouTube"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
# Переходим на YouTube
    link = driver.find_element(By.LINK_TEXT, "YouTube")
    link.click()
# Переключаемся на новую вкладку
    tabs = driver.window_handles
    driver.switch_to.window(tabs[-1])
    time.sleep(5)
 # Ищем Shorts
    login_button = driver.find_element(By.LINK_TEXT, "Shorts")
    login_button.click()
    time.sleep(5)
    assert "shorts" in driver.current_url.lower()
# Имитируем нажатие стрелки вниз 5 раз
   # for i in range(5):
  #      ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
   # time.sleep(2)



def fix(driver):
    assert 1==1




