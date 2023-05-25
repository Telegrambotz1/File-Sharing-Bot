#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"""<b>\n
            
╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸🤖 𝙈𝙔 𝙉𝘼𝙈𝙀 : <a href='https://t.me/FILE_STOREINDIA_BOT'>𝗥𝗢𝗦𝗬</a>
│
├🔸📝 𝗟𝗔𝗡𝗚𝗨𝗔𝗚𝗘 : <a href='https://www.python.org'>𝗣𝗬𝗧𝗛𝗢𝗡 3</a>
│
├🔹📚 𝗟𝗜𝗕𝗥𝗔𝗥𝗬 : <a href='https://docs.pyrogram.org'>𝗣𝗥𝗢𝗚𝗥𝗔𝗠</a>
│
├🔹📡 𝗛𝗢𝗦𝗧𝗘𝗗 𝗢𝗡 : <a href='https://fly.io'>𝗙𝗟𝗬.𝗜𝗢</a>
│
├🔸👨‍💻 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : <a href='https://t.me/SIRISH_123'>𝗦𝗜𝗥𝗜𝗦𝗛</a>
│
├🔹👥 𝗕𝗢𝗧 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 : <a href='https://t.me/KDRAMSREQUEST'>𝗝𝗢𝗜𝗡 𝗡𝗢𝗪</a>
│
├🔸🔔 𝗕𝗢𝗧 𝗨𝗣𝗗𝗔𝗧𝗘𝗦 : <a href='https://t.me/k_Drama_Hindi_Dubbed_avl'>𝗝𝗢𝗜𝗡 𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a>
│
╰──────[ 😎 ]───────────⍟<b>""",

            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [   
                        InlineKeyboardButton("😇 𝗖𝗢𝗡𝗧𝗔𝗖𝗧",url= "https://t.me/SIRISH_123"),
                        InlineKeyboardButton("🔒 𝗖𝗟𝗢𝗦𝗘", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
