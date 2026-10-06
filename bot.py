import os
import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ==================================================
#                    CONFIG
# ==================================================
# Security:
# Set BOT_TOKEN and ADMIN_ID as environment variables.
TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

START_IMAGE = "https://i.postimg.cc/MKWZn3Lv/IMG-20260521-163611-172.jpg"
PREMIUM_IMAGE = "https://i.postimg.cc/x89kTfHG/IMG-20260521-164434-789.jpg"

QR_99 = "https://i.postimg.cc/qvWDb4CW/IMG-20261007-013133-731.jpg"
QR_149 = "https://i.postimg.cc/rmfSHNPL/IMG-20261007-013340-805.jpg"
QR_249 = "https://i.postimg.cc/zfjWLk5x/IMG-20261007-013503-174.jpg"
QR_499 = "https://i.postimg.cc/d137hP4b/IMG-20261007-013542-616.jpg"

# Admin contact link
ADMIN_USERNAME = "https://t.me/dealer_x"

DEMO_CHANNEL = "https://t.me/demochannlink"
INFO_CHANNEL = "https://t.me/howtogetpre"

# ==================================================
#                    LOGGING
# ==================================================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ==================================================
#                    STATS
# ==================================================
users = set()

plan_99 = 0
plan_149 = 0
plan_249 = 0
plan_499 = 0


# ==================================================
#                  HOME BUTTONS
# ==================================================
def home_buttons():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "💎 𝐆𝐄𝐓 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 💎",
                callback_data="premium",
            )
        ],
        [
            InlineKeyboardButton("🎬 𝐃𝐄𝐌𝐎", url=DEMO_CHANNEL),
            InlineKeyboardButton("📖 𝐇𝐎𝐖 𝐓𝐎", url=INFO_CHANNEL),
        ],
    ])


# ==================================================
#                    START
# ==================================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user:
        users.add(update.effective_user.id)

    caption = (
        "<b>🔥 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐂𝐎𝐋𝐋𝐄𝐂𝐓𝐈𝐎𝐍 🔥</b>\n\n"
        "<b>🎬 𝟓𝟎𝟎𝟎+ 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐂𝐎𝐍𝐓𝐄𝐍𝐓</b>\n\n"
        "<b>📦 𝟏𝟎𝟎+ 𝐕𝐈𝐏 𝐂𝐎𝐋𝐋𝐄𝐂𝐓𝐈𝐎𝐍𝐒</b>\n\n"
        "<b>⚡ 𝐈𝐍𝐒𝐓𝐀𝐍𝐓 𝐀𝐂𝐂𝐄𝐒𝐒</b>\n\n"
        "<b>👇 𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 👇</b>"
    )

    await update.message.reply_photo(
        photo=START_IMAGE,
        caption=caption,
        parse_mode="HTML",
        reply_markup=home_buttons(),
    )


