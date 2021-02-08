import telebot
import config
import time
import os

def main():
    # ...
    port = os.getenv('PORT', default=8000)
    updater.start_webhook(port=port)
    
bot = telebot.TeleBot(config.TOKEN)

qa1 = ('@SmirnovIvan, @VIKACHU1337, @Konstantin_Gladun, @Azamat_Gu, @Igor_Kirichek')
tl1 = ('@ashutay, @DmitryMatlah')
back1 = ('@ivleonov, @tshloman, @mmeiko, @impavel, @barysh_vn, @DmitryChernoyarov')
front1 = ('@Frozenzxc, @mimoniskr, @Spartfin, @chimir')
pm1 = ('@gashimovak, @Becky_Bones, @daria_abramova')

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
    bot.send_message(message.chat.id,'ТОВАРИЩИ! \n' + qa1 + ' ' + tl1 + ' ' + front1 + ' ' + back1 + ' ' + pm1.format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(commands=['meet'])
 
def meetup(message):
    sti = open('stick/sticker.webp', 'rb')

    bot.send_message(message.chat.id,'МИТИНГ! \n' + qa1 + ' ' + tl1 + ' ' + front1 + ' ' + back1 + ' ' + pm1.format(message.from_user, bot.get_me()),parse_mode='html')
    time.sleep(2)
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text() == 'на обед', 'кушоц', 'кушать', 'кушац', 'ушел на обед', 'отобедаю', 'тоже на обед':
        bot.reply_to(message.from_user.id, 'Приятного, {message.from_user.first_name}')

bot.polling(none_stop=True)
