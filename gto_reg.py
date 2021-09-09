#Задание явных ожиданий с помощью инструментов WebDriverWait и expected_conditions.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#Задать нужные переменные
url = 'http://user.gto.ru/user/register'
url_pass = 'view-source:http://user.gto.ru/user/register?debug'
email = ''
password = 'pass1234'
datatime = '01.01.1940'



#Переходим на сайт ГТО (логин и пароль первички забил в урл)
browser = webdriver.Chrome()
browser.get(url)







#Закрываем браузер через 10 секунд после выполнения
time.sleep(10)
browser.quit()

# не забываем оставить пустую строку в конце файла