# ==================================================
#                 PREMIUM MENU
# ==================================================
async def premium_menu(query):
    keyboard = [
        [InlineKeyboardButton("💎 𝐌𝐌𝐒 𝐕𝐈𝐃𝐄𝐎 — ₹99", callback_data="p1")],
        [InlineKeyboardButton("🔥 𝐂𝐏 𝐕𝐢𝐝𝐞𝐨 — ₹149", callback_data="p2")],
        [InlineKeyboardButton("📦 𝐀𝐥𝐥 𝐈𝐧 𝐎𝐧𝐞 — ₹249", callback_data="p3")],
        [InlineKeyboardButton("👑 𝐕𝐈𝐏 𝐀𝐥𝐥 ( 𝟏𝟎𝟎+ 𝐆𝐫𝐨𝐮𝐩) — ₹499", callback_data="p4")],
        [InlineKeyboardButton("⬅️ 𝐁𝐀𝐂𝐊", callback_data="home")],
    ]

    await query.message.edit_media(
        media=InputMediaPhoto(
            media=PREMIUM_IMAGE,
            caption=(
                "<b>💎 𝐒𝐄𝐋𝐄𝐂𝐓 𝐘𝐎𝐔𝐑 𝐏𝐋𝐀𝐍 💎</b>\n\n"
                "👇 <b>Choose a plan below</b>"
            ),
            parse_mode="HTML",
        ),
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# ==================================================
#                    HOME PAGE
# ==================================================
async def home_page(query):
    caption = (
        "<b>🔥 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐂𝐎𝐋𝐋𝐄𝐂𝐓𝐈𝐎𝐍 🔥</b>\n\n"
        "<b>🎬 𝟓𝟎𝟎𝟎+ 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐂𝐎𝐍𝐓𝐄𝐍𝐓</b>\n\n"
        "<b>📦 𝟏𝟎𝟎+ 𝐕𝐈𝐏 𝐂𝐎𝐋𝐋𝐄𝐂𝐓𝐈𝐎𝐍𝐒</b>\n\n"
        "<b>⚡ 𝐈𝐍𝐒𝐓𝐀𝐍𝐓 𝐀𝐂𝐂𝐄𝐒𝐒</b>\n\n"
        "<b>👇 𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 👇</b>"
    )

    await query.message.edit_media(
        media=InputMediaPhoto(
            media=START_IMAGE,
            caption=caption,
            parse_mode="HTML",
        ),
        reply_markup=home_buttons(),
    )


# ==================================================
#                    QR PAGE
# ==================================================
async def qr_page(query, qr_image, amount):
    keyboard = [
        [
            InlineKeyboardButton(
                f"💳 𝐏𝐀𝐘 ₹{amount}",
                url=qr_image,
            )
        ],
        [
            InlineKeyboardButton(
                "✅ 𝐈 𝐇𝐀𝐕𝐄 𝐏𝐀𝐈𝐃",
                callback_data=f"paid_{amount}",
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ 𝐁𝐀𝐂𝐊",
                callback_data="back_to_plans",
            )
        ],
    ]

    await query.message.edit_media(
        media=InputMediaPhoto(
            media=qr_image,
            caption=(
                f"<b>💳 𝐏𝐀𝐘𝐌𝐄𝐍𝐓 — ₹{amount}</b>\n\n"
                "1️⃣ QR को scan karke payment karein.\n"
                "2️⃣ Payment complete hone ke baad "
                "<b>✅ I HAVE PAID</b> dabayein.\n"
                "3️⃣ Uske baad isi chat mein <b>payment screenshot</b> "
                "photo ke roop mein bhejein.\n\n"
                "⚠️ <b>Payment verification admin karega.</b>"
            ),
            parse_mode="HTML",
        ),
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# ==================================================
#              PAYMENT SCREENSHOT FLOW
# ==================================================
async def paid_page(query, amount):
    # Store the amount for the next screenshot message.
    user_id = query.from_user.id
    query.message.bot_data.setdefault("pending_payments", {})
    query.message.bot_data["pending_payments"][user_id] = amount

    keyboard = [
        [
            InlineKeyboardButton(
                "📩 𝐒𝐄𝐍𝐃 𝐒𝐂𝐑𝐄𝐄𝐍𝐒𝐇𝐎𝐓",
                callback_data=f"ready_ss_{amount}",
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ 𝐁𝐀𝐂𝐊",
                callback_data="back_to_plans",
            )
        ],
    ]

    await query.message.edit_caption(
        caption=(
            f"<b>✅ 𝐏𝐀𝐘𝐌𝐄𝐍𝐓 𝐌𝐀𝐑𝐊𝐄𝐃 — ₹{amount}</b>\n\n"
            "📸 <b>Next step:</b> apna payment screenshot isi bot chat "
            "mein bhejna hai.\n\n"
            "👇 Neeche button dabayein, phir screenshot photo ke "
            "roop mein send karein."
        ),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def ready_screenshot(query, amount):
    user_id = query.from_user.id
    query.message.bot_data.setdefault("pending_payments", {})
    query.message.bot_data["pending_payments"][user_id] = amount

    await query.message.edit_caption(
        caption=(
            f"<b>📸 𝐒𝐄𝐍𝐃 𝐏𝐀𝐘𝐌𝐄𝐍𝐓 𝐒𝐂𝐑𝐄𝐄𝐍𝐒𝐇𝐎𝐓</b>\n\n"
            f"💰 Plan amount: <b>₹{amount}</b>\n\n"
            "👉 Ab isi chat mein payment screenshot "
            "<b>photo</b> ke roop mein send karein.\n\n"
            "⏳ Screenshot admin verification ke liye forward hoga."
        ),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "⬅️ 𝐁𝐀𝐂𝐊",
                    callback_data="back_to_plans",
                )
            ]
        ]),
    )


