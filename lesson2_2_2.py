from selenium import webdriver
import time 
import math
#from selenium.webdriver.support.ui import Select

def calc():
     x = str(int(y) + int(z))
     return x

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome('chromedriver')
    browser.get(link)
    
    y = browser.find_element_by_id('num1').text
    z = browser.find_element_by_id('num2').text
    x = calc()
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(x)
    time.sleep(1)

    button = browser.find_element_by_tag_name('button').click()
    time.sleep(1)
    
    
    
    
   

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла