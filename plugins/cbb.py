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
    elif data == "con":
        await query.message.edit_text(
            text = f"""
       ┍━━━━━»•» 𝗥𝗨𝗟𝗘𝗦 🌺 «•«━┑

˚₊· ͟͟͞͞➳❥ 𝗬𝗢𝗨𝗥 𝗗𝗔𝗧𝗔 𝗜𝗦 𝗕𝗘𝗘𝗡 𝗖𝗢𝗟𝗟𝗘𝗖𝗧𝗘𝗗
˚₊· ͟͟͞͞➳❥ 𝗗𝗢𝗡𝗧 𝗦𝗣𝗔𝗠 𝗧𝗛𝗘 𝗕𝗢𝗧
˚₊· ͟͟͞͞➳❥ 𝗗𝗢𝗡𝗧 𝗕𝗟𝗢𝗖𝗞 𝗧𝗛𝗘 𝗕𝗢𝗧           
˚₊· ͟͟͞͞➳❥ 𝗝𝗨𝗦𝗧 𝗥𝗘𝗤𝗨𝗘𝗦𝗧 𝗗𝗥𝗔𝗠𝗔𝗦 𝗗𝗜𝗥𝗘𝗖𝗧𝗟𝗬         
˚₊· ͟͟͞͞➳❥ 𝗥𝗘𝗣𝗢𝗦𝗧𝗜𝗡𝗚 𝗧𝗛𝗘 𝗙𝗜𝗟𝗘𝗦 𝗜𝗦 𝗔 𝗖𝗥𝗜𝗠𝗘
˚₊· ͟͟͞͞➳❥ 𝗗𝗢𝗡𝗧 𝗖𝗢𝗣𝗬 𝗔𝗡𝗗 𝗣𝗔𝗦𝗧𝗘
˚₊· ͟͟͞͞➳❥ 𝗝𝗨𝗦𝗧 𝗦𝗛𝗔𝗥𝗘 𝗧𝗛𝗘 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗟𝗜𝗡𝗞 𝗔𝗡𝗗 𝗦𝗨𝗣𝗣𝗢𝗥𝗧
˚₊· ͟͟͞͞➳❥ 𝗜𝗧𝗦 𝗙𝗢𝗥𝗖𝗘𝗦 𝗦𝗨𝗕 𝗦𝗢 𝗗𝗢𝗡𝗧 𝗟𝗘𝗔𝗩𝗘 𝗧𝗛𝗥 𝗠𝗔𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟
˚₊· ͟͟͞͞➳❥ 𝗜𝗙 𝗬𝗢𝗨 𝗗𝗢 𝗬𝗢𝗨 𝗪𝗜𝗟𝗟.𝗕𝗘 𝗕𝗟𝗢𝗖𝗞𝗘𝗗 𝗙𝗢𝗥 𝗘𝗩𝗘𝗥
˚₊· ͟͟͞͞➳❥ 𝗗𝗢𝗡𝗧 𝗩𝗜𝗢𝗟𝗔𝗧𝗘 𝗧𝗛𝗘 𝗥𝗨𝗟𝗘𝗦 𝗘𝗡𝗝𝗢𝗬 :𝗗

 ┕━»•» 🌺 𝗘𝗡𝗗 «•«━━━━━┙""",
       reply_markup = InlineKeyboardMarkup(
                [
                    [   
                        InlineKeyboardButton("😇 𝗖𝗢𝗡𝗧𝗔𝗖𝗧",url= "https://t.me/SIRISH_123"),
                        InlineKeyboardButton("🔒 𝗖𝗟𝗢𝗦𝗘", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "dcma":
        await query.message.edit_text(
            text = """
𝗪𝗛𝗔𝗧 𝗜𝗦 𝗔 𝗗𝗖𝗠𝗔 ?

 Digital Millennium Copyright Act is a international act which says that a
 person know or unknow violents the hard wrok of someone it is against the
 rules of telegram so any kind of copyright violation is leads to permanent
 ban from telegram to protect the prior privacy telegram 2023 
 
 𝗛𝗢𝗪 𝗜𝗧 𝗪𝗢𝗥𝗞𝗦 ?
 
 if you think we miss used our power and copied your work
 and didn't give the credit and you think we going against law pls
 report it the owners we will remove the content right away from the 
 channel pls reporting is not a very good option we will surely respond
 if we are late we reply to all messages we are following law and not
 violating and of the main telegram rules
 
 report here @tufail505 && @SIRISH_123  thanks enjoy """
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

