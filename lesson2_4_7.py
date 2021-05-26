#Задание явных ожиданий реализуется с помощью инструментов WebDriverWait и expected_conditions. Улучшим наш тест:

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

#Как вы видите, в этом случае нужно использовать поиск элементов с помощью класса By, который мы рассмотрели ранее. 
#element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае.