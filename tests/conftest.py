import sys
import os
import pytest
from playwright.sync_api import sync_playwright
import allure

# Add project root to Python path so other modules can be imported easily
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.config import DEFAULT_TIMEOUT, DEFAULT_VIEWPORT, IS_CI
from pages.base_page import BasePage

def get_viewport_size():
    """
    Determine the viewport size based on the environment.
    - In CI, return a fixed size (e.g., 1920x1080).
    - Locally, try to detect the actual screen resolution using pyautogui.
    """
    if IS_CI:
        return DEFAULT_VIEWPORT
    else:
        try:
            import pyautogui
            width, height = pyautogui.size()
            return {"width": width, "height": height}
        except Exception:
            return DEFAULT_VIEWPORT  # fallback in case pyautogui fails
        

@pytest.fixture
def page():
    """
    Main Playwright fixture that provides a configured browser page:
    - Uses custom viewport based on local/CI
    - Applies global default timeout
    - Maximizes window on local machines
    - Automatically closes browser after test
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=IS_CI)  # headless in CI only
        context = browser.new_context(viewport=get_viewport_size())
        page = context.new_page()

        # Set global timeout for all actions (e.g. click, fill, wait_for_selector)
        page.set_default_timeout(DEFAULT_TIMEOUT)

        # Maximize browser only in local environment (not CI)
        if not IS_CI:
            base = BasePage(page)
            base.maximize_window()

        yield page
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on failure and attach to Allure Report.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            # Chụp screenshot
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)

            # Attach vào Allure
            with open(screenshot_path, "rb") as f:
                allure.attach(f.read(), name="screenshot", attachment_type=allure.attachment_type.PNG)