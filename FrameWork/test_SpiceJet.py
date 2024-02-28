import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from FrameWork.BookingPage import BookingPage
from FrameWork.FlightDetailsPage import FlightDetailsPage
from FrameWork.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass


class TestSpiceJet(BaseClass):
    def test_e2e(self, browserInvoke):

        self.driver.implicitly_wait(5)
        #Login Page actions####
        login = LoginPage(self.driver) # Creating object from LoginPage class

        login.clickLogin1().click() # Click on login Button
        #self.driver.find_element(By.XPATH, "//span[text()='Login']").click()  # Click on login Button

        login.clickFlagList().click() # Click on flag dropdown
        #self.driver.find_element(By.XPATH, "//div[@class=' flag-dropdown']").click()  # Click on flag dropdown


        countryCode = login.getCountriesList()
        #countryCode = self.driver.find_elements(By.XPATH, "//ul [@class=' country-list']/li/span[@class='country-name']")
        for country in countryCode:
            if country.text == "India":
                country.click()
                break

        login.putPhoneNumber().send_keys("8861141894")
        #self.driver.find_element(By.XPATH, "//input[@class=' form-control']").send_keys("8861141894")  # Enter mobile number

        login.putPassWord().send_keys("Syncmaster591!")
        #self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Syncmaster591!")  # Enter Password

        login.clickLogin2().click()
        #self.driver.find_element(By.XPATH, "//div[@class='btn btn-red plr-50']").click()  # Click on Login
        time.sleep(5)

        login.clickBookNow().click()
        #self.driver.find_element(By.XPATH, "//button[text()='BOOK NOW']/parent::a/parent::li[@class='nav-item']").click()

        #### Booking Details page. Next tab#####

        bookingDetailsPage = BookingPage(self.driver)

        windows_opened = self.driver.window_handles  # Handling window switch
        self.driver.switch_to.window(windows_opened[1])

        time.sleep(2)
        bookingDetailsPage.selectTrip().click()
        #self.driver.find_element(By.XPATH, "//div[@data-testid='round-trip-radio-button']").click()

        ######Choosing Origin######
        bookingDetailsPage.originInput().send_keys("ben")
        #self.driver.find_element(By.XPATH, "//div[@data-testid='to-testID-origin']/div/div[2]/input").send_keys("Ben")

        bookingDetailsPage.originSelect().click()
        #self.driver.find_element(By.XPATH, "//div[text()='Kempegowda International Airport']").click()

        #####Choosing Destination###

        bookingDetailsPage.destinationInput().send_keys("che")
        #self.driver.find_element(By.XPATH, "//div[@data-testid='to-testID-destination']/div/div[2]/input").send_keys("De")

        time.sleep(2)

        bookingDetailsPage.destinationSelect().click()
        #self.driver.find_element(By.XPATH, "//div[contains (text(), 'Dehradun Airport')]").click()

        bookingDetailsPage.startDate().click()
        #self.driver.find_element(By.XPATH, "//div[@data-testid='undefined-month-March-2024']/div[3]/div[4]/div[6]").click()

        time.sleep(2)
        bookingDetailsPage.returnDate().click()
        #self.driver.find_element(By.XPATH, "//div[@data-testid='undefined-month-April-2024']/div[3]/div[1]/div[3]").click()

        bookingDetailsPage.numOfMembers().click()
        #self.driver.find_element(By.XPATH, "//div[@data-testid='home-page-travellers']").click()

        for i in range(1, 3):
            bookingDetailsPage.plusButton().click()
            #self.driver.find_element(By.XPATH, "//div[@data-testid='Adult-testID-plus-one-cta']").click()

        bookingDetailsPage.membersConfirm().click()
        #self.driver.find_element(By.XPATH,"//div[@data-testid='home-page-travellers-done-cta']").click()  # Passenger done button

        # time.sleep(1)

        bookingDetailsPage.currencyDropDown().click()
        #self.driver.find_element(By.XPATH, "//div[contains (text(), 'Currency')]").click()  # click on currency dropdown

        currencies = bookingDetailsPage.currencyList()
        #currencies = self.driver.find_elements(By.XPATH,"//div[@class='css-1dbjc4n']/div/div[@dir='auto']")  # List of all currencies

        for currency in currencies:
            if currency.text == "USD":
                currency.click()
                break

        bookingDetailsPage.memberType().click()
        #self.driver.find_element(By.XPATH, "//div[text()='Family & Friends']").click()  # Select Family and friends

        bookingDetailsPage.searchButton().click()
        #self.driver.find_element(By.XPATH, "//div[@data-testid='home-page-flight-cta']").click()  # Click on search

        ####FlightDetailsPage####

        flightDetailsPage = FlightDetailsPage(self.driver)

        flightDetailsPage.clickCheckBox().click()
        #self.driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n r-zso239']/parent::div[@class='css-1dbjc4n r-1awozwy r-1loqt21 r-18u37iz r-1otgn73']").click()  # Click on checkbox

        flightDetailsPage.continueClick().click()
        #self.driver.find_element(By.XPATH,"//div[text()='Continue']/parent::div[@class='css-1dbjc4n r-1awozwy r-z2wwpe r-1loqt21 r-18u37iz r-1777fci r-d9fdf6 r-1w50u8q r-ah5dr5 r-1otgn73']").click()  # Click on Continue

        time.sleep(3)
        flightDetailsPage.profileDropdown().click()
        #self.driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-1jkjb']").click()  # click on Profile

        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.driver.find_element(By.XPATH, "//div[text()='Log Out']"))).click()  # logout
        #time.sleep(2)
        #self.driver.find_element(By.XPATH, "//div[text()='Log Out']").click()
        # driver.close()

