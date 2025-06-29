import os

class BasePage:
    def __init__(self, page):
        self.page = page

    def maximize_window(self):
        """Maximize browser on local (Not apply for CI run)"""
        if not os.getenv("CI"):
            try:
                import pyautogui
                screen_width, screen_height = pyautogui.size()
                self.page.set_viewport_size({"width": screen_width, "height": screen_height})
            except Exception as e:
                print(f"[!] Could not maximize window: {e}")
        else:
            print("[i] CI detected → skip maximize")