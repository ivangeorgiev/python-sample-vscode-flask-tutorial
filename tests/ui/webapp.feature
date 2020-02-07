Feature: Search for websites

    Scenario: submit search query returns list of results
    Given url "https://www.google.com/" is loaded
    When submit 'seleniumhq' query
    Then The browser returns search results

    Scenario: click Home nav opens Home page
    Given page About is loaded
    When click "nav-home"
    Then page with title "Home" is loaded

    Scenario: click About nav opens About page
    Given page Home is loaded
    When click "nav-about"
    Then page with title "About us" is loaded

    Scenario: click Contact nav opens Contact page
    Given page Home is loaded
    When click "nav-contact"
    Then page with title "Contact us" is loaded
