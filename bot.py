import os
import requests as re
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", 12345))

API_HASH = os.environ.get("API_HASH", "")

app = Client(
        "webscrap",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
    )
    
    
@app.on_message(filters.command(['start']))
def start(client, message):
            message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n **Iam Simple web scraper** 🕸 \n __SEND ME WEBSITE LINK AND GET THAT WEB SOURCE__",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚡𝐎𝐖𝐍𝐄𝐑⚡" ,url="https://t.me/FILMWORLDOFFICIA") ],
                 [InlineKeyboardButton("♻𝐂𝐇𝐀𝐍𝐍𝐄𝐋♻", url="https://t.me/FILMWORLDOFFI") ]          ]        ) )


@app.on_message(filters.regex("^(http|https|www\.)"))
def start(client, message):
    ms = message.reply_text("```Trying to web scrap .........```", reply_to_message_id = message.message_id)
    msg_id = message.chat.id
    html_url = message.text
    try:
        page = re.get(html_url, timeout=10)
        if page.status_code != 200:
            message.reply_text("Invalid URL.")
            return
    except re.exceptions.Timeout:
        message.reply_text("Error: Request Timeout")
        return
    app.send_chat_action(chat_id=message.chat.id, action="typing")
    try:
        page_text = page.text
        app.send_message(chat_id=message.chat.id, text=page_text)
    except ValueError as ve:
        message.reply_text("Error: File Size Value Error")
    ms.delete()

app.run()
