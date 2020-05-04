import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Test_buy_product(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_buy_product(self):
        first_name = "John"
        last_name = "smith"
        email_address = "pdevreede004@gmail.com"
        address = "1234 Main St"
        postal_code = "68123"
        city = "Omaha"
        card_number = "4111 1111 1111 1111"
        cvv = "123"
        expiration_date = "04/20"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://pcaz.pythonanywhere.com/")

        elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/a[2]").click()

        # new page
        elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()

        # new page
        elem = driver.find_element_by_xpath("/html/body/div[3]/p/a[2]").click()

        # new page
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys(first_name)

        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys(last_name)

        elem = driver.find_element_by_id("id_email")
        elem.send_keys(email_address)

        elem = driver.find_element_by_id("id_address")
        elem.send_keys(address)

        elem = driver.find_element_by_id("id_postal_code")
        elem.send_keys(postal_code)

        elem = driver.find_element_by_id("id_city")
        elem.send_keys(city)

        elem = driver.find_element_by_xpath("/html/body/div[3]/form/p[7]/input").click()

        #new page

        assert "bought a product"








        driver.get("http://pcaz.pythonanywhere.com/")
        assert "Logged In"

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
