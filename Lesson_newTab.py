import time
import math
from selenium import webdriver
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    time.sleep(3)
    browser.find_element_by_css_selector("button.trollface").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_css_selector("button[type=submit]").click()


finally:
    time.sleep(10)
    browser.quit()


