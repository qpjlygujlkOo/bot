import telebot
#import config1
import time
import os
import random
from fastapi import FastAPI
import requests

bot = FastAPI()

token = os.environ.get('TOKEN')
#token = '1548279772:AAFHf8ChEdDIsunUEFiSI7r_-JF-lKwBuMw'
 
f = open('dict.txt', 'r', encoding='utf-8')
list = f.read().split('\n')
dict = tuple(list)

# def main():
#     # ...
#     port = os.getenv('PORT', default=8000)
#     updater.start_webhook(port=port)
bot = telebot.TeleBot(token)


# bot = telebot.TeleBot(config1.TOKEN)

#key = (token)
qa1 = ('@rasul_mamedov, @Lobanova_Olga, @Azamat_Gu, @Igor_Kirichek')
# tl1 = ('@ashutay, @ivleonov')
# tlqa = ('@gryzb1')
# back1 = ('@paprozo, @mmeiko, @barysh_vn, @DmitryChernoyarov, @MaximB98')
# front1 = ('@Frozenzxc, @chimir')
# pm1 = ('@gashimovak, @Becky_Bones, @OlgaShtefanko')
# dnr1 = "на обед"
# dnr2 = "кушать"
# dnr3 = "кушоц"
# dnr4 = "кушац"
# dnr5 = "пойду поем"
# dnr6 = "ушел на обед"
# dnr7 = "ушел пообедать"
# dnr8 = "пообедаю"
# dnr9 = "я с вами"
# dnr10 = "подождите меня"
# dnr11 = "я тоже пойду поем"
# dnr12 = "я тоже на обед"
# dnr13 = "кушот"
# dnr14 = "кушоть"
# dnr15 = "тоже на обед"
# dnr16 = "обедать"
# dnr17 = "ушёл на обед"
# dnr18 = "покушать"
# dnr19 = "покушаю"
# dnr20 = "тоже покушать"
# dnr21 = "пора покушать"
# dnr22 = "обед"

# ras1 = "rasul_mamedov"
# kir1 = "Azamat_Gu"

# dnrstc1 = "AgADAgADA8KlDg"
# dnrstc2 = "AgADZgADqregFw"


# # @bot.message_handler(commands=['key'])

# # def key(message):
# #     bot.send.message(message.chat.id, 'токен' + key.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['qa'])
 
def qa(message):
    bot.send_message(message.chat.id,'Тестировщики! \n' + qa1.format(message.from_user, bot.get_me()),parse_mode='html')

# @bot.message_handler(commands=['tl'])
 
# def tl(message):
#     bot.send_message(message.chat.id,'Тимлиды! \n' + tl1.format(message.from_user, bot.get_me()),parse_mode='html')

# @bot.message_handler(commands=['front'])
 
# def front(message):
#     bot.send_message(message.chat.id,'Фронты! \n' + front1.format(message.from_user, bot.get_me()),parse_mode='html')

# @bot.message_handler(commands=['back'])
 
# def back(message):
#     bot.send_message(message.chat.id,'Бэки! \n' + back1.format(message.from_user, bot.get_me()),parse_mode='html')

# @bot.message_handler(commands=['pm'])
 
# def mgr(message):
#     bot.send_message(message.chat.id,'Манажеры! \n' + pm1.format(message.from_user, bot.get_me()),parse_mode='html')

# @bot.message_handler(commands=['all'])
 
# def all(message):
#     bot.send_message(message.chat.id,'ТОВАРИЩИ! \n' + qa1 + ' ' + tl1 + ' ' + front1 + ' ' + back1 + ' ' + tlqa + ' ' + pm1.format(message.from_user, bot.get_me()),parse_mode='html')

# @bot.message_handler(commands=['meet'])
 
# def meetup(message):
#     sti = open('stick/sticker.webp', 'rb')

#     bot.send_message(message.chat.id,'МИТИНГ! \n' + qa1 + ' ' + tl1 + ' ' + front1 + ' ' + back1 + ' ' + pm1.format(message.from_user, bot.get_me()),parse_mode='html')
#     time.sleep(2)
#     bot.send_sticker(message.chat.id, sti)
#     bot.send_message(message.chat.id, f'https://meet.google.com/bxq-nsek-ept')
# @bot.message_handler(content_types=['text'])

# def handle_text(message):
#     if (message.from_user.username == kir1 or message.from_user.username == ras1) and (message.text.casefold() == dnr1 or message.text.casefold() == dnr2 or message.text.casefold() == dnr3 or message.text.casefold() == dnr4 or message.text.casefold() == dnr5 or message.text.casefold() == dnr6 or message.text.casefold() == dnr7 or message.text.casefold() == dnr8 or message.text.casefold() == dnr9 or message.text.casefold() == dnr10 or message.text.casefold() == dnr11 or message.text.casefold() == dnr12 or message.text.casefold() == dnr13 or message.text.casefold() == dnr14 or message.text.casefold() == dnr15 or message.text.casefold() == dnr16 or message.text.casefold() == dnr17 or message.text.casefold() == dnr18 or message.text.casefold() == dnr19 or message.text.casefold() == dnr20 or message.text.casefold() == dnr21):
#         exp = open('gif/exp.gif', 'rb')
#         bot.send_message(message.chat.id, f'ب الهناء والشفاء / بالهنا والشف!, {message.from_user.first_name}!')
#         bot.send_animation(message.chat.id, exp)
#     elif (message.text.casefold() == dnr1 or message.text.casefold() == dnr2 or message.text.casefold() == dnr3 or message.text.casefold() == dnr4 or message.text.casefold() == dnr5 or message.text.casefold() == dnr6 or message.text.casefold() == dnr7 or message.text.casefold() == dnr8 or message.text.casefold() == dnr9 or message.text.casefold() == dnr10 or message.text.casefold() == dnr11 or message.text.casefold() == dnr12 or message.text.casefold() == dnr13 or message.text.casefold() == dnr14 or message.text.casefold() == dnr15 or message.text.casefold() == dnr16 or message.text.casefold() == dnr17 or message.text.casefold() == dnr18 or message.text.casefold() == dnr19 or message.text.casefold() == dnr20 or message.text.casefold() == dnr21):
#         bon = random.choice(dict)
#         bot.send_message(message.chat.id, f'{bon}, {message.from_user.first_name}!') 

# #@bot.message_handler(content_types=["sticker"])

# #def handle_docs_audio(message):
# #    if message.text.casefold() == dnr1:
# #        bot.send_message(message.chat.id, f'Приятного аппетита, {message.from_user.first_name}, {message.file_unique_id}!')

bot.polling(none_stop=True)