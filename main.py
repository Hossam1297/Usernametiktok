import random
import requests
import telebot
import threading
import time
import os

# ضع التوكن هنا أو من متغير بيئة
TOKEN = os.environ.get("BOT_TOKEN", "ضع_توكنك_هنا")
CHAT_ID = os.environ.get("CHAT_ID", "ضع_ايديك_هنا")

bot = telebot.TeleBot(TOKEN)

def check_usernames():
    rt = requests.session()
    litters = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    while True:
        user1 = ''.join(random.choice(litters) for _ in range(4))
        usernames = user1
        tiko = f'https://www.tiktok.com/@{usernames}?'

        hea = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
        }

        try:
            reqsnd = rt.get(tiko, headers=hea).status_code
            if reqsnd == 404:
                print(f'[+] {usernames} ✅ ')
                bot.send_message(CHAT_ID, f'𝙐𝙎𝙀𝙍: {usernames}\n𝘽𝙔: @AJSJ36')
            else:
                print(f'[+] {usernames} ❌ BAN ')
        except Exception as e:
            print(f'Error: {e}')
        time.sleep(1)

@bot.message_handler(commands=['start'])
def start_search(message):
    if str(message.chat.id) == str(CHAT_ID):
        bot.reply_to(message, "بدأ الفحص 🔍... راح أرسل أول اسم متاح إن شاء الله.")
        t = threading.Thread(target=check_usernames)
        t.start()
    else:
        bot.reply_to(message, "آسف، هذا البوت مخصص لصاحب الحساب فقط 🛡️")

print("البوت يعمل ✅")
bot.polling()