import allure
from dotenv import load_dotenv
from utils.browser_utils import wait_for_page_load_successfully
from config.config import LOGIN_URL

# Define all selectors as constants for maintainability
DEMO_TAB = 'div[data-testid="tab-login-account-type-demo"]'
USERNAME_INPUT = 'input[data-testid="login-user-id"]'
PASSWORD_INPUT = 'input[data-testid="login-password"]'
LOGIN_BUTTON = 'button[data-testid="login-submit"]'
SEARCH_INPUT = 'input[data-testid="symbol-input-search"]'
ORDER_BUTTON = 'button[data-testid="trade-button-order"]'

class LoginPage:
    def __init__(self, page):
        """
        Initialize LoginPage with a Playwright page instance.
        Loads environment variables from a .env file.
        """
        self.page = page
        load_dotenv()  # Load environment variables (e.g. credentials) from .env file

    @allure.step("Navigate to login page")
    def open_login_page(self):
        # Navigate to login page URL and wait for the page to be fully loaded
        self.page.goto(LOGIN_URL, wait_until="load")
        wait_for_page_load_successfully(self.page)

    @allure.step("Login with Demo credentials: {username} / ******")
    def login(self, username, password):
        # Click on the "Demo Account" tab
        self.page.click(DEMO_TAB)

        # Fill in user ID and password fields
        self.page.fill(USERNAME_INPUT, username)
        self.page.fill(PASSWORD_INPUT, password)

        # Click on the login button
        self.page.click(LOGIN_BUTTON)

        # Wait for the dashboard or main page to finish loading
        wait_for_page_load_successfully(self.page)

    @allure.step("Verify whether login was successful with Demo credentials")
    def verify_login_successfully(self):
        """
        Verify whether login was successful by checking for key elements
        that appear only after a successful login.

        Returns:
            bool: True if login was successful, False otherwise.
        """
        try:
            # Check for key UI elements that confirm successful login
            self.page.wait_for_selector(SEARCH_INPUT)
            self.page.wait_for_selector(ORDER_BUTTON)
            return True
        except:
            # If any element is missing, assume login failed
            return False