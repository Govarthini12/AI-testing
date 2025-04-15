Feature: Role Creation

  Scenario: Create a new role with valid details
    Given I am on the role creation page
    When I open the role creation form using the "Add New" button
    And I enter "Developer" as the role name
    And I enter "Developing software" as the role description
    And I select "Dashboard" and "Users" as screen names
    And I set the status to "ACTIVE"
    And I click the "Save" button
    Then the role should be created successfully
    And the role name "Developer" should be displayed

  Scenario: Create a new role with invalid details
    Given I am on the role creation page
    When I open the role creation form using the "Add New" button
    And I enter "Admin" as the role name
    And I enter "Administrator " as the role description
    And I select no screen names
    And I set the status to "ACTIVE"
    And I click the "Save" button
    Then an error message should be displayed
    And the error message should contain "Role Name is required"

  Scenario: Reset role creation form
    Given I am on the role creation page
    When I open the role creation form using the "Add New" button
    And I enter "Temporary Role" as the role name
    And I click the "Reset" button
    Then the form should be reset to its initial state
