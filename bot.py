import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
INPUT_FILE = os.getenv('INPUT_FILE', 'message.txt')


def load_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def send_message(token, chat_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    requests.post(url, data={'chat_id': chat_id, 'text': text})


if __name__ == '__main__':
    message = load_text(INPUT_FILE)
    send_message(TOKEN, CHAT_ID, message)
