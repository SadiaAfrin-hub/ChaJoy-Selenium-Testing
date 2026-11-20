# ChaJoy Selenium Test Automation

## 1. Project Overview

This repository contains automated browser test scripts for **ChaJoy – Online Beverage Ordering System**. The test suite is developed using Python, Selenium WebDriver, and pytest to exercise selected user-facing and administrative workflows through a web browser.

The repository is intended to support functional testing of the ChaJoy web application in a local development or test environment.

## 2. Objectives

The primary objectives of this project are to:

- Verify that selected application pages and interface elements load as expected.
- Test customer authentication with valid and invalid credentials.
- Examine beverage listing and search interactions.
- Exercise selected shopping-cart operations.
- Verify access to customer profile fields and profile updates.
- Exercise the administrative workflow for adding a beverage.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Test scripting language |
| Selenium WebDriver | Browser automation |
| pytest | Test discovery, execution, and fixtures |
| webdriver-manager | ChromeDriver installation and management |
| Google Chrome | Browser used for test execution |

## 4. Repository Structure

```text
ChaJoy-Selenium-Testing/
├── conftest.py
├── browser_test.py
├── test_login.py
├── test_beverages.py
├── test_cart.py
├── test_profile.py
├── requirements.txt
├── .gitignore
└── README.md
```

### File Descriptions

| File | Description |
|---|---|
| `conftest.py` | Defines the application base URL, the Selenium WebDriver fixture, and a helper function for customer login. |
| `browser_test.py` | Provides a standalone browser-launch demonstration that opens Google and prints the page title. |
| `test_login.py` | Contains tests for the login page, successful customer login, and rejection of an incorrect password. |
| `test_beverages.py` | Contains tests for beverage-list display, the search interaction, Add to Cart button visibility, and adding a beverage through the admin interface. |
| `test_cart.py` | Contains tests that open the cart, attempt to add an available beverage, update an item's quantity, and click the remove-item control. |
| `test_profile.py` | Contains tests for profile-page fields and updating customer profile information. |
| `requirements.txt` | Lists the Python packages required by the test suite. |
| `.gitignore` | Excludes virtual environments, cache files, and local development files from version control. |

## 5. Test Coverage

The current test scripts cover the following scenarios:

| Test Module | Test Scenario |
|---|---|
| `test_login.py` | Verify that the login form fields and submit button are displayed. |
| `test_login.py` | Verify customer login using the configured test credentials. |
| `test_login.py` | Verify that an incorrect password does not result in an authenticated page. |
| `test_beverages.py` | Verify that at least one beverage card is displayed. |
| `test_beverages.py` | Enter a search term in the beverage search field and inspect the resulting beverage cards. |
| `test_beverages.py` | Verify that Add to Cart buttons are present after customer login. |
| `test_beverages.py` | Log in as an administrator and submit a new beverage through the administration interface. |
| `test_cart.py` | Attempt to add an available beverage and open the cart page. |
| `test_cart.py` | Increase the quantity of a cart item and verify the displayed quantity change. |
| `test_cart.py` | Click the remove-item control for an item in the cart. |
| `test_profile.py` | Verify that the customer profile fields and submit button are displayed. |
| `test_profile.py` | Update customer profile information, verify the saved values, and restore the original name. |

**Scope note:** The test cases represent the checks currently implemented in the repository. Some scenarios are interaction-oriented rather than complete end-to-end assertions. For example, the search test does not assert specific search results, and the remove-item test does not verify the final cart contents.

## 6. Prerequisites

Before running the test suite, ensure that the following requirements are met:

1. Python is installed and available from the command line.
2. Google Chrome is installed.
3. The ChaJoy web application is configured and accessible on the local machine.
4. The application's database is running and contains the required test accounts and beverage data.
5. The application is available at the base URL configured in `conftest.py`.

The current base URL is:

```python
BASE_URL = "http://localhost/ChaJoy/"
```

If the application is hosted at a different local address or path, update `BASE_URL` in `conftest.py` before executing the tests.

For an XAMPP-based setup, start Apache and MySQL before running the test suite.

## 7. Installation and Configuration

### 7.1 Clone the Repository

Replace `YOUR-USERNAME` with the relevant GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/ChaJoy-Selenium-Testing.git
```

### 7.2 Navigate to the Project Directory

```bash
cd ChaJoy-Selenium-Testing
```

### 7.3 Create a Virtual Environment

```bash
python -m venv venv
```

### 7.4 Activate the Virtual Environment

**Windows PowerShell or Command Prompt:**

```bash
venv\Scripts\activate
```

### 7.5 Install the Dependencies

```bash
python -m pip install -r requirements.txt
```

The project uses `webdriver-manager` to manage the ChromeDriver installation required by Selenium.

## 8. Test Execution

Run all pytest test cases:

```bash
python -m pytest -v
```

Run a specific test module:

```bash
python -m pytest test_login.py -v
```

Run tests whose names match a keyword:

```bash
python -m pytest -v -k login
```

Run the standalone browser demonstration:

```bash
python browser_test.py
```

The pytest tests use the WebDriver fixture defined in `conftest.py`. The fixture launches Chrome, opens the configured application URL, and closes the browser after the test completes.

## 9. Test Accounts and Test Data

The current test configuration uses the following sample account credentials:

| Account Role | Email Address | Password |
|---|---|---|
| Customer | `customer@chajoy.com` | `password123` |
| Administrator | `admin@chajoy.com` | `password123` |

These accounts must be present in the local ChaJoy database for the corresponding tests to run successfully. The credentials are configuration examples for a local test environment; they must not be reused as production credentials.

The beverage-addition test creates a beverage named `Selenium Test Milk Tea`. Repeated executions may create additional records unless the application or test database is reset.

## 10. Execution Considerations

- Confirm that the ChaJoy application is accessible before starting the tests.
- Ensure that the local database contains the configured test accounts.
- Ensure that at least one beverage is available and in stock for cart-related scenarios.
- Run the tests against a dedicated test database rather than a production database.
- The profile-update test changes the customer's name, phone number, and address. The current script restores the original name but does not restore the original phone number or address.
- Some cart tests return early when the cart has no eligible items. Such a return does not, by itself, establish that the intended cart operation passed.
- Browser and application behavior may vary depending on the local environment and application data.

## 11. Known Scope and Limitations

This repository contains the Selenium test automation files only. It does not include the complete ChaJoy PHP application or its database.

The current test suite is a functional testing implementation and does not represent exhaustive application coverage. Additional assertions, test-data setup and cleanup, and reporting configuration may be introduced in future iterations.

## 12. Author and Project

**Project:** ChaJoy – Online Beverage Ordering System  
**Component:** Selenium Test Automation  
**Testing Framework:** pytest  
**Automation Tool:** Selenium WebDriver
