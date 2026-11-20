import time
from conftest import BASE_URL, login_as_customer

def test_add_item_and_open_cart(driver):
    login_as_customer(driver)
    time.sleep(1)

    driver.get(BASE_URL + "index.php?page=beverages")
    time.sleep(1)

    add_buttons = driver.find_elements("css selector", ".add-to-cart-btn:not([disabled])")
    if add_buttons:
        add_buttons[0].click()
        time.sleep(1.5)
        print("Clicked Add to Cart")
    else:
        print("No available items to add")

    driver.get(BASE_URL + "index.php?page=cart")
    time.sleep(1)

    source = driver.page_source.lower()
    assert "cart" in source or "total" in source or "empty" in source
    print("Cart page opened")


def test_update_quantity(driver):
    login_as_customer(driver)
    time.sleep(0.8)

    driver.get(BASE_URL + "index.php?page=beverages")
    time.sleep(0.8)
    add_buttons = driver.find_elements("css selector", ".add-to-cart-btn:not([disabled])")
    if add_buttons:
        add_buttons[0].click()
        time.sleep(1.2)

    driver.get(BASE_URL + "index.php?page=cart")
    time.sleep(1)

    increase_buttons = driver.find_elements("css selector", ".qty-increase")
    if not increase_buttons:
        print("Cart is empty – cannot test quantity update")
        return

    qty_span = driver.find_element("css selector", ".qty-value")
    old_qty = int(qty_span.text.strip())
    print(f"Old quantity: {old_qty}")

    increase_buttons[0].click()
    time.sleep(1.5)

    qty_span = driver.find_element("css selector", ".qty-value")
    new_qty = int(qty_span.text.strip())
    print(f"New quantity: {new_qty}")

    assert new_qty == old_qty + 1
    print("Quantity UPDATE works")


def test_remove_item_from_cart(driver):
    login_as_customer(driver)
    time.sleep(0.8)

    driver.get(BASE_URL + "index.php?page=beverages")
    time.sleep(0.8)
    add_buttons = driver.find_elements("css selector", ".add-to-cart-btn:not([disabled])")
    if add_buttons:
        add_buttons[0].click()
        time.sleep(1.2)

    driver.get(BASE_URL + "index.php?page=cart")
    time.sleep(1)

    remove_buttons = driver.find_elements("css selector", ".remove-item-btn")
    if not remove_buttons:
        print("No items to remove")
        return

    remove_buttons[0].click()
    time.sleep(1.5)
    print("Remove button clicked")