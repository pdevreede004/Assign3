import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#ran locally on my machine

class Test_create_account(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_create_user(self):
        username_login = "instructor"
        username_password = "maverick1a"
        first_name = "John"
        last_name = "smith"
        user = "user1"
        password = "password1a"
        email_address = "pdevreede004@gmail.com"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")

        elem = driver.find_element_by_id("id_username")
        elem.send_keys(username_login)

        elem = driver.find_element_by_id("id_password")
        elem.send_keys(username_password)
        time.sleep(1)


        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/input").click()
        time.sleep(1)

        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[1]/a").click()

        time.sleep(1)

        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(1)

        elem = driver.find_element_by_id("id_password1")
        elem.send_keys(password)
        time.sleep(1)

        elem = driver.find_element_by_id("id_password2")
        elem.send_keys(password)
        time.sleep(1)

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/input[1]").click()
        time.sleep(1)

        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys(first_name)
        time.sleep(1)

        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys(last_name)
        time.sleep(1)

        elem = driver.find_element_by_id("id_email")
        elem.send_keys(email_address)
        time.sleep(1)

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(1)

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[4]/th/a").click()
        time.sleep(1)

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/p/a").click()
        time.sleep(1)

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
        time.sleep(1)

        driver.get("http://127.0.0.1:8000/admin")
        assert "Logged In"
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