async def receive_screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.message:
        return

    user_id = update.effective_user.id
    pending = context.bot_data.get("pending_payments", {})
    amount = pending.get(user_id)

    # User ne payment flow start nahi kiya.
    if not amount:
        return

    if not update.message.photo:
        await update.message.reply_text(
            "📸 Please payment screenshot ko <b>photo</b> ke roop mein send karein.",
            parse_mode="HTML",
        )
        return

    photo = update.message.photo[-1]

    admin_caption = (
        "🔔 <b>NEW PAYMENT SCREENSHOT</b>\n\n"
        f"👤 User: <b>{update.effective_user.full_name}</b>\n"
        f"🆔 User ID: <code>{user_id}</code>\n"
        f"💰 Amount: <b>₹{amount}</b>\n\n"
        "⚠️ Please verify the payment manually."
    )

    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo.file_id,
        caption=admin_caption,
        parse_mode="HTML",
    )

    # Remove pending state after successful forwarding.
    pending.pop(user_id, None)

    await update.message.reply_text(
        "✅ <b>Screenshot received!</b>\n\n"
        "📨 Aapka screenshot admin ko verification ke liye bhej diya gaya hai.\n"
        "⏳ Verification ke baad admin aapko access dega.",
        parse_mode="HTML",
    )


# ==================================================
#                    STATS
# ==================================================
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or update.effective_user.id != ADMIN_ID:
        return

    text = (
        "📊 <b>𝐁𝐎𝐓 𝐒𝐓𝐀𝐓𝐒</b>\n\n"
        f"👥 Total Users: <b>{len(users)}</b>\n\n"
        f"💎 ₹99 Clicks: <b>{plan_99}</b>\n"
        f"🔥 ₹149 Clicks: <b>{plan_149}</b>\n"
        f"📦 ₹249 Clicks: <b>{plan_249}</b>\n"
        f"👑 ₹499 Clicks: <b>{plan_499}</b>"
    )

    await update.message.reply_text(text, parse_mode="HTML")


# ==================================================
#                 BUTTON HANDLER
# ==================================================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global plan_99, plan_149, plan_249, plan_499

    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "premium":
        await premium_menu(query)

    elif data == "home":
        await home_page(query)

    elif data == "back_to_plans":
        await premium_menu(query)

    elif data == "p1":
        plan_99 += 1
        await qr_page(query, QR_99, 99)

    elif data == "p2":
        plan_149 += 1
        await qr_page(query, QR_149, 149)

    elif data == "p3":
        plan_249 += 1
        await qr_page(query, QR_249, 249)

    elif data == "p4":
        plan_499 += 1
        await qr_page(query, QR_499, 499)

    elif data.startswith("paid_"):
        amount = int(data.split("_", 1)[1])
        await paid_page(query, amount)

    elif data.startswith("ready_ss_"):
        amount = int(data.split("_", 2)[2])
        await ready_screenshot(query, amount)


# ==================================================
#                  ERROR HANDLER
# ==================================================
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.exception(
        "Exception while processing an update:",
        exc_info=context.error,
    )


# ==================================================
#                    RUN BOT
# ==================================================
def main():
    if not TOKEN:
        raise RuntimeError(
            "BOT_TOKEN is missing. Set the BOT_TOKEN environment variable."
        )

    if not ADMIN_ID:
        raise RuntimeError(
            "ADMIN_ID is missing. Set the ADMIN_ID environment variable."
        )

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stats", stats))

    # Buttons
    app.add_handler(CallbackQueryHandler(button_handler))

    # Payment screenshot receiver
    app.add_handler(
        MessageHandler(filters.PHOTO, receive_screenshot)
    )

    app.add_error_handler(error_handler)

    print("✅ 𝐁𝐎𝐓 𝐈𝐒 𝐑𝐔𝐍𝐍𝐈𝐍𝐆 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘...")

    app.run_polling()


if __name__ == "__main__":
    main()
