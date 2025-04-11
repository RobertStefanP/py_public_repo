import requests


def send_telegram_message(message):            
    # Send to Telegram
    BOT_TOKEN = '??'
    CHAT_ID = '??'
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=payload)
