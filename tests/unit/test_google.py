from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os.path import dirname
import pytest

@pytest.fixture(scope="module")
def driver():
    options=None
    driver = webdriver.Chrome(dirname(__file__) + r"/../../chromedriver.exe", 
        options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_search(driver: webdriver.Chrome):
    driver.get('https://www.google.com/')
    search_box = driver.find_element_by_name('q')
    search_box.send_keys("seleniumhq" + Keys.RETURN)
    assert driver.title == "seleniumhq - Google Search"
