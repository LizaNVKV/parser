import requests
from aiogram import Bot, Dispatcher, executor
from bs4 import BeautifulSoup as b

URL = 'https://citatnica.ru/citaty/krutye-tsitaty-dlya-patsanov-400-tsitat'
TOKEN = '6232853649:AAEmgj63apZkj-xkkBnpwh5eEAku-HMFs9M'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    volki = soup.find_all('div', class_='su-note')
    return [c.text for c in volki]
#chisto_volki = [c.text for c in volki]
#print(chisto_volki)

list_staya = parser(URL)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['начать'])
async def hello(message):
    await message.reply('Ауф, брат! Нужна мудрость? Их есть у меня! Введи любую цифру:')


@dp.message_handler(content_types=['text'])
async def qoutes(message):
    if message.text.lower() in '123456789':
        await message.reply(list_staya[0])
        #bot.send_message(message.chat.id, list_staya[0])
        del list_staya[0]
    else:
        await message.reply('Воу, брат, сказал же, цифру!')
        #bot.send_message(message.chat.id, 'Воу, брат, сказал же, цифру!')

executor.start_polling(dp)