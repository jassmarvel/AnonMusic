from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from TanuMusic import app
from config import BOT_USERNAME

start_txt = """
❖ ʜᴇʏ , ᴛʜᴇʀᴇ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ  ♥︎\n\n● ɪғ ʏᴏᴜ ᴡᴀɴᴛ Qᴜʙʏ ꭙ ᴍᴜsɪᴄ ♡゙゙, ʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏʟʟᴇᴄᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ˹ Qᴜʙʏ ᴍᴜsɪᴄ™ ♡゙"""




@app.on_message(filters.command("sojao"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/anonymous_botz"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://envs.sh/sQ-.gif")
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/sQm.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
  
