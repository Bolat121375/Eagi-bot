from aiogram import types, Dispatcher
import aiofiles
import os
from utils import summarize_file

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def start_cmd(message: types.Message):
    await message.answer("Привет! Я бот для обмена учебными материалами 📚. Пришли файл, чтобы загрузить его.")

async def handle_file(message: types.Message):
    file = message.document
    file_name = file.file_name
    file_path = os.path.join(UPLOAD_DIR, file_name)

    await message.document.download(destination_file=file_path)
    await message.answer(f"Файл '{file_name}' успешно загружен!")

    summary = await summarize_file(file_path)
    if summary:
        await message.answer(f"📄 Краткое содержание:\n{summary}")
    else:
        await message.answer("Не удалось создать краткое содержание файла.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=["start"])
    dp.register_message_handler(handle_file, content_types=types.ContentType.DOCUMENT)
