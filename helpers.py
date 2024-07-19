from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from configs import cfg

sphoto="https://graph.org/file/a60b8722ca747117a0e0b.png"

stxt="""👋 Hey {},\n\n➻ I Can Accept User Join Requests Automatically.\n➻ I Can Accept All Pending Requests.\n\n➻ Add Me To Your Chat And Make Admin With Invite Users Via Link Rights."""
skey=InlineKeyboardMarkup([[InlineKeyboardButton(f"➕ Add me to your Group ➕", url=f"https://t.me/{app.me.username}?startgroup=true&admin=invite_users+promote_members+delete_messages")],[InlineKeyboardButton(f"➕ Add me to your Channel ➕", url=f"https://t.me/{app.me.username}?startchannel=true&admin=post_messages+delete_messages+edit_messages+invite_users+promote_members"),],[InlineKeyboardButton("Help", callback_data="help"),InlineKeyboardButton("Updates", url=f"https://t.me/AnshuSigroha")],])

htxt="""Here Is My Help Menu\n\n<u><b>User Commands To Be Used In Groups And Pm</u></b>\n\n<blockquote>» /start : Starts The Bot.\n» /help : Showcase The Help Menu.\n» /info [id/username/reply]: Extract Information.\n» /id [username or reply]: Extract The Id.</blockquote>\n\n<b><u>Admin Commands To Be Used In Groups Or Channel</b></u>\n\n<blockquote>» /welcome [on/off]: To Enable/Disable Custom Welcome Message. This Is To Be Used In Groups Only.\n» /approveall : Approves All The Pending Requests. This Can Be Used In Groups And Channels.</blockquote>"""

bkey=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="back")]])
ckey=InlineKeyboardMarkup([[InlineKeyboardButton("Close", callback_data="close")]])
