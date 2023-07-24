# Нажмите кнопку Run, чтобы запустить тесты.

# Файлы с исходным кодом можно посмотреть на вкладке "Files":
# src/capitalize.py        - тестируемая функция
# tests/test_capitalize.py - тесты функции

# Попробуйте изменять код функции/тестов, запуская проверки заново.

from src.capitalize import capitalize

assert capitalize('hello') == 'Hello'

assert capitalize('') == ''

assert capitalize('Hello') == 'Hello'

assert capitalize('h') == 'H'

assert capitalize('123') == '123'

assert capitalize('привет') == 'Привет'

assert capitalize(' text') == ' text'

assert capitalize(123) == 123

print('Все тесты пройдены!')
