Feature: Create Lead

  Scenario: Create Lead
    When  I navigate to "Sales" "Leads"
    And   Select view "All Leads"
    And   Click on ribbon button "New"
    And   Fill form data from csv file "d365.0001.CreateLead.data"
    Then  Click on ribbon button "Save"