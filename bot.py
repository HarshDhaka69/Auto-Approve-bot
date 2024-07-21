from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio, logging
from os import environ

logging.basicConfig(level=logging.INFO)

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

SESSION = environ.get("SESSION", "BAGyojMAjnLbu_1c9LwGqet0oaKPGvkuUsoen2NGJTtzWJetgn0U4wLdsYAjRDoyafE4IZsP5UaqtZxf__6fkh4hoVHkuZ-exl8hyC27K5w0k3fiUawYb6gH9ubz8Qaq29WESma6JYK4yYE7AaKEwy-e1liLZPD3he-6AXgDq7gp4p6qgVPGNVygSZOYV-8C7bMQbSEKnRfHcYFsEEF-rVWMBjJil8T4TXK8-Ar4f1MQ3zlwzGX4yMu_9LMEevmqMUIRNXwvH0R7nN9wqwVUjGeXfZBuN_8MXDJ46b6dQ8p739M3EUHe-AQj9hi0Cvmkw_gHZepZnH68xmSlfojbYNiT_xDWDQAAAAFnuV93AA")        
User = Client("AcceptUser", session_string=SESSION)

User.start()

photo="https://graph.org/file/a60b8722ca747117a0e0b.png"

stxt="""👋 Hey {},\n\n➻ I Can Accept User Join Requests Automatically.\n➻ I Can Accept All Pending Requests.\n\n➻ Add Me To Your Chat And Make Admin With Invite Users Via Link Rights."""
skey=InlineKeyboardMarkup([[InlineKeyboardButton(f"➕ Add me to your Group ➕", url=f"https://t.me/AutoAcceptMemberBot?startgroup=true&admin=invite_users+promote_members+delete_messages")],[InlineKeyboardButton(f"➕ Add me to your Channel ➕", url=f"https://t.me/AutoAcceptMemberBot?startchannel=true&admin=post_messages+delete_messages+edit_messages+invite_users+promote_members"),],[InlineKeyboardButton("Help", callback_data="help"),InlineKeyboardButton("Updates", url=f"https://t.me/AnshuSigroha")],])

htxt="""Here Is My Help Menu\n\n<u><b>User Commands To Be Used In Groups And Pm</u></b>\n\n<blockquote>» /start : Starts The Bot.\n» /help : Showcase The Help Menu.\n» /info [id/username/reply]: Extract Information.\n» /id [username or reply]: Extract The Id.</blockquote>\n\n<b><u>Admin Commands To Be Used In Groups Or Channel</b></u>\n\n<blockquote>» /welcome [on/off]: To Enable/Disable Custom Welcome Message. This Is To Be Used In Groups Only.\n» /approveall : Approves All The Pending Requests. This Can Be Used In Groups And Channels.</blockquote>"""

bkey=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="back")]])
ckey=InlineKeyboardMarkup([[InlineKeyboardButton("Close", callback_data="close")]])

