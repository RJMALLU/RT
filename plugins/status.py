import random
import re, asyncio, time, shutil, psutil, os, sys
from pyrogram import Client, filters, enums
from pyrogram.types import *
from info import BOT_UPTIME as BOT_START_TIME
from utils import humanbytes  


@Client.on_message(filters.command("status"))          
async def stats(bot, update):
    currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - BOT_START_TIME))
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    ms_g = f"""<b>⚙️ 𝖡𝗈𝗍 𝖲𝗍𝖺𝗍𝗎𝗌</b>

🕔 𝖴𝗉𝗍𝗂𝗆𝖾: <code>{currentTime}</code>
🛠 𝖢𝖯𝖴 𝖴𝗌𝖺𝗀𝖾: <code>{cpu_usage}%</code>
🗜 𝖱𝖠𝖬 𝖴𝗌𝖺𝗀𝖾: <code>{ram_usage}%</code>
🗂 𝖳𝗈𝗍𝖺𝗅 𝖣𝗂𝗌𝗄 𝖲𝗉𝖺𝖼𝖾: <code>{total}</code>
🗳 𝖴𝗌𝖾𝖽 𝖲𝗉𝖺𝖼𝖾: <code>{used} ({disk_usage}%)</code>
📝 𝖥𝗋𝖾𝖾 𝖲𝗉𝖺𝖼𝖾: <code>{free}</code> """

    msg = await bot.send_message(chat_id=update.chat.id, text="__𝖯𝗋𝗈𝖼𝖾𝗌𝗌𝗂𝗇𝗀...__", parse_mode=enums.ParseMode.MARKDOWN)         
    await msg.edit_text(text=ms_g, parse_mode=enums.ParseMode.HTML)
