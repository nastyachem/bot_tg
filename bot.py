#Импорт библиотек
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

# 2.Инициализация объектов
TOKEN= os.getenv('TOKEN')
bot = Bot(token =TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('bot_transliteration.log', encoding='utf-8'),
                              logging.StreamHandler()
                              ])
logger = logging.getLogger(__name__)
#3.Обработка комманды старт
@dp.message(Command(commands=['start']))
async def process_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Сейчас я сделаю транслитерацию твоих сообщений 📨'
    logging.info(f'{user_name} {user_id}  запустил бота')
    await bot.send_message(chat_id=user_id, text=text)


#4. создаем словать для транслитерации
dict_trans = {
    'А': 'A', 'а': 'a',
    'Б': 'B', 'б': 'b',
    'В': 'V', 'в': 'v',
    'Г': 'G', 'г': 'g',
    'Д': 'D', 'д': 'd',
    'Е': 'E', 'е': 'e',
    'Ё': 'E', 'ё': 'e',
    'Ж': 'ZH', 'ж': 'zh',
    'З': 'Z', 'з': 'z',
    'И': 'I', 'и': 'i',
    'Й': 'I', 'й': 'i',
    'К': 'K', 'к': 'k',
    'Л': 'L', 'л': 'l',
    'М': 'M', 'м': 'm',
    'Н': 'N', 'н': 'n',
    'О': 'O', 'о': 'o',
    'П': 'P', 'п': 'p',
    'Р': 'R', 'р': 'r',
    'С': 'S', 'с': 's',
    'Т': 'T', 'т': 't',
    'У': 'U', 'у': 'u',
    'Ф': 'F', 'ф': 'f',
    'Х': 'KH', 'х': 'kh',
    'Ц': 'TS', 'ц': 'ts',
    'Ч': 'CH', 'ч': 'ch',
    'Ш': 'SH', 'ш': 'sh',
    'Щ': 'SHCH', 'щ': 'shch',
    'Ы': 'Y', 'ы': 'y',
    'Ъ': 'IE', 'ъ': 'ie',
    'Ь': '', 'ь': '',
    'Э': 'E', 'э': 'e',
    'Ю': 'IU', 'ю': 'iu',
    'Я': 'IA', 'я': 'ia',
}

def transliteration(text: str):
    res = []
    for char in text:
        if char in dict_trans:
            res.append(dict_trans[char])
        else:
            res.append(char)    
    return ''.join(res)        


# 5.Обработка всех сообщений
@dp.message()
async def send_transcription(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    text_trans = transliteration(text)
    logging.info(f'Транслитерация для {user_name} {user_id}:Оригинал ({text}) -> {text_trans}')
    await message.answer(text=text_trans)


#6.Запуск процесса пуллинга

if __name__ == '__main__':
    dp.run_polling(bot)
