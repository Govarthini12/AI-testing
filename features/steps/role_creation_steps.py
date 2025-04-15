from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup for the WebDriver
@given('I am on the role creation page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://trunova-coolingtower-iiot-app-ae7e23b9458d.herokuapp.com/role_creation")
    context.driver.maximize_window()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

# Step for opening the role creation form
@when('I open the role creation form using the "Add New" button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "addnewBtn") and contains(text(), "Add New")]')))
    add_button.click()

# Step for entering role name
@when('I enter "{role_name}" as the role name')
def step_impl(context, role_name):
    wait = WebDriverWait(context.driver, 10)
    field = context.driver.find_element(By.ID, "roleName")
    field.clear()
    field.send_keys(role_name)

# Step for entering role description
@when('I enter "{role_description}" as the role description')
def step_impl(context, role_description):
    field = context.driver.find_element(By.ID, "roleDescription")
    field.clear()
    field.send_keys(role_description)

# Step for selecting screen names
@when('I select "{screen1}" and "{screen2}" as screen names')
def step_impl(context, screen1, screen2):
    dropdown = context.driver.find_element(By.CSS_SELECTOR, ".multiselect-dropdown")
    dropdown.click()
    WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, f"//input[@aria-label='{screen1}']"))
    )
    context.driver.find_element(By.XPATH, f"//input[@aria-label='{screen1}']").click()
    context.driver.find_element(By.XPATH, f"//input[@aria-label='{screen2}']").click()

# Step for no screen names selected
@when('I select no screen names')
def step_impl(context):
    pass  # No action needed for empty selection

# Step for setting the status
@when('I set the status to "{status}"')
def step_impl(context, status):
    dropdown = context.driver.find_element(By.ID, "statusDropdown")
    dropdown.click()
    option = dropdown.find_element(By.XPATH, f".//option[text()='{status}']")
    option.click()

# Step for clicking the Save button
@when('I click the "Save" button')
def step_impl(context):
    save_button = context.driver.find_element(By.ID, "saveBtn")
    save_button.click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "successMessage"))
    )

# Step to verify successful role creation
@then('the role should be created successfully')
def step_impl(context):
    message = context.driver.find_element(By.ID, "successMessage")
    assert "Role created successfully" in message.text

# Step to verify the role name displayed
@then('the role name "{role_name}" should be displayed')
def step_impl(context, role_name):
    displayed_role = context.driver.find_element(By.CSS_SELECTOR, ".role-display")
    assert role_name in displayed_role.text

# Step for verifying error message on invalid details
@then('an error message should be displayed')
def step_impl(context):
    error_message = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message"))
    )
    assert error_message.is_displayed()

# Step for verifying error message text
@then('the error message should contain "{error_message}"')
def step_impl(context, error_message):
    error_elem = context.driver.find_element(By.CSS_SELECTOR, ".error-message")
    assert error_message in error_elem.text

# Step for clicking the Reset button
@when('I click the "Reset" button')
def step_impl(context):
    reset_button = context.driver.find_element(By.ID, "resetBtn")
    reset_button.click()
    time.sleep(1)  # Ensure reset action takes place before verifying

# Step for verifying the form is reset
@then('the form should be reset to its initial state')
def step_impl(context):
    name_field = context.driver.find_element(By.ID, "roleName")
    desc_field = context.driver.find_element(By.ID, "roleDescription")
    assert name_field.get_attribute('value') == ""
    assert desc_field.get_attribute('value') == ""
