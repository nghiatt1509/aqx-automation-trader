# AQX Automation Trader - Python Playwright Test

## 📦 Tech Stack
- Python 3.13
- Pytest
- Playwright
- Allure Report
- GitHub Actions

## 🚀 Local Test

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest --alluredir=allure-results
allure serve allure-results