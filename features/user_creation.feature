Feature: User Creation
  As an administrator
  I want to be able to create new users
  So that I can manage access to the system

  Scenario: Create a new user with valid details
    Given I am on the user creation page
    And I open the user creation form using the "Add New" button
    When I enter "John Doe" as the user name
    And I enter "9999999999" as the contact number
    And I enter "john@example.com" as the contact email
    And I select "Manager" as the role name
    And I select "ACTIVE" as the status
    And I click the "Save" button
    Then I should see a success message

  Scenario: Create user with missing email
    Given I am on the user creation page
    And I open the user creation form using the "Add New" button
    When I enter "Jane Smith" as the user name
    And I enter "8888888888" as the contact number
    And I leave the email empty
    And I select "Admin" as the role name
    And I select "ACTIVE" as the status
    And I click the "Save" button
    Then I should see an error message

  Scenario: Create user with invalid role name
    Given I am on the user creation page
    And I open the user creation form using the "Add New" button
    When I enter "Alice Example" as the user name
    And I enter "7777777777" as the contact number
    And I enter "alice@example.com" as the contact email
    And I select "InvalidRole" as the role name
    And I select "ACTIVE" as the status
    And I click the "Save" button
    Then I should see a success message
