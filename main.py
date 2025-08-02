import requests
import time
import random

bot_token = '8399186679:AAH1ZtLHnfGFQZ4x1cxe3N_vnBXooYhVoMU'
chat_id = '8192424118'

last_update_id = None

def get_updates():
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    return response.json()

def send_message(text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, data=payload)

def generate_signal():
    crash = round(random.uniform(1.5, 3.0), 2)
    cashout = round(crash - random.uniform(0.1, 0.3), 2)
    return f"🎯 New Signal:\n💣 Crash Point: {crash}x\n📊 Cash Out at: {cashout}x"

# 📦 This is the part that handles your bot commands
while True:
    updates = get_updates()

    if "result" in updates:
        for update in updates["result"]:
            if last_update_id is None or update["update_id"] > last_update_id:
                last_update_id = update["update_id"]

                if "message" in update:
                    text = update["message"].get("text", "")
                    user_chat_id = update["message"]["chat"]["id"]

                    if str(user_chat_id) != chat_id:
                        continue  # ignore messages from other users (for now)

                    if text.lower() == "/start":
                        send_message("👋 Welcome to Aviator Bot!\n\nCommands:\n/signal - Get a new Aviator signal\n/help - See available commands")

                    elif text.lower() == "/help":
                        send_message("ℹ️ Available commands:\n/signal - Get a crash prediction\n/help - Show this menu again")

                    elif text.lower() == "/signal":
                        signal = generate_signal()
                        send_message(signal)
    time.sleep(3)
