import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True) # Does not let browser close automatically
driver = webdriver.Chrome(options = chrome_options)

#driver.get("https://www.spicejet.com/")
driver.get("https://spiceclub.spicejet.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//span[text()='Login']").click() # Click on login Button

driver.find_element(By.XPATH,"//div[@class=' flag-dropdown']").click() # Click on flag dropdown

countryCode = driver.find_elements(By.XPATH,"//ul [@class=' country-list']/li/span[@class='country-name']")
for country in countryCode:
    if country.text == "India":
        country.click()
        break

driver.find_element(By.XPATH, "//input[@class=' form-control']").send_keys("8861141894") # Enter mobile number
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Syncmaster591!") # Enter Password

driver.find_element(By.XPATH,"//div[@class='btn btn-red plr-50']").click() # Click on Login
time.sleep(5)

#WebDriverWait(driver,5).until(expected_conditions.element_to_be_clickable(driver.find_element(By.XPATH,"//button[text()='BOOK NOW']/parent::a/parent::li[@class='nav-item']"))).click()# Click on Book Now
driver.find_element(By.XPATH,"//button[text()='BOOK NOW']/parent::a/parent::li[@class='nav-item']").click()



#### Travel details page. Next tab#####

windows_opened = driver.window_handles # Handling window switch
driver.switch_to.window(windows_opened[1])


driver.find_element(By.XPATH, "//div[@data-testid='round-trip-radio-button']").click()

#Choosing Origin
driver.find_element(By.XPATH, "//div[@data-testid='to-testID-origin']/div/div[2]/input").send_keys("Ben")
driver.find_element(By.XPATH, "//div[text()='Kempegowda International Airport']").click()

#Choosing Destination
driver.find_element(By.XPATH, "//div[@data-testid='to-testID-destination']/div/div[2]/input").send_keys("De")
#time.sleep(2)
driver.find_element(By.XPATH, "//div[contains (text(), 'Dehradun Airport')]").click()

driver.find_element(By.XPATH,"//div[@data-testid='undefined-month-March-2024']/div[3]/div[4]/div[6]").click()

driver.find_element(By.XPATH,"//div[@data-testid='undefined-month-April-2024']/div[3]/div[1]/div[3]").click()

driver.find_element(By.XPATH,"//div[@data-testid='home-page-travellers']").click()

for i in range (1,3):
    driver.find_element(By.XPATH,"//div[@data-testid='Adult-testID-plus-one-cta']").click()

driver.find_element(By.XPATH, "//div[@data-testid='home-page-travellers-done-cta']").click() # Passenger done button

#time.sleep(1)

driver.find_element(By.XPATH,"//div[contains (text(), 'Currency')]").click() # click on currency dropdown

currencies = driver.find_elements(By.XPATH, "//div[@class='css-1dbjc4n']/div/div[@dir='auto']") # List of all currencies

for currency in currencies:
    if currency.text == "USD":
        currency.click()
        break


driver.find_element(By.XPATH,"//div[text()='Family & Friends']").click() # Select Family and friends

driver.find_element(By.XPATH,"//div[@data-testid='home-page-flight-cta']").click() # Click on search





driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n r-zso239']/parent::div[@class='css-1dbjc4n r-1awozwy r-1loqt21 r-18u37iz r-1otgn73']").click() # Click on checkbox


driver.find_element(By.XPATH,"//div[text()='Continue']/parent::div[@class='css-1dbjc4n r-1awozwy r-z2wwpe r-1loqt21 r-18u37iz r-1777fci r-d9fdf6 r-1w50u8q r-ah5dr5 r-1otgn73']").click() # Click on Continue


driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n r-1jkjb']").click()

driver.find_element(By.XPATH, "//div[text()='Log Out']").click() # logout

#driver.close()

