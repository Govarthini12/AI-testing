# 🚀 TruNova Automation Testing Suite

This repository contains automated test cases for the **TruNova IIoT Web Application** using **Python**, **Selenium**, and **Behave (BDD)**. It focuses on critical user flow validations including **User Creation** and **Login Functionality**.

Branch: `govarthini-testing-agent`

 📂 Project Structure

├── features/
│   ├── steps/
│   │   └── step_definitions.py
│   ├── login.feature
│   └── user_creation.feature
├── README.md
├── requirements.txt


## ⚙️ Technologies Used

- 🐍 Python 3.8+
- 🌐 Selenium WebDriver
- 🧪 Behave (Behavior Driven Development)
- 🧰 ChromeDriver

---

## 🔧 Installation

1. **Clone the repository**

bash
  git clone -b govarthini-testing-agent https://github.com/TruNovaTech/truNova-testing-agent.git
  cd truNova-testing-agent
  
2. Create a virtual environment (optional but recommended)

  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install dependencies

  pip install -r requirements.txt

4. 🚀 Running the Tests
    * To execute all scenarios:
          behave
    * To run a specific feature file:
        behave features/user_creation.feature
