# Инструкция по установке и запуску
1. Создать виртуальное окружение
```bash
python -m venv venv
```
2. Активировать виртуальное окружение
```bash
Linux/macOS
source venv/bin/activate
Windows
venv\Scripts\activate
```
3. Установить зависимости
```bash
pip install -r requirements.txt
```
---
## Скрипт 1: Проверка email-доменов
1. Создать файл emails.txt и добавить email-адреса, по одному в строке:
```text
user@example.com
test@gmail.com
wrong@nonexistentdomain12345.xyz
```
2. Запустить скрипт:
```bash
python3 email_checker.py
```
Скрипт выведет статус домена для каждого email.
---
## Скрипт 2: Отправка текста в Telegram
1. Создать файл .env рядом со скриптом:
```env
TOKEN=ВАШ_ТОКЕН_БОТА
CHAT_ID=ВАШ_CHAT_ID
INPUT_FILE=message.txt
```
2. Создать файл message.txt с текстом, который нужно отправить.
3. Запустить скрипт:
```bash
python3 bot.py
```
Бот отправит текст из message.txt в указанный чат Telegram.