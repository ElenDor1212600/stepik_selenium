import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

from selenium import webdriver
link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.find_element_by_css_selector("button[type=submit]").click() # кликнуть на кнопку

    alert = browser.switch_to.alert  # Переключились на окно alert
    alert.accept()    # Нажали в окне кнопочку принять или ок

    time.sleep(2)

    x_element = browser.find_element_by_id("input_value")   #получаем элемент для числа =х
    x = x_element.text   # переменная х = значению элемента
    y = calc(x)         # переменная у = мат. футкции из х

    browser.find_element_by_id("answer").send_keys(y)   # переменную у помещаем в инпут

    browser.find_element_by_css_selector("button[type=submit]").click()   #кликаем на кнопку Отправить



finally:
    time.sleep(10)  #ждем 10 сек
    browser.quit()    #закрыть браузер
