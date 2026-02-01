import json
from selenium import webdriver
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from config.config import BASE_URL, TIMEOUT

def test_profile_update():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)

    with open("data/credentials.json") as f:
        creds = json.load(f)

    login_page = LoginPage(driver, TIMEOUT)
    profile_page = ProfilePage(driver, TIMEOUT)

    login_page.open_login()
    login_page.login(creds["username"], creds["password"])

    profile_page.open_profile()
    profile_page.update_headline()
    profile_page.save_profile()

    # ASSERTION (interview critical)
    assert "profile" in driver.current_url.lower()

    driver.quit()
