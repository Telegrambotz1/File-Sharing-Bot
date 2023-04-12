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
            text = f"<b>○ Creator : <a href='https://t.me/SIRISH_123'>𝗦𝗜𝗥𝗜𝗦𝗛</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Channel : @BOSSHINDIOFFCIAL_DRAMAZ\n○ Support Group : @MOVIESREQUESTGROUPINDIA</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [   
                        InlineKeyboardButton("😇 𝗖𝗢𝗡𝗧𝗔𝗖𝗧",url= "https://t.me/SIRISH_123")
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
