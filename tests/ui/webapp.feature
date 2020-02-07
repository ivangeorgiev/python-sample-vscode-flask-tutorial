Feature: Search for websites

    Scenario: submit search query returns list of results
    Given the browser is opened
    When I navigate to "https://www.google.com/"
    And submit 'seleniumhq' query
    Then The browser returns search results

    Scenario: site is up
    Given the browser is opened
    When I navigate to "https://python-sample-flask-13382.azurewebsites.net/"
    And click "nav-home" navigates to page "Home"
    And click "nav-about" navigates to page "About"
    And click "nav-contact" navigates to page "Contact"
