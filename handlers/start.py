from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import BOT_USERNAME, SUPPORT_GROUP, UPDATE_CHANNEL, START_IMAGE, OWNER_ID
import db


def register_handlers(app: Client):

    # ==========================================================
    # Start Menu
    # ==========================================================
    async def send_start_menu(message, user):
        text = f"""
✨ ʜᴇʏ {user}! ✨  

ɪ’ᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴀɪ ʙᴏᴛ ⚙️  
ᴅᴇsɪɢɴᴇᴅ ᴛᴏ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀᴛ ᴄʟᴇᴀɴ, sᴀꜰᴇ, ᴀɴᴅ ᴏʀɢᴀɴɪᴢᴇᴅ.

⚡ ᴡʜᴀᴛ ɪ ᴄᴀɴ ᴅᴏ:
• ᴅᴇᴛᴇᴄᴛ ᴀɴᴅ ʙʟᴏᴄᴋ sᴘᴀᴍ ɪɴ ʀᴇᴀʟ-ᴛɪᴍᴇ  
• ᴀᴜᴛᴏᴍᴀᴛᴇ ᴡᴇʟᴄᴏᴍᴇs, ᴍᴜᴛᴇs, ᴀɴᴅ ʟᴏᴄᴋs  
• sᴍᴀʀᴛ ᴄᴏɴᴛʀᴏʟs ғᴏʀ ʟɪɴᴋs, ᴍᴇᴅɪᴀ, ᴀɴᴅ ᴜsᴇʀs  
• sʟᴇᴇᴋ ɪɴʟɪɴᴇ ᴍᴇɴᴜs ᴛᴏ ᴍᴀᴋᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴇᴀsʏ
"""

        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [
                InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇs", url=UPDATE_CHANNEL),
                InlineKeyboardButton("💬 sᴜᴘᴘᴏʀᴛ", url=SUPPORT_GROUP),
            ],
            [
                InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", user_id=OWNER_ID)
            ],
            [InlineKeyboardButton("📖 ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs", callback_data="help")]
        ])

        if message.text:
            await message.reply_photo(START_IMAGE, caption=text, reply_markup=buttons)
        else:
            media = InputMediaPhoto(media=START_IMAGE, caption=text)
            await message.edit_media(media=media, reply_markup=buttons)

    # ==========================================================
    # /start Command
    # ==========================================================
    @app.on_message(filters.private & filters.command("start"))
    async def start_command(client, message):
        user = message.from_user
        await db.add_user(user.id, user.first_name)
        await send_start_menu(message, user.first_name)

    # ==========================================================
    # Help Menu
    # ==========================================================
    async def send_help_menu(message):
        text = """
✨ ʜᴇʟᴘ ᴍᴇɴᴜ ✨

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ!  
ᴄʜᴏᴏsᴇ ᴀ ᴄᴀᴛᴇɢᴏʀʏ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ.

───────────────
💬 ɢʀᴇᴇᴛɪɴɢs — ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇs  
🔒 ʟᴏᴄᴋs — ᴜʀʟ, ᴍᴇᴅɪᴀ, ʟᴀɴɢᴜᴀɢᴇ ᴄᴏɴᴛʀᴏʟ  
⚙️ ᴍᴏᴅᴇʀᴀᴛɪᴏɴ — ᴍᴀɴᴀɢᴇ ᴜsᴇʀs ᴇᴀsɪʟʏ
───────────────

ᴛᴀᴘ ᴀ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ sᴇᴇ ᴅᴇᴛᴀɪʟᴇᴅ ᴄᴏᴍᴍᴀɴᴅs ↓
"""
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("💬 ɢʀᴇᴇᴛɪɴɢs", callback_data="greetings"),
                InlineKeyboardButton("🔒 ʟᴏᴄᴋs", callback_data="locks"),
            ],
            [InlineKeyboardButton("⚙️ ᴍᴏᴅᴇʀᴀᴛɪᴏɴ", callback_data="moderation")],
            [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="back_to_start")]
        ])

        media = InputMediaPhoto(media=START_IMAGE, caption=text)
        await message.edit_media(media=media, reply_markup=buttons)

    # ==========================================================
    # Help Callback
    # ==========================================================
    @app.on_callback_query(filters.regex("help"))
    async def help_callback(client, callback_query):
        await send_help_menu(callback_query.message)
        await callback_query.answer()

    # ==========================================================
    # Back to Start
    # ==========================================================
    @app.on_callback_query(filters.regex("back_to_start"))
    async def back_to_start_callback(client, callback_query):
        user = callback_query.from_user.first_name
        await send_start_menu(callback_query.message, user)
        await callback_query.answer()

    # ==========================================================
    # Greetings Callback
    # ==========================================================
    @app.on_callback_query(filters.regex("greetings"))
    async def greetings_callback(client, callback_query):
        text = """
💬 ᴡᴇʟᴄᴏᴍᴇ sʏsᴛᴇᴍ

🎯 ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ’s ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇs:

/setwelcome <text> — sᴇᴛ ᴀ ᴄᴜsᴛᴏᴍ ᴡᴇʟᴄᴏᴍᴇ  
/welcome on — ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇs  
/welcome off — ᴅɪsᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇs

✨ ᴘʟᴀᴄᴇʜᴏʟᴅᴇʀs:
{username}, {first_name}, {id}, {mention}
"""
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")]
        ])
        media = InputMediaPhoto(media=START_IMAGE, caption=text)
        await callback_query.message.edit_media(media=media, reply_markup=buttons)
        await callback_query.answer()

    # ==========================================================
    # Locks Callback
    # ==========================================================
    @app.on_callback_query(filters.regex("locks"))
    async def locks_callback(client, callback_query):
        text = """
🔒 ʟᴏᴄᴋ sʏsᴛᴇᴍ

/lock <type> — ᴇɴᴀʙʟᴇ ᴀ ʟᴏᴄᴋ  
/unlock <type> — ᴅɪsᴀʙʟᴇ ᴀ ʟᴏᴄᴋ  
/locks — ᴠɪᴇᴡ ᴀᴄᴛɪᴠᴇ ʟᴏᴄᴋs

🔹 ᴛʏᴘᴇs ᴏғ ʟᴏᴄᴋs:
url | sticker | media | username | language
"""
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")]
        ])
        media = InputMediaPhoto(media=START_IMAGE, caption=text)
        await callback_query.message.edit_media(media=media, reply_markup=buttons)
        await callback_query.answer()

    # ==========================================================
    # Moderation Callback
    # ==========================================================
    @app.on_callback_query(filters.regex("moderation"))
    async def moderation_callback(client, callback_query):
        try:
            text = """
⚙️ ᴍᴏᴅᴇʀᴀᴛɪᴏɴ ᴛᴏᴏʟs

/kick <user> — ʀᴇᴍᴏᴠᴇ ᴀ ᴍᴇᴍʙᴇʀ  
/ban <user> — ʙᴀɴ ᴘᴇʀᴍᴀɴᴇɴᴛʟʏ  
/unban <user> — ᴜɴʙᴀɴ ᴀ ᴜsᴇʀ  
/mute <user> — ᴍᴜᴛᴇ ᴛʜᴇ ᴜsᴇʀ  
/unmute <user> — ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴜsᴇʀ  
/warn <user> — ᴀᴅᴅ ᴀ ᴡᴀʀɴɪɴɢ  
/warns <user> — ᴄʜᴇᴄᴋ ᴡᴀʀɴs  
/resetwarns <user> — ᴄʟᴇᴀʀ ᴀʟʟ  
/promote <user> — ᴍᴀᴋᴇ ᴀᴅᴍɪɴ  
/demote <user> — ʀᴇᴍᴏᴠᴇ ᴀᴅᴍɪɴ

💡 Example:
Reply to a user or type  
/ban @username
"""
            buttons = InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")]
            ])
            media = InputMediaPhoto(media=START_IMAGE, caption=text)
            await callback_query.message.edit_media(media=media, reply_markup=buttons)
            await callback_query.answer()

        except Exception as e:
            print(f"Error in moderation_callback: {e}")
            await callback_query.answer("❌ Something went wrong.", show_alert=True)

    # ==========================================================
    # Broadcast
    # ==========================================================
    @app.on_message(filters.private & filters.command("broadcast"))
    async def broadcast_message(client, message):
        if message.from_user.id != OWNER_ID:
            return await message.reply_text("❌ Only the bot owner can use this command.")

        if not message.reply_to_message:
            return await message.reply_text("⚠️ Please reply to a message to broadcast it.")

        text_to_send = message.reply_to_message.text or message.reply_to_message.caption
        if not text_to_send:
            return await message.reply_text("⚠️ The replied message has no text to send.")

        users = await db.get_all_users()
        sent, failed = 0, 0
        await message.reply_text(f"📡 Broadcasting to {len(users)} users...")

        for user_id in users:
            try:
                await client.send_message(user_id, text_to_send)
                sent += 1
            except Exception:
                failed += 1

        await message.reply_text(f"✅ Broadcast completed!\n\nSent: {sent}\nFailed: {failed}")

    # ==========================================================
    # Stats
    # ==========================================================
    @app.on_message(filters.private & filters.command("stats"))
    async def stats_command(client, message):
        if message.from_user.id != OWNER_ID:
            return await message.reply_text("❌ Only the bot owner can use this command.")
        users = await db.get_all_users()
        await message.reply_text(f"📊 Total registered users: {len(users)}")