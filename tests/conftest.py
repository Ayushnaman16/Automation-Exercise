import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function')
def setup():
    location=Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-popup-blocking")
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--disable-save-password-bubble")
    driver = webdriver.Chrome(service=location, options=options)
    driver.maximize_window()

    driver.execute_cdp_cmd("Network.enable", {})

    driver.execute_cdp_cmd(
        "Network.setBlockedURLs",
        {
            "urls": [
                "*doubleclick.net*",
                "*googlesyndication.com*",
                "*googleads*",
                "*adsystem*",
                "*adservice*",
                "*analytics*"
            ]
        }
    )
    yield driver
    driver.quit()