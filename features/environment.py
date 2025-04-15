from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    options = Options()
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')  
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--remote-debugging-port=9222')
    options = webdriver.ChromeOptions() # Optional: run in headless mode
    context.driver = webdriver.Chrome(options=options)  # Ensure chromedriver is in PATH

    service = Service('drivers/chromedriver.exe')
    context.driver = webdriver.Chrome(service=service, options=options)
    # Maximize the window to make sure all elements are visible
    context.driver.maximize_window()
    # Add implicit wait as a backup
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
