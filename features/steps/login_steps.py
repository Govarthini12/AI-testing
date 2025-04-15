from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the login page')
def step_impl(context):
    options = Options()
    options.add_argument("--disable-gpu")  # Avoid GPU errors
    context.driver = webdriver.Chrome(options=options)
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
    context.driver.execute_script("arguments[0].click();", login_button)

@then('I should be redirected to the dashboard')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 15).until(
            EC.url_contains("dashboard")
        )
        assert "dashboard" in context.driver.current_url.lower()
        print("✅ Redirected to Dashboard:", context.driver.current_url)
    finally:
        context.driver.quit()

@then('I should see a login error message')
def step_impl(context):
    try:
        # Adjust error message XPath based on real DOM
        error_element = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Invalid") or contains(text(), "incorrect") or contains(text(), "error")]'))
        )
        assert error_element.is_displayed()
        print("✅ Error message displayed.")
    finally:
        context.driver.quit()

# from behave import given, when, then
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# @given('I am on the login page')
# def step_impl(context):
#     context.driver = webdriver.Chrome()
#     context.driver.get("https://trunova-coolingtower-iiot-app-ae7e23b9458d.herokuapp.com/login")
#     context.driver.maximize_window()
#     WebDriverWait(context.driver, 10).until(
#         EC.presence_of_element_located((By.ID, "emailLogin"))
#     )

# @when('I enter "{email}" as the email')
# def step_impl(context, email):
#     email_input = context.driver.find_element(By.ID, "emailLogin")
#     email_input.clear()
#     email_input.send_keys(email)

# @when('I enter "{password}" as the password')
# def step_impl(context, password):
#     password_input = context.driver.find_element(By.ID, "passwordLogin")
#     password_input.clear()
#     password_input.send_keys(password)

# @when('I click the login button')
# def step_impl(context):
#     login_button = context.driver.find_element(By.XPATH, '//button[contains(text(), "Login")]')
#     context.driver.execute_script("arguments[0].click();", login_button)  # safer than .click()


# @then('I should be redirected to the dashboard')
# def step_impl(context):
#     # You can change this URL check based on your actual dashboard URL
#     WebDriverWait(context.driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Dashboard")]'))
#     )
#     assert "dashboard" in context.driver.current_url.lower()

#     context.driver.quit()

# @then('I should see a login error message')
# def step_impl(context):
#     WebDriverWait(context.driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, '//p[contains(text(), "Invalid")]'))
#     )
#     error_msg = context.driver.find_element(By.XPATH, '//p[contains(text(), "Invalid")]')
#     assert error_msg.is_displayed()
#     context.driver.quit()
