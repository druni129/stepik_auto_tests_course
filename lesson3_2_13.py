import unittest
from selenium import webdriver

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_tag_name(":required.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_tag_name(":required.form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_tag_name(":required.form-control.third")
        input3.send_keys("mail")
        button = browser.find_element_by_xpath("//button[@type='submit']")
        button.click()
        
    def test_abs2(self):
        self.assertEqual
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_tag_name(":required.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_tag_name(":required.form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_tag_name(":required.form-control.third")
        input3.send_keys("mail")
        button = browser.find_element_by_xpath("//button[@type='submit']")
        button.click()
        
if __name__ == "__main__":
    unittest.main()