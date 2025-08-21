from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def enter_user_id(self, username_value):
        user_id = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#email"))
        )
        user_id.clear()
        user_id.send_keys(str(username_value))

    def enter_password(self, password_value):
        password = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#password"))
        )
        password.clear()
        password.send_keys(str(password_value))

    def click_login_button(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='submit-button'] span"))
        )
        login_button.click()

