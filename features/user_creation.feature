Feature: User Creation

  Scenario: Create user with Admin role and Active status
    Given I am on the user creation page
    And I open the user creation form using the "Add New" button
    When I enter "Govarthini_K" as the user name
    And I enter "9879465802" as the contact number
    And I enter "govarthini@trunovatech.com" as the contact email
    And I select the role "Employee"
    And I select the status "ACTIVE"
    And I click the "Save" button on user creation form
    Then the user should be created successfully



  Scenario: Create user with Cooling tower operator role and Inactive status
    Given I am on the user creation page
    And I open the user creation form using the "Add New" button
    When I enter "Jane Smith" as the user name
    And I enter "9123456780" as the contact number
    And I enter "john.doe@example.com" as the contact email
    And I select the role "Cooling tower operator"
    And I select the status "INACTIVE"
    And I click the "Save" button on user creation form
    Then the user should be created successfully


  Scenario: Create user with multiple roles and Active status
    Given I am on the user creation page
    And I open the user creation form using the "Add New" button
    When I enter "Alice Johnson" as the user name
    And I enter "9988776655" as the contact number
    And I enter "john.doe@example.com" as the contact email
    And I select the roles "Manager, Supervisor"
    And I select the status "ACTIVE"
    And I click the "Save" button on user creation form
    Then the user should be created successfully
