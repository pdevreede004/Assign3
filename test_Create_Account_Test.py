import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test_create_account(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_create_account(self):
        username = "testuser2"
        first_name = "John"
        pwd = "password"
        email_address = "pdevreede@unomaha.edu"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://pcaz.pythonanywhere.com/")

        elem = driver.find_element_by_xpath("/html/body/div[2]/span/a").click()

        elem = driver.find_element_by_xpath("/html/body/div[3]/p[2]/a").click()

        elem = driver.find_element_by_id("id_username")
        elem.send_keys(username)

        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys(first_name)

        elem = driver.find_element_by_id("id_email")
        elem.send_keys(email_address)

        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)

        elem = driver.find_element_by_id("id_password2")
        elem.send_keys(pwd)

        elem = driver.find_element_by_xpath("/html/body/div[3]/form/p[6]/input").click()


        driver.get("http://pcaz.pythonanywhere.com/")
        assert "Logged In"
        time.sleep(5)




    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
