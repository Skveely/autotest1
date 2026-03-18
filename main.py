import driver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://yandex.by/")
search_box = driver.find_element(By.NAME, "text")
search_query = "YouTube"
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)
time.sleep(2)
link = driver.find_element(By.LINK_TEXT, "YouTube")
link.click()
time.sleep(2)
tabs = driver.window_handles
driver.switch_to.window(tabs[-1])
login_button = driver.find_element(By.LINK_TEXT, "Shorts")
login_button.click()
time.sleep(5)
# Имитируем нажатие стрелки вниз 5 раз
for i in range(5):
    ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    print(f"Переключил на видео №{i+2}")
    time.sleep(2)


#2131234324234324234

