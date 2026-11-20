import time
from conftest import BASE_URL, login_as_customer

def test_profile_page_opens(driver):
    login_as_customer(driver)
    driver.get(BASE_URL + "index.php?page=profile")

    assert driver.find_element("name", "full_name").is_displayed()
    assert driver.find_element("name", "phone").is_displayed()
    assert driver.find_element("name", "address").is_displayed()
    assert driver.find_element("css selector", "button[type='submit']").is_displayed()
    print("Profile page opened")


def test_update_profile(driver):
    login_as_customer(driver)
    driver.get(BASE_URL + "index.php?page=profile")
    time.sleep(0.8)

    name_field = driver.find_element("name", "full_name")
    phone_field = driver.find_element("name", "phone")
    address_field = driver.find_element("name", "address")

    original_name = name_field.get_attribute("value")
    print(f"Original name: {original_name}")

    name_field.clear()
    name_field.send_keys("Test Customer Selenium")

    phone_field.clear()
    phone_field.send_keys("01712345678")

    address_field.clear()
    address_field.send_keys("Selenium Test Address, Dhaka")

    driver.find_element("css selector", "button[type='submit']").click()
    time.sleep(1.5)

    driver.get(BASE_URL + "index.php?page=profile")
    time.sleep(0.8)

    saved_name = driver.find_element("name", "full_name").get_attribute("value")
    saved_phone = driver.find_element("name", "phone").get_attribute("value")
    saved_address = driver.find_element("name", "address").get_attribute("value")

    assert saved_name == "Test Customer Selenium"
    assert saved_phone == "01712345678"
    assert "Selenium Test Address" in saved_address
    print("Profile UPDATE successful")

    name_field = driver.find_element("name", "full_name")
    name_field.clear()
    name_field.send_keys(original_name)
    driver.find_element("css selector", "button[type='submit']").click()
    time.sleep(1)
    print("Original name restored")