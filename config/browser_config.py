import os
from dotenv import load_dotenv

load_dotenv()

Browser_config = {
    'default_browser': os.getenv('DEFAULT_BROWSER', 'chrome'),
    'headless': os.getenv('BROWSER_HEADLESS', 'true').lower() == 'true',
    'base_url': os.getenv('BASE_URL', 'https://ace-time.onrender.com/'),
}