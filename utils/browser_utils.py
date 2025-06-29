import os

def get_screen_size():
    if os.getenv("CI"):
        # Headless mode: return default resolution
        return {"width": 1920, "height": 1080}
    else:
        try:
            import pyautogui
            width, height = pyautogui.size()
            return {"width": width, "height": height}
        except Exception:
            return {"width": 1366, "height": 768}

def wait_for_page_load_successfully(page, state="networkidle", timeout=10000):
    """
    Wait for page to reach a load state. Log warning if it fails, don't throw.
    """
    try:
        page.wait_for_load_state(state=state, timeout=timeout)
    except Exception as e:
        print(f"[Warning]: Page may not have fully loaded. Reason: {e}")
