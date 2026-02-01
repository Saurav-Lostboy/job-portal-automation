from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ProfilePage:

    def __init__(self, driver, timeout):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.profile_link = (By.ID, "view-profile")
        self.edit_button = (By.ID, "edit-profile")
        self.headline_input = (By.ID, "profile-headline")
        self.save_button = (By.ID, "save-profile")

    def open_profile(self):
        self.wait.until(EC.element_to_be_clickable(self.profile_link)).click()

    def update_headline(self):
        field = self.wait.until(EC.visibility_of_element_located(self.headline_input))
        field.send_keys(".")
        field.send_keys(Keys.BACKSPACE)

    def save_profile(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()
