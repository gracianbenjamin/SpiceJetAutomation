from selenium.webdriver.common.by import By


class FlightDetailsPage:
    check_box = (By.XPATH,"//div[@class='css-1dbjc4n r-zso239']/parent::div[@class='css-1dbjc4n r-1awozwy r-1loqt21 r-18u37iz r-1otgn73']")
    continue_button = (By.XPATH,"//div[text()='Continue']/parent::div[@class='css-1dbjc4n r-1awozwy r-z2wwpe r-1loqt21 r-18u37iz r-1777fci r-d9fdf6 r-1w50u8q r-ah5dr5 r-1otgn73']")
    profile_dropdown = (By.XPATH, "//div[@class='css-1dbjc4n r-1jkjb']")
    logout_button = (By.XPATH,"//div[text()='Log Out']")

    def __init__(self,driver):
        self.driver=driver

    def clickCheckBox(self):
        return self.driver.find_element(*FlightDetailsPage.check_box)

    def continueClick(self):
        return self.driver.find_element(*FlightDetailsPage.continue_button)

    def profileDropdown(self):
        return self.driver.find_element(*FlightDetailsPage.profile_dropdown)

    def logout(self):
        return self.driver.find_element(*FlightDetailsPage.logout_button)