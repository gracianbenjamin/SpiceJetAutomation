from selenium.webdriver.common.by import By


class BookingPage:
    round_trip = (By.XPATH,"//div[@data-testid='round-trip-radio-button']")
    input_origin = (By.XPATH,"//div[@data-testid='to-testID-origin']/div/div[2]/input")
    select_origin = (By.XPATH, "//div[text()='Kempegowda International Airport']")
    input_dest = (By.XPATH, "//div[@data-testid='to-testID-destination']/div/div[2]/input")
    select_dest = (By.XPATH,"//div[text()='Chennai International Airport']")
    select_start_date = (By.XPATH,"//div[@data-testid='undefined-month-March-2024']/div[3]/div[4]/div[6]")
    select_return_date = (By.XPATH,"//div[@data-testid='undefined-month-April-2024']/div[3]/div[1]/div[3]")
    select_members = (By.XPATH,"//div[@data-testid='home-page-travellers']")
    members_plus_button = (By.XPATH,"//div[@data-testid='Adult-testID-plus-one-cta']")
    members_done_button = (By.XPATH,"//div[@data-testid='home-page-travellers-done-cta']")
    currency_dropdown = (By.XPATH,"//div[contains (text(), 'Currency')]")
    currency_list = (By.XPATH,"//div[@class='css-1dbjc4n']/div/div[@dir='auto']")
    select_member_type = (By.XPATH,"//div[text()='Family & Friends']")
    search_button = (By.XPATH, "//div[@data-testid='home-page-flight-cta']")


    def __init__(self, driver):
        self.driver = driver

    def selectTrip(self):
        return self.driver.find_element(*BookingPage.round_trip)

    def originInput(self):
        return self.driver.find_element(*BookingPage.input_origin)

    def originSelect(self):
        return self.driver.find_element(*BookingPage.select_origin)

    def destinationInput(self):
        return self.driver.find_element(*BookingPage.input_dest)

    def destinationSelect(self):
        return self.driver.find_element(*BookingPage.select_dest)

    def startDate(self):
        return self.driver.find_element(*BookingPage.select_start_date)

    def returnDate(self):
        return self.driver.find_element(*BookingPage.select_return_date)

    def numOfMembers(self):
        return self.driver.find_element(*BookingPage.select_members)

    def plusButton(self):
        return self.driver.find_element(*BookingPage.members_plus_button)

    def membersConfirm(self):
        return self.driver.find_element(*BookingPage.members_done_button)

    def currencyDropDown(self):
        return self.driver.find_element(*BookingPage.currency_dropdown)

    def currencyList(self):
        return self.driver.find_elements(*BookingPage.currency_list)

    def memberType(self):
        return self.driver.find_element(*BookingPage.select_member_type)

    def searchButton(self):
        return self.driver.find_element(*BookingPage.search_button)



