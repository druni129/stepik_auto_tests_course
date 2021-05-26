from selenium import webdriver
import time 
import math

def calc(x):return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("answer")
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    x_element.send_keys(y)
    
    def calc(x):return str(math.log(abs(12*math.sin(int(x)))))
    
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']").click()
    option2 = browser.find_element_by_css_selector("[id='robotsRule']").click()
    button = browser.find_element_by_xpath("//button[@type='submit']").click()
    
    
    
    
   

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла