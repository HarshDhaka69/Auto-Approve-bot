from bot import app
from pyrogram.types import CallbackQuery
from pyrogram import filters

from bot.utils.helpers import htxt, stxt, bkey, skey
from bot.utils.database import welcomes

from Abg.chat_status import adminsOnly
#Help
@app.on_callback_query(filters.regex("help"))
async def help(app, query: CallbackQuery):
    u = query.from_user.first_name
    b = app.me.first_name
    await query.edit_message_text(text=htxt.format(u,b,b), reply_markup=bkey)

#Back
@app.on_callback_query(filters.regex("back"))
async def back(app, query: CallbackQuery):
    u = query.from_user.mention
    b = app.me.mention
    await query.edit_message_text(text=stxt.format(u,b,b), reply_markup=skey)

#Close
@app.on_callback_query(filters.regex("close"))
async def close(app, query: CallbackQuery):
    await query.message.delete()
