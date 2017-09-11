import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

# Facebook config
fb_user_login = os.getenv('FACEBOOK_USER_LOGIN')
fb_user_password = os.getenv('FACEBOOK_USER_PASSWORD')

# Required configuration

em_data_dir = os.getenv('DATA_DIR')
em_database = os.getenv('DATABASE_FILE')