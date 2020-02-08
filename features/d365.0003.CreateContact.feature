Feature: Create Contact

  Scenario: Create Contact
    When  I navigate to "Sales" "Contacts"
    And   Select view "Active Contacts"
    And   Click on ribbon button "New"
    And   Fill form data from csv file "d365.0003.CreateContact.data"
    Then  Click on ribbon button "Save"