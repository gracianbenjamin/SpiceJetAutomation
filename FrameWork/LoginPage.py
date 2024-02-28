import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class LoginPage:

    login_button = (By.XPATH,"//span[text()='Login']") # Login Button Tupple
    flag_dropdown = (By.XPATH, "//div[@class=' flag-dropdown']") # Clicking on Flag dropdown
    countries_options= (By.XPATH, "//ul [@class=' country-list']/li/span[@class='country-name']") # List of country codes
    phone_number = (By.XPATH, "//input[@class=' form-control']") # Phone number for login
    pass_word = (By.XPATH, "//input[@type='password']") # Password for login
    login_button2 = (By.XPATH, "//div[@class='btn btn-red plr-50']") # login button tupple
    booknow_button = (By.XPATH, "//button[text()='BOOK NOW']/parent::a/parent::li[@class='nav-item']")

    def __init__(self,driver):
        self.driver = driver

    def clickLogin1(self):
        return self.driver.find_element(*LoginPage.login_button)

    def clickFlagList(self):
        return self.driver.find_element(*LoginPage.flag_dropdown)

    def getCountriesList(self):
        return self.driver.find_elements(*LoginPage.countries_options)

    def putPhoneNumber(self):
        return self.driver.find_element(*LoginPage.phone_number)

    def putPassWord(self):
        return self.driver.find_element(*LoginPage.pass_word)

    def clickLogin2(self):
        return self.driver.find_element(*LoginPage.login_button2)

    def clickBookNow(self):
        return self.driver.find_element(*LoginPage.booknow_button)




