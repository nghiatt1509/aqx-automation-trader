import pytest
from pages.login_page import LoginPage
from pages.trader_page import TraderPage
from utils.data_loader import load_login_data

# Shared login fixture for reusability
def login_and_verify(page, credentials):
    # Step 1: Perform login and verify success
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login(credentials["username"], credentials["password"])
    assert login_page.verify_login_successfully(), f"Login failed for user: {credentials['username']}"
    return TraderPage(page)

# Test case 1: Place market order with both SL and TP
@pytest.mark.parametrize("credentials", load_login_data())
def test_place_market_order_with_sl_and_tp(page, credentials):
    # Step 1: Login and verify
    trader_page = login_and_verify(page, credentials)

    # Step 2: Get current order count
    count_before = trader_page.get_open_order_count()

    # Step 3: Place market order with SL and TP
    trader_page.place_market_order_with_sl_tp(sl="10", tp="20")

    # Step 4: Verify that a new order was added
    assert trader_page.verify_order_added(count_before), "No new order row added after placing order."

    # Step 5: Close all opening orders to clean up
    trader_page.close_all_open_orders()

# Test case 2: Place market order with only Stop Loss
@pytest.mark.parametrize("credentials", load_login_data())
def test_place_market_order_with_stop_loss_only(page, credentials):
    # Step 1: Login and verify
    trader_page = login_and_verify(page, credentials)

    # Step 2: Get current order count
    count_before = trader_page.get_open_order_count()

    # Step 3: Place market order with only SL
    trader_page.place_market_order_with_sl_tp(sl="10", tp="")

    # Step 4: Verify that a new order was added
    assert trader_page.verify_order_added(count_before), "No new order row added after placing order."

    # Step 5: Close all opening orders to clean up
    trader_page.close_all_open_orders()

# Test case 3: Place market order with only Take Profit
@pytest.mark.parametrize("credentials", load_login_data())
def test_place_market_order_with_take_profit_only(page, credentials):
    # Step 1: Login and verify
    trader_page = login_and_verify(page, credentials)

    # Step 2: Get current order count
    count_before = trader_page.get_open_order_count()

    # Step 3: Place market order with only TP
    trader_page.place_market_order_with_sl_tp(sl="", tp="20")

    # Step 4: Verify that a new order was added
    assert trader_page.verify_order_added(count_before), "No new order row added after placing order."

    # Step 5: Close all opening orders to clean up
    trader_page.close_all_open_orders()