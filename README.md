Here’s a README.md file tailored for your pytest Selenium project where all tests are passing successfully:

# SauceDemo Automation Test Suite

This project contains an automated test suite for **SauceDemo** (https://www.saucedemo.com/) using **Python**, **Selenium WebDriver**, and **pytest**. The suite covers login, product addition, checkout, cancel, and cart summary functionalities.

---

## Project Structure



.
├── pytestswaglab.py # Main test script containing all test cases
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .venv # Virtual environment (optional)


---

## Prerequisites

- Python 3.10+ installed
- Google Chrome browser installed
- ChromeDriver (managed automatically using `webdriver-manager`)
- Virtual environment recommended

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/PaulBorson/swag_lab-Souce_demo-.git
cd swag_lab-Souce_demo-.git


Create and activate virtual environment (optional but recommended):

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate


Install required dependencies:

pip install -r requirements.txt

How to Run Tests

To execute all tests:

pytest -v --order-scope=module


-v gives verbose output

--order-scope=module ensures tests run in the defined order

All tests are expected to pass successfully.

Test Cases Included

Login Test
Verifies login functionality with valid credentials (standard_user / secret_sauce).

Add Product Test
Searches for a product (e.g., "Sauce Labs Bolt T-Shirt") and adds it to the cart.

Checkout Test
Completes the checkout process, including entering first name, last name, and postal code.

Cancel Checkout Test
Navigates to checkout and clicks Cancel, returning to the cart page.

Cart Summary Test
Validates that items in the cart display proper name, description, and price format.

Logging

All test steps are logged using Python's logging module.
You can view logs for debugging or test execution insights.

Notes

Chrome is launched in incognito mode to ensure a clean session.

WebDriver is automatically managed by webdriver-manager.

Assertions ensure that the application behaves as expected:

Successful login

Product added to cart

Checkout completed

Cart contains items

Cancel redirects properly

Dependencies
selenium
pytest
pytest-order
webdriver-manager


You can install them using:

pip install selenium pytest pytest-order webdriver-manager

Author

Prattoy Paul Borson
Automated QA Test Suite for SauceDemo


