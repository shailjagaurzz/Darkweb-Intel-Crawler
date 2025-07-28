import re
from bs4 import BeautifulSoup
from db import collection
import datetime

def detect_nsfw(email, password):
    # Placeholder for real NSFW detection logic
    return False

def insert_leak(email, password, source):
    leak = {
        "email": email,
        "password": password,
        "source": source,
        "is_nsfw": detect_nsfw(email, password),
        "timestamp": datetime.datetime.now()
    }
    collection.insert_one(leak)

def extract_leaks(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()

    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    password_pattern = r'(?i)password\s*[:=]\s*([^\s,]+)'
    phone_pattern = r'\b\d{10}\b'
    credit_card_pattern = r'\b(?:\d[ -]*?){13,16}\b'

    emails = re.findall(email_pattern, text)
    passwords = re.findall(password_pattern, text)
    phones = re.findall(phone_pattern, text)
    cards = re.findall(credit_card_pattern, text)

    return {
        'emails': list(set(emails)),
        'passwords': list(set(passwords)),
        'phones': list(set(phones)),
        'cards': list(set(cards))
    }
