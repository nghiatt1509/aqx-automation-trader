import os

# Timeout
DEFAULT_TIMEOUT = 10000  # 10 giây

# 🖥 Browser resolution
DEFAULT_VIEWPORT = {
    "width": 1920,
    "height": 1080
}

# URLs
LOGIN_URL = "https://aqxtrader.aquariux.com/web/login"
BASE_URL = "https://aqxtrader.aquariux.com/solutions/trader"

# Is executed on CI or local
IS_CI = os.getenv("CI") == "true"