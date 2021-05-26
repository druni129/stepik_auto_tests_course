from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname("C:\TEST\lesson2_2_8.py"))   # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    for elem_name in ["firstname", "lastname", "email"]:
        browser.find_element_by_name(elem_name).send_keys(elem_name)

    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()