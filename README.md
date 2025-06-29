## AQX Automation Trader

![CI](https://github.com/nghiatt1509/aqx-automation-trader/actions/workflows/ci.yml/badge.svg)

Automation framework for testing core trading functionalities on the AQX Trading Platform, built using Playwright, Pytest, and Allure Report.

## 🚀 Features

- ✅ Login with data-driven credentials (from JSON)
- ✅ Place Market Orders with Stop Loss / Take Profit / Volume
- ✅ Verify order placed successfully (via UI table)
- ✅ Close bulk-close all opening Orders
- ✅ Allure report with step-by-step detail
- ✅ Framework built using POM structure
- ✅ CI/CD via GitHub Actions

## 📁 Project Structure
```
📦aqx-automation-trader
 ┣ 📂pages
 ┃ ┣ 📜login_page.py
 ┃ ┗ 📜trader_page.py
 ┣ 📂tests
 ┃ ┣ 📜test_login.py
 ┃ ┗ 📜test_place_market.py
 ┣ 📂utils
 ┃ ┗ 📜browser_utils.py
 ┣ 📂data
 ┃ ┗ 📜login_data.json
 ┣ 📜.env
 ┣ 📜.gitignore
 ┣ 📜pytest.ini
 ┣ 📜requirements.txt
 ┗ 📜README.md
```

## 🔧 Setup

1. Clone repo & install dependencies
```
git clone https://github.com/<your-username>/aqx-automation-trader.git
cd aqx-automation-trader
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
2. Install requirements
- 📦 For CI or Linux/macOS without GUI:
```
pip install -r requirements.txt
```
- 🧪 For local development with GUI (e.g., Mac, PyAutoGUI):
```
pip install -r requirements-dev.txt
```
3. Setup .env (optional)
```
BASE_URL=https://aqxtrader.aquariux.com/web
LOGIN_URL=https://aqxtrader.aquariux.com/web/login
```
4. Run tests and generate Allure report
# Run tests with detailed output 
```bash
pytest --alluredir=allure-results --headed -v
```
# Generate Allure report
```bash
allure serve allure-results
```
```
✅ --headed shows the browser UI. Use headless for CI runs.
📌 -v enables verbose output.
```

## 🔄 Continuous Integration (CI)

- This project includes a GitHub Actions workflow (.github/workflows/ci.yml) that:
- Runs on every push or pull request to main
- Installs Python, Playwright, and all dependencies
- Executes all tests using Pytest
- Collects Allure test results as artifacts
- CI runs are visible under the Actions tab on GitHub

### 📤 View Allure Report from GitHub CI

After each test run on GitHub Actions, an artifact named `allure-results` is uploaded.

To view the report:

1. Go to the **Actions** tab
2. Select the latest workflow run
3. Download the artifact named **`allure-results`**
4. On your local machine:
```bash
   allure serve allure-results
```

## 📄 License
MIT © 2025 Nghia Tran
