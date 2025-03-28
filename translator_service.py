import logging
from googletrans import Translator, LANGUAGES

translator = Translator()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

def log_and_process(bot, text):
    """Проверяет длину текста и возвращает его, если длина корректна."""
    if not text:
        return "Ошибка: текст не должен быть пустым."
    if len(text) < 10:
        return f"Текст слишком короткий: {text}"
    if len(text) > 100:
        return f"Текст слишком длинный: {text}"
    return text

def complex_translate_process(language, text):
    """Переводит текст на указанный язык, если язык доступен."""
    if language not in LANGUAGES:
        return f"Ошибка: язык '{language}' не поддерживается."

    try:
        result = translator.translate(text, dest=language)
        return result.text
    except Exception as e:
        logging.error(f"Ошибка перевода: {e}")
        return "Ошибка перевода. Попробуйте позже."