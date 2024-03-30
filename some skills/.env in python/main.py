"""
    Create At 2024/3/29
    At:21:58 PM
"""
import os
from dotenv import load_dotenv


load_dotenv('.env')

username = os.getenv('USER')
password = os.getenv('PASSWORD')
print(username, password)
