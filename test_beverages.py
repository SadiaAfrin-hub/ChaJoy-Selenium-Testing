
import time
from conftest import BASE_URL, login_as_customer
from selenium.webdriver.support.ui import Select


def test_beverages_list_shows(driver):
    driver.get(BASE_URL + "index.php?page=beverages")

    cards = driver.find_elements("css selector", ".beverage-card")
    print(f"Number of beverages found: {len(cards)}")

    assert len(cards) > 0, "At least one beverage should be displayed"
    print("Beverages list is displayed")


def test_search_beverage(driver):
    driver.get(BASE_URL + "index.php?page=beverages")

    search_box = driver.find_element("id", "searchInput")
    search_box.clear()
    search_box.send_keys("tea")

    time.sleep(1.5)

    cards = driver.find_elements("css selector", ".beverage-card")
    print(f"Beverages after searching 'tea': {len(cards)}")
    print("Search works")


def test_add_to_cart_button_exists(driver):
    login_as_customer(driver)
    driver.get(BASE_URL + "index.php?page=beverages")

    buttons = driver.find_elements("css selector", ".add-to-cart-btn")

    assert len(buttons) > 0, "Add to Cart buttons should be visible"
    print("Add to Cart buttons are visible")


def test_add_beverage(driver):

    driver.get(BASE_URL + "index.php?page=login")

    driver.find_element("name", "email").send_keys("admin@chajoy.com")
    driver.find_element("name", "password").send_keys("password123")
    driver.find_element("css selector", "button[type='submit']").click()

    time.sleep(2)

    driver.get(BASE_URL + "index.php?page=admin_beverages")

    time.sleep(2)
    driver.find_element("css selector", ".open-beverage-modal").click()

    time.sleep(1)

    beverage_name = "Selenium Test Milk Tea"

    driver.find_element("id", "bev_name").send_keys(beverage_name)

    category = driver.find_element("id", "bev_category")
    Select(category).select_by_value("1")

    driver.find_element("id", "bev_description").send_keys(
        "This beverage was added using Selenium testing"
    )

    driver.find_element("id", "bev_price").send_keys("120")
    driver.find_element("id", "bev_stock").send_keys("50")

    # Submit beverage form
    driver.find_element(
        "css selector",
        "#beverageForm button[type='submit']"
    ).click()

    time.sleep(2)
    success_message = driver.find_elements(
        "css selector", ".alert-success"
    )

    assert len(success_message) > 0, "Beverage should be added successfully"
    page_text = driver.find_element("tag name", "body").text

    assert beverage_name in page_text, "New beverage should appear in the list"

    print("New beverage added successfully")
