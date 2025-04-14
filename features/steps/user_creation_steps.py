from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

@given('I am on the user creation page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://trunova-coolingtower-iiot-app-ae7e23b9458d.herokuapp.com/user_creation")
    context.driver.maximize_window()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

@given('I open the user creation form using the "Add New" button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    add_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//button[contains(@class, "addnewBtn") and contains(text(), "Add New")]')))
    add_button.click()

@when('I enter "{name}" as the user name')
def step_impl(context, name):
    wait = WebDriverWait(context.driver, 10)
    name_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter User Name"]')))
    name_field.clear()
    name_field.send_keys(name)

@when('I enter "{number}" as the contact number')
def step_impl(context, number):
    contact_field = context.driver.find_element(By.XPATH, '//input[@placeholder="Enter Contact Number"]')
    contact_field.clear()
    contact_field.send_keys(number)

@when('I enter "{email}" as the contact email')
def step_impl(context, email):
    email_field = context.driver.find_element(By.XPATH, '//input[@placeholder="Enter Contact Email"]')
    email_field.clear()
    email_field.send_keys(email)

@when('I leave the email empty')
def step_impl(context):
    email_field = context.driver.find_element(By.XPATH, '//input[@placeholder="Enter Contact Email"]')
    email_field.clear()

@when('I select "{role}" as the role name')
def step_impl(context, role):
    wait = WebDriverWait(context.driver, 10)
    
    # Click to open the role dropdown
    role_dropdown_toggle = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "role-multiselect")]')))
    role_dropdown_toggle.click()
    
    # Select the role item based on visible text
    role_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, f'//li[contains(@class, "multiselect-item-checkbox")]//div[text()="{role}"]')))
    role_option.click()

@when('I select "{status}" as the status')
def step_impl(context, status):
    status_dropdown = Select(context.driver.find_element(By.XPATH, '//select[@name="status"]'))
    status_dropdown.select_by_visible_text(status)

@when('I click the "Save" button')
def step_impl(context):
    save_btn = context.driver.find_element(By.XPATH, '//button[contains(text(), "Save")]')
    save_btn.click()

@then('I should see a success message')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    success_message = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "successfully")]')))
    assert success_message is not None
    context.driver.quit()

@then('I should see an error message')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "error") or contains(text(), "required")]')))
    assert error_message is not None
    context.driver.quit()
