import pytest
from pages.login_page import LoginPage
from utils.data_loader import load_login_data

# Data-driven test: run the same login test with multiple sets of credentials

@pytest.mark.skip(reason="Covered by test_trader.py")
@pytest.mark.parametrize("credentials", load_login_data())
def test_login_with_multiple_credentials(page, credentials):  
    # Step 1: Initialize LoginPage object
    login_page = LoginPage(page)

    # Step 2: Open the login page (navigate to login URL)
    login_page.open_login_page()

    # Step 3: Fill in login form and submit with provided credentials
    login_page.login(credentials["username"], credentials["password"])

    # Step 4: Verify that login is successful by checking for key UI elements
    assert login_page.verify_login_successfully(), f"Login failed for user: {credentials['username']}"