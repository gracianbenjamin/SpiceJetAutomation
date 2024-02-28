import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


@pytest.fixture(scope="class")
def browserInvoke(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)  # Does not let browser close automatically
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://spiceclub.spicejet.com/")
    driver.maximize_window()
    request.cls.driver = driver # #To establish connection betweeen Conftest, local "driver" and the EndtoEnd class "driver"
    yield
    #driver.close()
