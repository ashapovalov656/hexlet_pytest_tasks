# Нажмите кнопку Run, чтобы запустить тесты.

# Файлы с исходным кодом можно посмотреть на вкладке "Files":
# src/capitalize.py        - тестируемая функция
# tests/test_capitalize.py - тесты функции

# Попробуйте изменять код функции/тестов, запуская проверки заново.

from src.capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')

if capitalize('Hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize('h') != 'H':
    raise Exception('Функция работает неверно!')

if capitalize('123') != '123':
    raise Exception('Функция работает неверно!')

if capitalize('привет') != 'Привет':
    raise Exception('Функция работает неверно!')

if capitalize(' text') != ' text':
    raise Exception('Функция работает неверно!')

if capitalize(123) != 123:
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')
