from conftest import BASE_URL

def test_login_page_opens(driver):
    driver.get(BASE_URL + "index.php?page=login")

    email_box = driver.find_element("name", "email")
    password_box = driver.find_element("name", "password")
    login_btn = driver.find_element("css selector", "button[type='submit']")

    assert email_box.is_displayed()
    assert password_box.is_displayed()
    assert login_btn.is_displayed()
    print("Login page opened correctly")


def test_successful_login(driver):
    driver.get(BASE_URL + "index.php?page=login")

    driver.find_element("name", "email").send_keys("customer@chajoy.com")
    driver.find_element("name", "password").send_keys("password123")
    driver.find_element("css selector", "button[type='submit']").click()

    page = driver.page_source
    assert "Logout" in page or "Dashboard" in page or "Profile" in page
    print("Successful login")


def test_login_wrong_password(driver):
    driver.get(BASE_URL + "index.php?page=login")

    driver.find_element("name", "email").send_keys("customer@chajoy.com")
    driver.find_element("name", "password").send_keys("wrongpassword999")
    driver.find_element("css selector", "button[type='submit']").click()

    assert "login" in driver.current_url or "invalid" in driver.page_source.lower()
    print("Wrong password correctly rejected")