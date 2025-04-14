from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://trunova-coolingtower-iiot-app-ae7e23b9458d.herokuapp.com/login")
    context.driver.maximize_window()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "emailLogin"))
    )

@when('I enter "{email}" as the email')
def step_impl(context, email):
    email_input = context.driver.find_element(By.ID, "emailLogin")
    email_input.clear()
    email_input.send_keys(email)

@when('I enter "{password}" as the password')
def step_impl(context, password):
    password_input = context.driver.find_element(By.ID, "passwordLogin")
    password_input.clear()
    password_input.send_keys(password)

@when('I click the login button')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, '//button[contains(text(), "Login")]')
    login_button.click()

@then('I should be redirected to the dashboard')
def step_impl(context):
    # You can change this URL check based on your actual dashboard URL
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("dashboard")
    )
    assert "dashboard" in context.driver.current_url
    context.driver.quit()

@then('I should see a login error message')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "invalid") or contains(text(), "error")]'))
    )
    context.driver.quit()
