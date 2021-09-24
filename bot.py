import telebot
import config
import time
import os
import re

def main():
    # ...
    port = os.getenv('PORT', default=8000)
    updater.start_webhook(port=port)
    
bot = telebot.TeleBot(config.TOKEN)

dnr111 = re.findall(r'обедать')
qa1 = ('@MikFilippov, @Lobanova_Olga, @Azamat_Gu, @Igor_Kirichek, @esaulkovaav')
tl1 = ('@ashutay, @mike_alexandrov')
tlqa = ('@gryzb1')
back1 = ('@ivleonov, @tshloman, @mmeiko, @barysh_vn, @DmitryChernoyarov, @MaximB98')
front1 = ('@Frozenzxc, @chimir, @Danil_Abr')
pm1 = ('@gashimovak, @Becky_Bones, @daria_abramova')
dnr1 = "на обед"
dnr2 = "кушать"
dnr3 = "кушоц"
dnr4 = "кушац"
dnr5 = "пойду поем"
dnr6 = "ушел на обед"
dnr7 = "ушел пообедать"
dnr8 = "пообедаю"
dnr9 = "я с вами"
dnr10 = "подождите меня"
dnr11 = "я тоже пойду поем"
dnr12 = "я тоже на обед"
dnr13 = "кушот"
dnr14 = "кушоть"
dnr15 = "тоже на обед"
dnr16 = "обедать"
dnr17 = "ушёл на обед"
dnr18 = "покушать"
dnr19 = "покушаю"
dnr20 = "тоже покушать"
dnr21 = "пора покушать"

dnrstc1 = "AgADAgADA8KlDg"
dnrstc2 = "AgADZgADqregFw"

@bot.message_handler(commands=['qa'])
 
def qa(message):
    bot.send_message(message.chat.id,'Тестировщики! \n' + qa1.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['tl'])
 
def tl(message):
    bot.send_message(message.chat.id,'Тимлиды! \n' + tl1.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['front'])
 
def front(message):
    bot.send_message(message.chat.id,'Фронты! \n' + front1.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['back'])
 
def back(message):
    bot.send_message(message.chat.id,'Бэки! \n' + back1.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['pm'])
 
def mgr(message):
    bot.send_message(message.chat.id,'Манажеры! \n' + pm1.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['all'])
 
def all(message):
    bot.send_message(message.chat.id,'ТОВАРИЩИ! \n' + qa1 + ' ' + tl1 + ' ' + front1 + ' ' + back1 + ' ' + tlqa + ' ' + pm1.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['meet'])
 
def meetup(message):
    sti = open('stick/sticker.webp', 'rb')

    bot.send_message(message.chat.id,'МИТИНГ! \n' + qa1 + ' ' + tl1 + ' ' + front1 + ' ' + back1 + ' ' + pm1.format(message.from_user, bot.get_me()),parse_mode='html')
    time.sleep(2)
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, f'https://meet.google.com/bxq-nsek-ept')
@bot.message_handler(content_types=['text'])

def handle_text(message):
    if re.findall(r'кушоц', message.text) or message.text.casefold() == dnr111 or message.text.casefold() == dnr1 or message.text.casefold() == dnr2 or message.text.casefold() == dnr3 or message.text.casefold() == dnr4 or message.text.casefold() == dnr5 or message.text.casefold() == dnr6 or message.text.casefold() == dnr7 or message.text.casefold() == dnr8 or message.text.casefold() == dnr9 or message.text.casefold() == dnr10 or message.text.casefold() == dnr11 or message.text.casefold() == dnr12 or message.text.casefold() == dnr13 or message.text.casefold() == dnr14 or message.text.casefold() == dnr15 or message.text.casefold() == dnr16 or message.text.casefold() == dnr17 or message.text.casefold() == dnr18 or message.text.casefold() == dnr19 or message.text.casefold() == dnr20 or message.text.casefold() == dnr21:
        bot.send_message(message.chat.id, f'Приятного аппетита, {message.from_user.first_name}!')
    
@bot.message_handler(content_types=["sticker"])

def handle_docs_audio(message):
    if message.sticker.file_unique_id == dnrstc1 or message.sticker.file_unique_id == dnrstc2:
        bot.send_message(message.chat.id, f'Приятного аппетита, {message.from_user.first_name}!')

bot.polling(none_stop=True)