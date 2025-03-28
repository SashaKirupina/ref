import pytest
from translator_service import log_and_process, complex_translate_process

# Тест для log_and_process
def test_log_and_process_short_text():
    assert log_and_process(None, "Hi") == "Текст слишком короткий: Hi"

def test_log_and_process_long_text():
    long_text = "A" * 101
    assert log_and_process(None, long_text) == f"Текст слишком длинный: {long_text}"

def test_log_and_process_valid_text():
    text = "Hello, world!"
    assert log_and_process(None, text) == text

# Тест для complex_translate_process (нужен мок, так как Google Translate делает сетевой запрос)
def test_complex_translate_process_valid_language(mocker):
    mocker.patch("translator_service.translator.translate", return_value=type("obj", (object,), {"text": "Привет, мир!"})())

    result = complex_translate_process("ru", "Hello, world!")
    assert result == "Привет, мир!"

def test_complex_translate_process_invalid_language():
    result = complex_translate_process("invalid_lang", "Hello, world!")
    assert result.startswith("Ошибка")