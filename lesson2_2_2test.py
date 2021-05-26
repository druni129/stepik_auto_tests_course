from selenium import webdriver
import time

def calc():
     x = str(int(y) + int(z))
     return x

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_tag_name('button').click()
    time.sleep(1)
    
finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла