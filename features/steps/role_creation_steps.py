
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from time import sleep

@given('I am on the role creation page')
def step_impl(context):
    context.driver.get("https://trunova-coolingtower-iiot-app-ae7e23b9458d.herokuapp.com/role_creation")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'addnewBtn')]"))
    )

@when('I open the role creation form using the "Add New" button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "addnewBtn") and contains(text(), "Add New")]')))
    add_button.click()

@when('I enter "{role_name}" as the role name')
def step_impl(context, role_name):
    role_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Role Name']"))
    )
    role_input.clear()
    role_input.send_keys(role_name)

@when('I enter "{role_description}" as the role description')
def step_impl(context, role_description):
    desc_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Role Description']"))
    )
    desc_input.clear()
    desc_input.send_keys(role_description)

@when('I select "{screen1}" and "{screen2}" as screen names')
def step_impl(context, screen1, screen2):
    wait = WebDriverWait(context.driver, 10)
    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'dropdown-btn')]")))
    dropdown.click()
    sleep(1)

    for screen in [screen1, screen2]:
        checkbox_xpath = f"//li[contains(@class, 'multiselect-item-checkbox')]//div[text()='{screen}']/preceding-sibling::input"
        try:
            checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath)))
            if not checkbox.is_selected():
                context.driver.execute_script("arguments[0].click();", checkbox)
                sleep(0.2)
        except ElementClickInterceptedException:
            print(f"Retrying JavaScript click for: {screen}")
            checkbox = context.driver.find_element(By.XPATH, checkbox_xpath)
            context.driver.execute_script("arguments[0].click();", checkbox)
            sleep(0.2)

@when('I select no screen names')
def step_impl(context):
    pass  # intentionally left empty

@when('I set the status to "{status}"')
def step_impl(context, status):
    status_dropdown = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select"))
    )
    status_dropdown.click()
    sleep(0.3)
    option = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//option[normalize-space(text())='{status.upper()}']"))
    )
    option.click()

@when('I click the "Save" button')
def step_impl(context):
    save_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save')]"))
    )
    save_btn.click()
    sleep(2)

@then('the role should be created successfully')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Role created successfully')]"))
        )
    except TimeoutException:
        assert False, "Success message not found."

@then('the role name "{role_name}" should be displayed')
def step_impl(context, role_name):
    displayed_role = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//td[contains(text(), '{role_name}')]"))
    )
    assert displayed_role is not None

@then('an error message should be displayed')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'error') or contains(@class, 'alert-danger')]"))
    )

@then('the error message should contain "Role Name is required"')
def step_impl(context):
    error_message = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Role Name is required')]")
    assert "Role Name is required" in error_message.text

@when('I click the "Reset" button')
def step_impl(context):
    reset_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Reset')]"))
    )
    reset_btn.click()
