#Задание явных ожиданий с помощью инструментов WebDriverWait и expected_conditions.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#Задать нужные переменные
url_1 = "https://admin.gto.ru/"
url_2 = 'https://testuser:miToorohY2eiwah@admin.gto.ru'
email = 'admin@yandex.ru' #'test2@srv-zimbra-01.local.ru'
password = 'pass1234'
datatime = '29.07.2021'
user1 = '21-27-0000001'
user2 = '21-27-0000002' 
user3 = '21-27-0000003' # нужный
user4 = '21-27-0000004'
user5 = '21-27-0000005'
result1 = '0'
result2 = '6'
result3 = '0'
result4 = '8'
result5 = '1'

#Переходим на сайт ГТО (логин и пароль первички забил в урл)
browser = webdriver.Chrome()
browser.get(url_1)

button = browser.find_element_by_id("details-button")
button.click()
button = browser.find_element_by_id("proceed-link")
button.click()

browser.get(url_2)

#Говорим ожидать элемент в течении 5 секунд каждые 0.5 секунд
#browser.implicitly_wait(5)

#Авторизовываемся под админом
browser.find_element_by_name('email').send_keys(email) 
browser.find_element_by_name('password').send_keys(password)
browser.find_element_by_class_name('btn-block').click()

#Ведем самый безопасный код в мире
browser.find_element_by_name('code').send_keys('1111') 
browser.find_element_by_class_name('btn-success').click()

#Переходим на страницу создания протокола чтобы создать первое испытание
browser.get('http://admin.gto.ru/admin/protocols/add')

#Указываем ЦТ
browser.find_element_by_css_selector("div #general > .form-group:nth-child(2) >.col-lg-6 >.selectize-control div").click()
Centr = browser.find_element_by_xpath("//*[contains(text(), 'Тест ICL')]")
Centr.click()
#Указываем испытание для первого протокола
browser.find_element_by_css_selector("div #general > .form-group:nth-child(3) >.col-lg-6 >.selectize-control div").click()
Trial = browser.find_element_by_xpath("//*[contains(text(), 'Смешанное передвижение на 2 км')]")
Trial.click()
#Указываем дату для первого протокола
data = browser.find_element_by_name("item[start]")
data.click()
data.send_keys(datatime)
#Нажимаем "Применить" и создаем первый протокол 
button = browser.find_element_by_name("apply")
button.click()

#Проверяем что протокол успешно создан
#message = browser.find_element_by_xpath("//*[contains(text(), 'успешно создан')]")
#assert "successful" in message

#Заполняем юзеров для первого испытания
first_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(1) > td  > div > input")
first_user.send_keys(user1)

second_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(2) > td > div > input")
second_user.send_keys(user2)

third_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(3) > td > div > input")
third_user.send_keys(user3)

fourth_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(4) > td > div > input")
fourth_user.send_keys(user4)

fifth_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(5) > td > div > input")
fifth_user.send_keys(user5)

#Заполняем результаты юзерам для первого испытания
first_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(1) > td:nth-child(4) > input")
first_result.send_keys(result1)

second_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(2) > td:nth-child(4) > input")
second_result.send_keys(result1)

third_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(3) > td:nth-child(4) > input")
third_result.send_keys(result1)

fourth_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(4) > td:nth-child(4) > input")
fourth_result.send_keys(result1)

fifth_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(5) > td:nth-child(4) > input")
fifth_result.send_keys(result1)

#Ждем 3 секунды чтобы успело всё записаться
time.sleep(5)

#Сохраняем протокол с юзерами
button_save = browser.find_element_by_css_selector("#footer-edit >button:nth-child(2)")
button_save.click()


#Переходим на страницу создания протокола чтобы создать ВТОРОЕ испытание
browser.get('http://admin.gto.ru/admin/protocols/add')

