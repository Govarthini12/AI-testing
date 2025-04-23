
 📂 Project Structure

├── features/
│   ├── steps/
│   │   └── step_definitions.py
│   ├── login.feature
│   └── user_creation.feature
├── README.md
├── requirements.txt

# AI Testing Automation

This repository contains the code and automation tests for AI Testing using Behave and Selenium. It is designed to automate user creation, login, and role creation in an application using Python's Behave framework and Selenium WebDriver.

## Requirements

Before running the tests, ensure you have the following installed:

- Python 3.x
- Git
- Google Chrome browser (for Selenium WebDriver)

### Required Python Libraries

To install all the required dependencies, follow the instructions below.

 Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Govarthini12/AI-testing.git
cd AI-testing


 Step 2: Set Up a Virtual Environment (Optional but Recommended)
It is a good practice to use a virtual environment for your project to keep dependencies isolated:

``bash

python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate # On macOS/Linux

Step 3: Install Dependencies
Install the required dependencies using the following command:

bash

pip install -r requirements.txt

or
If you don't have a requirements.txt, manually install the required packages:

 pip install selenium behave webdriver-manager

Step 4: Install ChromeDriver
For Selenium to interact with Chrome, you need to install ChromeDriver. Either manually download it or use the webdriver-manager package to handle the installation:
pip install webdriver-manager


Step 5: Running the Tests
To run your Behave tests, use the following command:

bash
behave


You can also run specific feature files by specifying them like this:

bash

python -m behave features/login.feature
python -m behave features/user_creation.feature
python -m behave features/role_creation.feature
