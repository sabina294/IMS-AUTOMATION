import logging
import pytest
from utils.screenshot_utils import capture_full_page_screenshot
from pages.login_page import LoginPage
from utils.data_loader import load_all_test_data

@pytest.mark.parametrize("test_case", load_all_test_data("../data/data.json"))
def test_tc_login_001(browser_config, test_case):
    logging.info("TC_LOGIN_001 Started..")
    logging.info(test_case["login"][0]["TC_LOGIN_001"]["_comment"])
    driver, wait = browser_config

    login_page = LoginPage(driver, wait)

    # Step 1: Enter Username
    try:
        login_page.enter_user_id(test_case["login"][0]["TC_LOGIN_001"]["username"])
        logging.info("Valid Username entered successfully.")
    except Exception as e:
        capture_full_page_screenshot(driver, "username_error")
        logging.error(f"Element 'Username' not found. Error: {e}")
        pytest.fail("Test Failed. Username field not found. !!!")

    # Step 2: Enter Password
    try:
        login_page.enter_password(test_case["login"][0]["TC_LOGIN_001"]["password"])
        logging.info("Valid Password entered successfully.")
    except Exception as e:
        capture_full_page_screenshot(driver, "password_error")
        logging.error(f"Element 'Password' not found. Error: {e}")
        pytest.fail("Test Failed. Password field not found. !!!")

    # Step 3: Click Login
    try:
        login_page.click_login_button()
        logging.info("Click on Login button successfully.")
    except Exception as e:
        capture_full_page_screenshot(driver, "login_button_error")
        logging.error(f"Element 'Login' button not found. Error: {e}")
        pytest.fail("Test Failed. Login button not found. !!!")

        driver.quit()
