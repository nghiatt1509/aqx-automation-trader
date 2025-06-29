import pyautogui

def get_screen_size():
    screen_width, screen_height = pyautogui.size()
    return screen_width, screen_height

def wait_for_page_load_successfully(page, state="networkidle", timeout=10000):
    """
    Wait for page to reach a load state. Log warning if it fails, don't throw.
    """
    try:
        page.wait_for_load_state(state=state, timeout=timeout)
    except Exception as e:
        print(f"[Warning]: Page may not have fully loaded. Reason: {e}")
