from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver, timeout):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.login_button = (By.ID, "login-button")
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.submit_button = (By.ID, "submit-login")

    def open_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
