from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
)

from config import TOKEN
from handlers.start import start
from handlers.menu import menu
from handlers.prayers import prayers, get_city, CITY
from handlers.azkar import azkar_menu
from handlers.quran import quran_menu, read_surah

app = Application.builder().token(TOKEN).build()

# /start
app.add_handler(CommandHandler("start", start))

# مواقيت الصلاة
prayer_handler = ConversationHandler(
    entry_points=[
        MessageHandler(
            filters.Regex("^🕌 مواقيت الصلاة$"),
            prayers
        )
    ],
    states={
        CITY: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_city
            )
        ]
    },
    fallbacks=[]
)

app.add_handler(prayer_handler)

# أزرار الأذكار
app.add_handler(
    MessageHandler(
        filters.Regex(
            "^(🌅 أذكار الصباح|🌙 أذكار المساء|🤲 أذكار بعد الصلاة|⬅️ رجوع)$"
        ),
        azkar_menu
    )
)

# أزرار القرآن
app.add_handler(
    MessageHandler(
        filters.Regex(
            "^(📚 فهرس السور|📖 سورة اليوم)$"
        ),
        quran_menu
    )
)

# قراءة السورة بالرقم
app.add_handler(
    MessageHandler(
        filters.Regex(r"^\d+$"),
        read_surah
    )
)

# القائمة الرئيسية
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        menu
    )
)

print("Bot is running...")

app.run_polling()