#Указываем ЦТ
browser.find_element_by_css_selector("div #general > .form-group:nth-child(2) >.col-lg-6 >.selectize-control div").click()
Centr = browser.find_element_by_xpath("//*[contains(text(), 'Тест ICL')]")
Centr.click()
#Указываем испытание для ВТОРОГО протокола
browser.find_element_by_css_selector("div #general > .form-group:nth-child(3) >.col-lg-6 >.selectize-control div").click()
Trial = browser.find_element_by_xpath("//*[contains(text(), 'Сгибание и разгибание рук в упоре о сиденье стула')]")
Trial.click()
#Указываем дату для ВТОРОЙ протокола
data = browser.find_element_by_name("item[start]")
data.click()
data.send_keys(datatime)
#Нажимаем "Применить" и создаем ВТОРОЙ протокол 
button = browser.find_element_by_name("apply")
button.click()

#Заполняем юзеров для ВТОРОГО испытания
first_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(1) > td  > div > input")
first_user.send_keys(user1)

second_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(2) > td > div > input")
second_user.send_keys(user2)

third_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(3) > td > div > input")
third_user.send_keys(user3)

fourth_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(4) > td > div > input")
fourth_user.send_keys(user4)

fifth_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(5) > td > div > input")
fifth_user.send_keys(user5)

#Заполняем результаты юзерам для ВТОРОГО испытания
first_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(1) > td:nth-child(4) > input")
first_result.send_keys(result2)

second_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(2) > td:nth-child(4) > input")
second_result.send_keys(result2)

third_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(3) > td:nth-child(4) > input")
third_result.send_keys(result2)

fourth_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(4) > td:nth-child(4) > input")
fourth_result.send_keys(result2)

fifth_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(5) > td:nth-child(4) > input")
fifth_result.send_keys(result2)

#Ждем 3 секунды чтобы успело всё записаться
time.sleep(5)

#Сохраняем протокол с юзерами
button_save = browser.find_element_by_css_selector("#footer-edit >button:nth-child(2)")
button_save.click()




#Переходим на страницу создания протокола чтобы создать ТРЕТЬЕ испытание
browser.get('http://admin.gto.ru/admin/protocols/add')

#Указываем ЦТ
browser.find_element_by_css_selector("div #general > .form-group:nth-child(2) >.col-lg-6 >.selectize-control div").click()
Centr = browser.find_element_by_xpath("//*[contains(text(), 'Тест ICL')]")
Centr.click()
#Указываем испытание для ТРЕТЬЕГО протокола
browser.find_element_by_css_selector("div #general > .form-group:nth-child(3) >.col-lg-6 >.selectize-control div").click()
Trial = browser.find_element_by_xpath("//*[contains(text(), 'Наклон вперед из положения стоя с прямыми ногами на гимнастической скамье')]")
Trial.click()
#Указываем дату для ТРЕТЬЕГО протокола
data = browser.find_element_by_name("item[start]")
data.click()
data.send_keys(datatime)
#Нажимаем "Применить" и создаем ТРЕТИЙ протокол 
button = browser.find_element_by_name("apply")
button.click()

#Заполняем юзеров для ТРЕТИГО испытания
first_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(1) > td  > div > input")
first_user.send_keys(user1)

second_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(2) > td > div > input")
second_user.send_keys(user2)

third_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(3) > td > div > input")
third_user.send_keys(user3)

fourth_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(4) > td > div > input")
fourth_user.send_keys(user4)

fifth_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(5) > td > div > input")
fifth_user.send_keys(user5)

#Заполняем результаты юзерам для ТРЕТЕГО испытания
first_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(1) > td:nth-child(4) > input")
first_result.send_keys(result3)

second_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(2) > td:nth-child(4) > input")
second_result.send_keys(result3)

third_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(3) > td:nth-child(4) > input")
third_result.send_keys(result3)

fourth_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(4) > td:nth-child(4) > input")
fourth_result.send_keys(result3)

fifth_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(5) > td:nth-child(4) > input")
fifth_result.send_keys(result3)

#Ждем 3 секунды чтобы успело всё записаться
time.sleep(5)

#Сохраняем протокол с юзерами
button_save = browser.find_element_by_css_selector("#footer-edit >button:nth-child(2)")
button_save.click()



#Переходим на страницу создания протокола чтобы создать ЧЕТВЕРТОЕ испытание
browser.get('http://admin.gto.ru/admin/protocols/add')

