# получение ответа и автоматический его ввод на степике
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

button = browser.find_element_by_class_name('btn-primary').click()
browser.switch_to.alert.accept()

x = browser.find_element_by_id("input_value").text
y = calc(x)

browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_class_name('btn-primary').click()


time.sleep(10)
browser.quit()