from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenario, given, when, then, parsers



@scenario("./search.feature", "submit search query returns list of results")
def test_submit_search_query_returns_a_list_of_results():
    pass


@given("the browser is opened", scope="session")
def browser():
    options=None
    driver = webdriver.Chrome(r"chromedriver.exe", 
        options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@when(parsers.parse('I navigate to "{url:string}"', extra_types=dict(string=str)))
def navigate_page(browser, url):
    browser.get(url)


@when(parsers.parse("submit '{query:string}' query", extra_types=dict(string=str)))
def submit_search_query(browser, query):
    search_box = browser.find_element_by_name('q')
    search_box.send_keys(query + Keys.RETURN)

@then('The browser returns search results')
def then_the_browser_returns_search_results(browser):
    assert browser.title == "seleniumhq - Google Search"


# @pytest.fixture(scope="module")
# def driver():
#     options=None
#     driver = webdriver.Chrome(r"chromedriver.exe", 
#         options=options)
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()

# def atest_search(driver: webdriver.Chrome):
#     driver.get('https://www.google.com/')
#     search_box = driver.find_element_by_name('q')
#     search_box.send_keys("seleniumhq" + Keys.RETURN)
#     assert driver.title == "seleniumhq - Google Search"
