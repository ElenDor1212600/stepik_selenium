import os  # импортируем модуль
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()

try:

    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "input[name=firstname]").send_keys("Elena")  # вставить значение в поле

    browser.find_element(By.CSS_SELECTOR, "input[name=lastname]").send_keys("Dor")  # вставить значение в поле

    browser.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys("Helena@gmail.com")  # вставить значение в поле

    current_dir = os.path.abspath(
        os.path.dirname('__file__'))  # получаем путь к директории текущего исполняемого скрипта .py
    file_name = "lena.txt"  # имя файла, который будем загружать на сайт
    file_path = os.path.join(current_dir, file_name)  # получаем путь к file_example.txt
    browser.find_element(By.ID, "file").send_keys(file_path)  # отправляем файл

    button = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")  # определяем кнопку отправки
    button.click()  # кликаем на Отправить

finally:
    time.sleep(10)
    browser.quit()
