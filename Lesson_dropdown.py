import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
try:
    browser.get(link)

    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text

    sum_int = int(x) + int(y)
    sum_str = str(sum_int)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum_str)  # ищем элемент с текстом "Python"

    browser.find_element_by_css_selector("button[type=submit]").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
