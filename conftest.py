import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://localhost/ChaJoy/"

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    driver.get(BASE_URL)
    yield driver
    driver.quit()


def login_as_customer(driver):
    driver.get(BASE_URL + "index.php?page=login")
    driver.find_element("name", "email").send_keys("customer@chajoy.com")
    driver.find_element("name", "password").send_keys("password123")
    driver.find_element("css selector", "button[type='submit']").click()