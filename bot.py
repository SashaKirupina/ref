import telebot
from translator_service import log_and_process, complex_translate_process, LANGUAGES

TOKEN = "7914727289:AAGUyJfA3ex2t_MTxrYGIFKqNbGYrDwN_Hs"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот-переводчик. Используйте /translate <язык> <текст>.")


@bot.message_handler(commands=['translate'])
def handle_translate(message):
    """Обработчик команды /translate"""
    args = message.text.split(maxsplit=2)

    if len(args) < 3:
        bot.reply_to(message, "Ошибка: укажите язык и текст для перевода.")
        return

    language, text = args[1], args[2]
    try:
        # Обрабатываем текст
        processed_text = log_and_process(bot, text)
        if "Текст" in processed_text or "Ошибка" in processed_text:
            bot.reply_to(message, processed_text)
            return  # Выход, если обработка текста вернула ошибку

        # Выполняем перевод
        translation = complex_translate_process(language, text)
        bot.reply_to(message, f"Перевод на {language}: {translation}")

    except Exception as e:
        bot.reply_to(message, f"Ошибка обработки: {e}")


@bot.message_handler(commands=['languages'])
def handle_languages(message):
    """Отправляет список доступных языков"""
    languages_str = "\n".join([f"{key}: {LANGUAGES[key]}" for key in LANGUAGES])
    bot.reply_to(message, f"Доступные языки:\n{languages_str}")


bot.polling()