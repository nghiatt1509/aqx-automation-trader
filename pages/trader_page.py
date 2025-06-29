import allure
import time
from dotenv import load_dotenv

# Constants for trade page locators
ORDER_TYPE_DROPDOWNLIST = 'div[data-testid="trade-dropdown-order-type"]'
ORDER_SIZE = 'input[data-testid="trade-input-volume"]'
STOP_LOSS_PRICE_INPUT = 'input[data-testid="trade-input-stoploss-price"]'
TAKE_PROFIT_PRICE_INPUT = 'input[data-testid="trade-input-takeprofit-price"]'
STOP_LOSS_POINTS_INPUT = 'input[data-testid="trade-input-stoploss-points"]'
TAKE_PROFIT_POINTS_INPUT = 'input[data-testid="trade-input-takeprofit-points"]'
PLACE_BUY_ORDER_BUTTON = 'button[data-testid="trade-button-order"]'
TRADE_CONFIRMATION_BUTTON = 'button[data-testid="trade-confirmation-button-confirm"]'
ORDER_TABLE = 'table[data-testid="asset-open-table"]'
ORDER_ROWS = 'table[data-testid="asset-open-table"] tbody tr[data-testid="asset-open-list-item"]'
BULK_CLOSE_DROPDOWN_LIST = 'div[data-testid="bulk-close"]'
BULK_CLOSE_ALL_ITEM = 'div[data-testid="dropdown-bulk-close-all"]'
BULK_CLOSE_ALL_CONFIRM_BUTTON = 'button[data-testid="bulk-close-modal-button-submit-all"]'

class TraderPage:
    def __init__(self, page):
        """
        Initialize TradePage with a Playwright page instance.
        """
        self.page = page
        load_dotenv()  # Load environment variables from .env file (only once per session)

    @allure.step("Set Stop Loss Points to: {sl}")
    def set_stop_loss(self, sl: str):
        """
        Fill the Stop Loss points field.
        """
        self.page.fill(STOP_LOSS_POINTS_INPUT, sl)

    @allure.step("Set Take Profit Points to: {tp}")
    def set_take_profit(self, tp: str):
        """
        Fill the Take Profit points field.
        """
        self.page.fill(TAKE_PROFIT_POINTS_INPUT, tp)

    @allure.step("Set Order Size to: {size}")
    def set_order_size(self, size: str):
        """
        Fill the Order Size field.
        """
        self.page.fill(ORDER_SIZE, size)

    @allure.step("Place a Market Buy order with size={size}, SL={sl}, TP={tp}")
    def place_market_order_with_sl_tp(self, size: str = "0.05", sl: str = "", tp: str = ""):
        """
        Places a Market order by setting Order Size and optionally Stop Loss / Take Profit.

        Args:
            sl (str): Stop Loss in points (optional)
            tp (str): Take Profit in points (optional)
            size (str): Order size (default is "1")
        """
        # Step 1: Select order type as Market using dynamic dropdown selector
        self.select_dropdown_item(ORDER_TYPE_DROPDOWNLIST, "Market")

        # Step 2: Set order size
        self.set_order_size(size)

        # Step 3: Conditionally set Stop Loss and Take Profit if values are provided
        if sl:
            self.set_stop_loss(sl)
        if tp:
            self.set_take_profit(tp)

        # Step 4: Click the Buy Order button
        self.page.click(PLACE_BUY_ORDER_BUTTON)

        # Step 5: Wait for order confirmation and confirm
        self.page.wait_for_selector(TRADE_CONFIRMATION_BUTTON)
        self.page.click(TRADE_CONFIRMATION_BUTTON)
        time.sleep(10)  # Wait for the order to be processed

    @allure.step("Select '{value}' from dropdown: {dropdown_locator}")
    def select_dropdown_item(self, dropdown_locator: str, value: str):
        """
        Select an item from a dropdown list using dynamic locator.

        Args:
            dropdown_locator (str): The locator for the dropdown element
            value (str): The value to select (e.g. 'market', 'limit', 'stop')
        """
        self.page.click(dropdown_locator)
        item_locator = f"div[data-testid='trade-dropdown-order-type-{value.lower()}']"
        self.page.click(item_locator)

    @allure.step("Get current number of open orders")
    def get_open_order_count(self) -> int:
        """
        Returns the current number of open orders in the open orders table.
        """
        try:
            # Try waiting for the order row selector (with short timeout)
            self.page.wait_for_selector(ORDER_ROWS, timeout=3000)
            return len(self.page.locator(ORDER_ROWS).all())
        except:
            # If rows are not found within timeout, return 0
            return 0

    @allure.step("Verify new order record was added to the open order table")
    def verify_order_added(self, previous_count: int) -> bool:
        """
        Verifies a new order record appears in the open orders table.

        Args:
            previous_count (int): The number of rows before placing the order

        Returns:
            bool: True if a new row has been added, False otherwise.
        """
        self.page.wait_for_selector(ORDER_ROWS)
        rows = self.page.locator(ORDER_ROWS).all()
        return len(rows) > previous_count
    
    @allure.step("Close all open orders")
    def close_all_open_orders(self):
        """
        Closes all currently open orders via bulk close menu.
        Performs the following steps:
        1. Click the bulk close dropdown list
        2. Select the 'Close All' option
        3. Wait for and confirm the close-all confirmation dialog
        """
        # Step 1: Click to open the bulk close dropdown
        self.page.click(BULK_CLOSE_DROPDOWN_LIST)

        # Step 2: Wait for and select the "Close All" menu item
        self.page.wait_for_selector(BULK_CLOSE_ALL_ITEM)
        self.page.click(BULK_CLOSE_ALL_ITEM)

        # Step 3: Confirm the bulk close action
        self.page.wait_for_selector(BULK_CLOSE_ALL_CONFIRM_BUTTON)
        self.page.click(BULK_CLOSE_ALL_CONFIRM_BUTTON)

        time.sleep(5)  # Wait for the orders to be closed
        