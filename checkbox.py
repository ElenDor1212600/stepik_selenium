import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)
    option1 = browser.find_element_by_css_selector('input[type=checkbox]')
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    browser.find_element_by_css_selector("button[type=submit]").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