gif = [
    'https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4',
    'https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4',
    'https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4',
    'https://telegra.ph/file/293cc10710e57530404f8.mp4',
    'https://telegra.ph/file/506898de518534ff68ba0.mp4',
    'https://telegra.ph/file/dae0156e5f48573f016da.mp4',
    'https://telegra.ph/file/3e2871e714f435d173b9e.mp4',
    'https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4',
    'https://telegra.ph/file/876edfcec678b64eac480.mp4',
    'https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4',
    'https://telegra.ph/file/b4834b434888de522fa49.mp4'
]


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        await app.send_video(kk.id,img, "**Hello {}!\nWelcome To {}\n\n__Bot By : AnshuSigroha".format(m.from_user.mention, m.chat.title))
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    
 
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("start"))
async def op(_, m :Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("➕ Add me to your Group ➕", url="https://t.me/AutoAcceptMemberBot?startgroup=true&admin=invite_users+promote_members+delete_messages")
                    ],[
                        InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/AutoAcceptMemberBot?startchannel=true&admin=post_messages+delete_messages+edit_messages+invite_users+promote_members")
                    ],[
                        InlineKeyboardButton("Help", callback_data="help"),
                        InlineKeyboardButton("Updates", url="https://t.me/AnshuSigroha")
                    ]
                ]
            )
            add_user(m.from_user.id)
            await m.reply_photo(
    "https://graph.org/file/a60b8722ca747117a0e0b.png",
    caption="👋 Hey {},\n\n➻ I Can Accept User Join Requests Automatically.\n\n➻ I Can Accept All Pending Requests.\n\n➻ Add Me To Your Chat And Make Admin With Invite Users Via Link Rights".format(m.from_user.mention),
    reply_markup=keyboard
)
        
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ Start Me In Private 💁‍♂️", url="https://t.me/AutoAceeptMemberBot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("{} Start Me In Private For More Info..".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Joined", "chk")
                ]
            ]
        )
        await m.reply_text("You must join @AnshuSigroha to use me.".format(cfg.FSUB), reply_markup=key)
        
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ approveall ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@User.on_message(filters.command("approveall") & filters.group & filters.channel)
async def approve_all(client, message):
    chat_id = message.chat.id
    
    # Delete the command message
    await message.delete()

    while True:
        try:
            # Get all pending join requests
            pending_requests = await client.get_chat_requests(chat_id)
            for request in pending_requests:
                await client(functions.messages.ApproveChatJoinRequestRequest(chat_id, request.user_id))
            await message.reply("All pending join requests have been approved!")
            break  # Exit the loop after successful approval

        except FloodWait as e:
            # Log the flood wait time and sleep for the duration
            logger.warning(f"FloodWait exception caught. Waiting for {e.seconds} seconds.")
            await asyncio.sleep(e.seconds)
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            await message.reply("An error occurred while processing the join requests.")
            break  # Exit the loop if there’s a non-recoverable error

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("➕ Add me to your Group ➕", url="https://t.me/AutoAcceptMemberBot?startgroup=true&admin=invite_users+promote_members+delete_messages")
                    ],[
                        InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/AutoAcceptMemberBot?startchannel=true&admin=post_messages+delete_messages+edit_messages+invite_users+promote_members")
                    ],[
                        InlineKeyboardButton("Help", callback_data="help"),
                        InlineKeyboardButton("Updates", url="https://t.me/AnshuSigroha")
                    ]
                ]
            )
            add_user(cb.from_user.id)
            await cb.message.edit("👋 Hey {},/n/n➻ I Can Accept User Join Requests Automatically./n/n➻ I Can Accept All Pending Requests./n/n➻ Add Me To Your Chat And Make Admin With Invite Users Via Link Rights".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard, disable_web_page_preview=True)
        print(cb.from_user.first_name +" Is started Your Bot!")
    except UserNotParticipant:
        await cb.answer("You must join @AnshuSigroha to use me.")

#Help
@app.on_callback_query(filters.regex("help"))
async def help(_, query: CallbackQuery):
    u = query.from_user.first_name
    b = app.me.first_name
    await query.edit_message_text(
        text=htxt,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Back", callback_data="back")]]
        )
    )

#Back
@app.on_callback_query(filters.regex("back"))
async def back(_, query: CallbackQuery):
    u = query.from_user.mention
    b = app.me.mention
    stxt="""👋 Hey {},\n\n➻ I Can Accept User Join Requests Automatically.\n➻ I Can Accept All Pending Requests.\n\n➻ Add Me To Your Chat And Make Admin With Invite Users Via Link Rights."""
    skey=InlineKeyboardMarkup([[InlineKeyboardButton(f"➕ Add me to your Group ➕", url=f"https://t.me/AutoAcceptMemberBot?startgroup=true&admin=invite_users+promote_members+delete_messages")],[InlineKeyboardButton(f"➕ Add me to your Channel ➕", url=f"https://t.me/AutoAcceptMemberBot?startchannel=true&admin=post_messages+delete_messages+edit_messages+invite_users+promote_members"),],[InlineKeyboardButton("Help", callback_data="help"),InlineKeyboardButton("Updates", url=f"https://t.me/AnshuSigroha")],]
                              )
    await query.edit_message_text(text=stxt, reply_markup=skey)

#Close
@app.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m: Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success += 1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated += 1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked += 1
        except Exception as e:
            print(e)
            failed += 1

    await lel.edit(f"✅ Successful to `{success}` users.\n❌ Failed to `{failed}` users.\n👾 Found `{blocked}` blocked users \n👻 Found `{deactivated}` deactivated users.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m: Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success += 1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated += 1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked += 1
        except Exception as e:
            print(e)
            failed += 1

    await lel.edit(f"✅ Successful to `{success}` users.\n❌ Failed to `{failed}` users.\n👾 Found `{blocked}` blocked users \n👻 Found `{deactivated}` deactivated users.")
    
print("I'm Alive Now!")
app.run()
