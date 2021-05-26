from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

try:
    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element_by_id('answer').send_keys(y)
    input2 = browser.find_element_by_id('robotCheckbox').click()
    input3 = browser.find_element_by_id('robotsRule').click()
    time.sleep(1)

    button = browser.find_element_by_tag_name('button').click()
    time.sleep(1)

    # response(browser)

finally:
    resp = browser.switch_to.alert
    resp_text = resp.text
    resp.accept()
    print(resp_text.split()[-1])
    browser.close()
    browser.quit()