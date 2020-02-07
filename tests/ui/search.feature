Feature: Search for websites

    Scenario: submit search query returns list of results
    Given the browser is opened
    When I navigate to "https://www.google.com/"
    And submit 'seleniumhq' query
    Then The browser returns search results

