from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenario, given, when, then, parsers
import pytest

# @pytest.mark.skip(reason="no way of currently testing this")
@scenario("./webapp.feature", "submit search query returns list of results")
def test_submit_search_query_returns_a_list_of_results():
    pass

# @pytest.mark.skip(reason="no way of currently testing this")
@scenario("./webapp.feature", "click Home nav opens Home page")
def test_nav_home():
    pass

@scenario("./webapp.feature", "click About nav opens About page")
def test_nav_about():
    pass

@scenario("./webapp.feature", "click Contact nav opens Contact page")
def test_nav_contact():
    pass

@given("the browser is opened", scope="session")
def browser():
    options=None
    driver = webdriver.Chrome(r"chromedriver.exe", 
        options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@given(parsers.parse('page {page:string} is loaded', extra_types=dict(string=str)))
def navigate_page(browser, page):
    base_url = "https://python-sample-flask-13382.azurewebsites.net/"
    if page == 'Home':
        url = base_url
    elif page == "About":
        url = base_url + "about/"
    elif page == "Contact":
        url = base_url + "contact/"
    else:
        raise KeyError(f"Unknown page {page}")
    browser.get(url)

@given(parsers.parse('url "{url:string}" is loaded', extra_types=dict(string=str)))
def navigate_url(browser, url):
    browser.get(url)



@when(parsers.parse('click "{element_id:string}"', extra_types=dict(string=str)))
def click_element(browser, element_id):
    element = browser.find_element_by_id(element_id)
    element.click()


@when(parsers.parse('click "{element_id:string}" navigates to page "{page_title:string}"',
        extra_types=dict(string=str)))
def click_link_opens_page(browser: webdriver.Chrome, element_id, page_title):
    element = browser.find_element_by_id(element_id)
    element.click()
    assert browser.title == page_title


@when(parsers.parse("submit '{query:string}' query", extra_types=dict(string=str)))
def submit_search_query(browser, query):
    search_box = browser.find_element_by_name('q')
    search_box.send_keys(query + Keys.RETURN)

@then(parsers.parse('page with title "{title:string}" is loaded', extra_types=dict(string=str)))
def then_page_with_title(browser, title):
    assert browser.title == title

@then('The browser returns search results')
def then_the_browser_returns_search_results(browser):
    assert browser.title == "seleniumhq - Google Search"
