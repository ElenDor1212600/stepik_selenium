import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://SunInJuly.github.io/execute_script.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 100);")

    browser.find_element_by_id("answer").send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()
