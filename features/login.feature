Feature: User Login
  As a registered user
  I want to log into the system
  So that I can access the dashboard

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter "user@example.com" as the email
    And I enter "password123" as the password
    And I click the login button
    Then I should be redirected to the dashboard

  Scenario: Unsuccessful login with invalid password
    Given I am on the login page
    When I enter "user@example.com" as the email
    And I enter "wrongpassword" as the password
    And I click the login button
    Then I should see a login error message