#Указываем ЦТ
browser.find_element_by_css_selector("div #general > .form-group:nth-child(2) >.col-lg-6 >.selectize-control div").click()
Centr = browser.find_element_by_xpath("//*[contains(text(), 'Тест ICL')]")
Centr.click()
#Указываем испытание для ЧЕТВЕРТОГО протокола
browser.find_element_by_css_selector("div #general > .form-group:nth-child(3) >.col-lg-6 >.selectize-control div").click()
Trial = browser.find_element_by_xpath("//*[contains(text(), 'Поднимание туловища из положения лежа на спине')]")
Trial.click()
#Указываем дату для ЧЕТВЕРТОГО протокола
data = browser.find_element_by_name("item[start]")
data.click()
data.send_keys(datatime)
#Нажимаем "Применить" и создаем ЧЕТВЕРТОЕ протокол 
button = browser.find_element_by_name("apply")
button.click()

#Заполняем юзеров для ЧЕТВЕРТОГО испытания
first_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(1) > td  > div > input")
first_user.send_keys(user1)

second_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(2) > td > div > input")
second_user.send_keys(user2)

third_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(3) > td > div > input")
third_user.send_keys(user3)

fourth_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(4) > td > div > input")
fourth_user.send_keys(user4)

fifth_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(5) > td > div > input")
fifth_user.send_keys(user5)

#Заполняем результаты юзерам для ЧЕТВЕРТОГО испытания
first_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(1) > td:nth-child(4) > input")
first_result.send_keys(result4)

second_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(2) > td:nth-child(4) > input")
second_result.send_keys(result4)

third_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(3) > td:nth-child(4) > input")
third_result.send_keys(result4)

fourth_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(4) > td:nth-child(4) > input")
fourth_result.send_keys(result4)

fifth_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(5) > td:nth-child(4) > input")
fifth_result.send_keys(result4)

#Ждем 3 секунды чтобы успело всё записаться
time.sleep(5)

#Сохраняем протокол с юзерами
button_save = browser.find_element_by_css_selector("#footer-edit >button:nth-child(2)")
button_save.click()





#Переходим на страницу создания протокола чтобы создать ПЯТОЕ испытание
browser.get('http://admin.gto.ru/admin/protocols/add')

#Указываем ЦТ
browser.find_element_by_css_selector("div #general > .form-group:nth-child(2) >.col-lg-6 >.selectize-control div").click()
Centr = browser.find_element_by_xpath("//*[contains(text(), 'Тест ICL')]")
Centr.click()
#Указываем испытание для ПЯТОГО протокола
browser.find_element_by_css_selector("div #general > .form-group:nth-child(3) >.col-lg-6 >.selectize-control div").click()
Trial = browser.find_element_by_xpath("//*[contains(text(), 'Плавание 25 м')]")
Trial.click()
#Указываем дату для ПЯТОГО протокола
data = browser.find_element_by_name("item[start]")
data.click()
data.send_keys(datatime)
#Нажимаем "Применить" и создаем ПЯТЫЙ протокол 
button = browser.find_element_by_name("apply")
button.click()

#Заполняем юзеров для ПЯТОГО испытания
first_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(1) > td  > div > input")
first_user.send_keys(user1)

second_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(2) > td > div > input")
second_user.send_keys(user2)

third_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(3) > td > div > input")
third_user.send_keys(user3)

fourth_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(4) > td > div > input")
fourth_user.send_keys(user4)

fifth_user = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(5) > td > div > input")
fifth_user.send_keys(user5)

#Заполняем результаты юзерам для ПЯТОГО испытания
first_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(1) > td:nth-child(4) > input")
first_result.send_keys(result5)

second_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(2) > td:nth-child(4) > input")
second_result.send_keys(result5)

third_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(3) > td:nth-child(4) > input")
third_result.send_keys(result5)

fourth_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(4) > td:nth-child(4) > input")
fourth_result.send_keys(result5)

fifth_result = browser.find_element_by_css_selector("#table-results-items > tbody > tr:nth-child(5) > td:nth-child(4) > input")
fifth_result.send_keys(result5)

#Ждем 3 секунды чтобы успело всё записаться
time.sleep(5)

#Сохраняем протокол с юзерами
button_save = browser.find_element_by_css_selector("#footer-edit >button:nth-child(2)")
button_save.click()


#Закрываем браузер через 10 секунд после выполнения
time.sleep(10)
browser.quit()

# не забываем оставить пустую строку в конце файла