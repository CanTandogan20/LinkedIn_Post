import os
from dotenv import load_dotenv

load_dotenv()

def get_linkedin_token():
    return os.getenv('LINKEDIN_ACCESS_TOKEN')
