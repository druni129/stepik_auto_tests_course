from selenium import webdriver
import time 
import math

def calc(x):return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    z_element = browser.find_element_by_id("answer")
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    z_element.send_keys(y)
    
    #def calc(x):return str(math.log(abs(12*math.sin(int(x)))))
    
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']").click()
    option2 = browser.find_element_by_css_selector("[id='robotsRule']").click()
    button = browser.find_element_by_xpath("//button[@type='submit']").click()
    
    
    
    
   

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

  # x = treasure # 123
  #  y = calc(x) # правильный ответ
   # input.send_keys(treasure) # ???