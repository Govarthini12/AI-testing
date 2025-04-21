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
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "addnewBtn") and contains(text(), "Add New")]')))
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


@when('I select the role "{role}"')
def step_impl(context, role):
    wait = WebDriverWait(context.driver, 10)
    dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "dropdown-btn")))
    dropdown.click()
    time.sleep(1)
    role_elements = context.driver.find_elements(By.XPATH, f'//div[text()="{role}"]/preceding-sibling::input[@type="checkbox"]')
    for el in role_elements:
        context.driver.execute_script("arguments[0].click();", el)
    dropdown.click()  # Close dropdown

# @when('I select the roles "{roles}"')
# def step_impl(context, roles):
#     role_list = [r.strip() for r in roles.split(',')]
#     wait = WebDriverWait(context.driver, 10)
#     dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "dropdown-btn")))
#     dropdown.click()
#     time.sleep(1)
#     for role in role_list:
#         role_elements = context.driver.find_elements(By.XPATH, f'//div[text()="{role}"]/preceding-sibling::input[@type="checkbox"]')
#         for el in role_elements:
#             context.driver.execute_script("arguments[0].click();", el)
#     dropdown.click()  # Close dropdown

@when('I select the status "{status}"')
def step_impl(context, status):
    select_element = Select(context.driver.find_element(By.XPATH, '//select'))
    select_element.select_by_visible_text(status.strip())

@when('I click the "Save" button on user creation form')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Save")]')))
    save_btn.click()



@then('the user should be created successfully')
def step_impl(context):
    # Assuming success message is shown
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "User created successfully")]'))
    )
    print("User creation passed")
    context.driver.quit()
