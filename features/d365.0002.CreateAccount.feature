Feature: Create Account

  Scenario: Create Account
    When  I navigate to "Sales" "Accounts"
    And   Select view "Active Accounts"
    And   Click on ribbon button "New"
    And   Fill form data from csv file "d365.0002.CreateAccount.data"
    Then  Click on ribbon button "Save"