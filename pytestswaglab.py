import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger()
logger.setLevel(logging.INFO)
chrome_options = Options()
chrome_options.add_argument("--incognito")


@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    logging.info("Opening Chrome browser with webdriver-manager")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

def login(driver):
    driver.get("https://www.saucedemo.com/")
    logger.info("login successful")
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password = driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")

    submit = driver.find_element(By.ID,"login-button")
    submit.click()


    assert driver.current_url == "https://www.saucedemo.com/inventory.html","failed to login"
    print("login successful")

def add_product(driver, product_name):
    driver.get("https://www.saucedemo.com/inventory.html")
    logger.info("Adding products...")


    elements = driver.find_elements(By.CLASS_NAME, "inventory_item")

    for product in elements:
        name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        if product_name.lower() in name.lower():
            logger.info(f"✅ Found product: {name} | Adding to cart...")


            button = product.find_element(By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory")
            button.click()


            remove_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn_secondary.btn_small.btn_inventory"))
            )
            logger.info(f"🛒 Product '{name}' added successfully.")
            return remove_button

    logger.warning(f"❌ Product not found: {product_name}")
    return None


def checkout_step_one(driver):
    driver.get("https://www.saucedemo.com/inventory.html")
    logger.info("checkout step 1")
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

def checkout_step_two(driver):
    driver.get("https://www.saucedemo.com/cart.html")
    logger.info("checkout step 2")
    button=driver.find_element(By.XPATH,'//button[@class="btn btn_action btn_medium checkout_button "]')
    button.click()

def final_checkout(driver):
    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    logger.info("final checkout step 1")
    first_name=driver.find_element(By.ID,"first-name")
    first_name.send_keys("Prattoy")
    last_name=driver.find_element(By.ID,"last-name")
    last_name.send_keys("borson")
    postal_code=driver.find_element(By.ID,"postal-code")
    postal_code.send_keys("2400")
    continue_button=driver.find_element(By.ID,"continue")
    continue_button.click()
    logger.info("final checkout step 2")
    assert 'checkout-step-two.html' in driver.current_url,"failed to login"
    time.sleep(3)
    logger.info("final checkout step 3")
    finish_button=driver.find_element(By.ID,"finish")
    finish_button.click()
    logger.info("final checkout step 4")

def cancels(driver):
    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    logger.info("cancel")
    cancel_button=driver.find_element(By.ID,"cancel")
    cancel_button.click()

def summary_cart(driver):
    driver.get("https://www.saucedemo.com/cart.html")
    cart_items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
    )

    assert len(cart_items)>0,"Cart is empty"
    print("summary cart item")


    for i, item in enumerate(cart_items,1):
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        description = item.find_element(By.CLASS_NAME, "inventory_item_desc").text
        price = item.find_element(By.CLASS_NAME, "inventory_item_price").text

        print(f"Item {i}: {name} | {description} | {price}")
        assert name != "", f"Item {i} name is empty"
        assert description != "", f"Item {i} description is empty"
        assert price.startswith("$"), f"Item {i} price format incorrect: {price}"




@pytest.mark.order(1)
def test_login(driver):
    login(driver)

@pytest.mark.order(2)
def test_add_product(driver):
    login(driver)
    add_product(driver, "Sauce Labs Bolt T-Shirt")



    time.sleep(1)
@pytest.mark.order(3)
def test_checkout(driver):
    login(driver)
    checkout_step_one(driver)
    checkout_step_two(driver)
    final_checkout(driver)
    assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html","failed to checkout"
    print("checkout successful")

@pytest.mark.order(4)
def test_cancel(driver):
    login(driver)
    checkout_step_one(driver)
    checkout_step_two(driver)
    cancels(driver)
    assert driver.current_url == "https://www.saucedemo.com/cart.html","failed to cancel"
    print("cancel successful")

@pytest.mark.order(5)
def test_summary_checkout(driver):
    login(driver)
    add_product(driver, "Sauce Labs Bike Light")
    checkout_step_one(driver)
    summary_cart(driver)















