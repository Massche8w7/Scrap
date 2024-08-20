import asyncio
import json
import requests
import random
import time
import aiogram
import os
from faker import Faker
from aiogram.types import InputFile
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keep_alive import live
import multiprocessing
from telegraph import Telegraph

fake = Faker()

emojis = ["🐉"]

telegraph = Telegraph()
telegraph.create_account(short_name="Maria")


PROXIE = "prox-eg.pointtoserver.com:10799:purevpn0s13830845:6phsLWXBQEq4MR"  # Your Proxie
TOKEN = "7428987544:AAFFUX4u0lq4JqH_W9_-B3NJQu1oh_Kc7J4"  # Your BotToken
CHAT_ID = -1002237348547  # Your ChatID


async def send_messages():
    CONTADOR = 0
    bot = aiogram.Bot(token=TOKEN)
    chat_id = CHAT_ID

    with open("cards.txt") as file:
        lines = file.readlines()

    requests_limit = 1
    pause_duration = 50

    image_files = os.listdir("imagenes")
    for i, line in enumerate(lines, start=1):
        linea = line[:28]
        card_number = line[:12]
        month = str(random.randint(1, 12)).zfill(2)
        year = str(random.randint(23, 29)).zfill(2)
        cvv = str(random.randint(100, 999)).zfill(3)

        url3 = "https://testgen.alwaysdata.net/gen.php"
        params3 = {"lista": linea}
        Gen3 = requests.get(url3, params=params3, proxies=PROXIE)

        año1 = random.randint(2024, 2030)
        extr_a1 = random.randrange(100, 950, 3)
        mes_1 = random.choice(
            ("01", "02", "03", "04", "05", "06", "07", "09", "09", "10", "11", "12")
        )
        año_1 = random.randint(2024, 2031)
        extr_a2 = random.randrange(100, 950, 3)
        mes_2 = random.choice(
            ("01", "02", "03", "04", "05", "06", "07", "09", "09", "10", "11", "12")
        )
        año_2 = random.randint(2024, 2031)
        extr_a3 = random.randrange(100, 950, 3)
        mes_3 = random.choice(
            ("01", "02", "03", "04", "05", "06", "07", "09", "09", "10", "11", "12")
        )
        año_3 = random.randint(2024, 2031)
        extr_a4 = random.randrange(100, 950, 3)
        mes_4 = random.choice(
            ("01", "02", "03", "04", "05", "06", "07", "09", "09", "10", "11", "12")
        )
        año_4 = random.randint(2024, 2031)
        extr_a5 = random.randrange(100, 950, 3)
        mes_5 = random.choice(
            ("01", "02", "03", "04", "05", "06", "07", "09", "09", "10", "11", "12")
        )
        año_5 = random.randint(2024, 2031)
        extr_a6 = random.randrange(100, 950, 3)
        mes_6 = random.choice(
            ("01", "02", "03", "04", "05", "06", "07", "09", "09", "10", "11", "12")
        )
        año_6 = random.randint(2024, 2031)
        extr_a7 = random.randrange(100, 950, 3)
        mes_7 = random.choice(
            ("01", "02", "03", "04", "05", "06", "07", "09", "09", "10", "11", "12")
        )
        año_7 = random.randint(2024, 2031)
        extr_a8 = random.randrange(100, 950, 3)
        mes_8 = random.choice(
            ("01", "02", "03", "04", "05", "06", "07", "09", "09", "10", "11", "12")
        )
        año_8 = random.randint(2024, 2031)
        extr_a9 = random.randrange(100, 950, 3)
        mes_9 = random.choice(
            ("01", "02", "03", "04", "05", "06", "07", "09", "09", "10", "11", "12")
        )
        año_9 = random.randint(2024, 2031)
        extr_a10 = random.randrange(100, 950, 3)
        mes_10 = random.choice(
            ("01", "02", "03", "04", "05", "06", "07", "09", "09", "10", "11", "12")
        )
        año_10 = random.randint(2024, 2031)

        mes1 = random.choice(
            ("01", "02", "03", "04", "05", "06", "07", "09", "09", "10", "11", "12")
        )
        extra = random.randrange(100, 950, 3)
        extm = random.randrange(10, 90, 2)
        extm2 = random.randrange(10, 90, 2)
        extm3 = random.randrange(1, 9, 1)

        BIN = card_number[:6]
        req = requests.get(
            url=f"https://bins.antipublic.cc/bins/{BIN}", proxies=PROXIE
        ).json()

        try:
            brand = req["brand"]
        except KeyError:
            print(
                "La clave 'brand' no está presente en la respuesta JSON. Se omitirá esta entrada."
            )
            continue

        bin = req["bin"]
        country = req["country"]
        country_name = req["country_name"]
        country_flag = req["country_flag"]
        country_currencies = req["country_currencies"]
        bank = req["bank"]
        level = req["level"]
        typea = req["type"]
        xountry = country
        api = requests.get(
            url=f"https://randomuser.me/api/?nat={xountry}&inc=name,location",
            proxies=PROXIE,
        ).json()
        name = api["results"][0]["name"]["first"]
        lastname = api["results"][0]["name"]["last"]
        street = api["results"][0]["location"]["street"]["name"]
        complement = api["results"][0]["location"]["street"]["number"]
        city = api["results"][0]["location"]["city"]
        state = api["results"][0]["location"]["state"]
        countri = api["results"][0]["location"]["country"]
        postcode = api["results"][0]["location"]["postcode"]

        full_name = fake.name()
        address = fake.address()

        random_emoji = random.choice(emojis)

        random_image = random.choice(image_files)
        image_path = os.path.join("imagenes", random_image)
        photo = InputFile(image_path)

        cc = Gen3.text.replace("", "")
        ccs = cc.split("|")
        cnum = ccs[0]
        extra = f"{cnum[:12]}xxxx|{ccs[1]}|{ccs[2]}|rnd"
        message = f"<b>𝐁𝐞𝐫𝐬𝐞𝐫𝐤 𝐒𝐜𝐫𝐚𝐩𝐩𝐞𝐫 🕷</b>\n\n"
        message += f"{bin} - <b>[#" + f"{CONTADOR}]</b>\n"
        message += f"ア 𝐂𝐂 -» <code>{cc}</code>\n"
        message += f"キ 𝘽𝙞𝙣 -» <code>{brand} - {typea} - {level}</code>\n"
        message += f"朱 𝘽𝙖𝙣𝙠 -» <code>{bank}</code>\n"
        message += f"零 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 -» <code>{country_name} {country_flag}</code>\n\n"
        message += f"カ 𝗘𝘅𝘁𝗿𝗮 ↓\n"
        message += f"<code>{extra}</code>\n\n"
        message += f" 𝐎𝐰𝐧𝐞𝐫 -» <a href='https://t.me/MLXML9'>@MLXML9</a>"

        try:
            await bot.send_photo(chat_id, photo, caption=message, parse_mode="HTML")
            CONTADOR += 1
        except Exception as e:
            print(f"Error al enviar el mensaje: {e}")

        if i % requests_limit == 0 and i != len(lines):
            print(f"𝐍𝐞𝐰 𝐂𝐫𝐞𝐝𝐢𝐭 𝐂𝐚𝐫𝐝 ! {Gen3.text.replace('', '')} #{CONTADOR}")
            time.sleep(pause_duration)


def run_bot():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_messages())


def heartbeat():
    while True:
        print("Dp Heart - Bot in Ejecution")
        time.sleep(300)


def main():
    while True:
        bot_process = multiprocessing.Process(target=run_bot)
        heartbeat_process = multiprocessing.Process(target=heartbeat)

        bot_process.start()
        heartbeat_process.start()

        bot_process.join()
        heartbeat_process.join()
        print("Reiniciando procesos...")


if __name__ == "__main__":
    main()
