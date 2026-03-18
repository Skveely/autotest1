import driver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://yandex.by/")
search_box = driver.find_element(By.NAME, "text")
search_query = "хабр
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)
time.sleep(2)
link = driver.find_element(By.LINK_TEXT, "Все статьи в порядке публикации на Хабре")
link.click()
time.sleep(2)
tabs = driver.window_handles
driver.switch_to.window(tabs[-1])
login_button = driver.find_element(By.LINK_TEXT, "Войти")
login_button.click()
time.sleep(2)

#213123
