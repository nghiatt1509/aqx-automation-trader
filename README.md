AQX Automation Trader

Automation framework for testing core trading functionalities on the AQX Trading Platform, built using Playwright, Pytest, and Allure Report.

⸻

🚀 Features
	•	✅ Login with data-driven credentials (from JSON)
	•	✅ Place Market Orders with Stop Loss / Take Profit / Volume
	•	✅ Verify order placed successfully (via UI table)
	•	✅ Close single order or bulk-close all
	•	✅ Allure report with step-by-step detail
	•	✅ Framework built using POM structure

⸻

📁 Project Structure

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


⸻

🔧 Setup

1. Clone repo & install dependencies

git clone https://github.com/<your-username>/aqx-automation-trader.git
cd aqx-automation-trader
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

2. Setup .env (optional)

BASE_URL=https://aqxtrader.aquariux.com/web
LOGIN_URL=https://aqxtrader.aquariux.com/web/login

3. Run tests and generate Allure report

# Run tests with detailed output 
pytest --alluredir=allure-results --headed -v

# Generate Allure report
allure serve allure-results
