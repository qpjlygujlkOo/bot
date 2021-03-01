import telebot
import config
import time
import os
import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,MessageHandler, Filters
import visionocr
import os
from CREDENTIALS import BOT_KEY

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

@bot.message_handler(commands=['митинг'])
 
def meetup(message):
    sti = open('stick\\sticker.webp', 'rb')

    bot.send_message(message.chat.id,'МИТИНГ! \n' + qa1 + ' ' + tl1 + ' ' + front1 + ' ' + back1 + ' ' + pm1.format(message.from_user, bot.get_me()),parse_mode='html')
    time.sleep(2)
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler(content_types=['text'])

def handle_text(message):
    if message.text.casefold() == dnr1 or message.text.casefold() == dnr2 or message.text.casefold() == dnr3 or message.text.casefold() == dnr4 or message.text.casefold() == dnr5 or message.text.casefold() == dnr6 or message.text.casefold() == dnr7 or message.text.casefold() == dnr8 or message.text.casefold() == dnr9 or message.text.casefold() == dnr10 or message.text.casefold() == dnr11 or message.text.casefold() == dnr12 or message.text.casefold() == dnr13 or message.text.casefold() == dnr14 or message.text.casefold() == dnr15 or message.text.casefold() == dnr16 or message.text.casefold() == dnr17 or message.text.casefold() == dnr18 or message.text.casefold() == dnr19 or message.text.casefold() == dnr20 or message.text.casefold() == dnr21:
        bot.send_message(message.chat.id, f'Приятного аппетита, {message.from_user.first_name}!')
    
@bot.message_handler(content_types=["sticker"])

def handle_docs_audio(message):
    if message.sticker.file_unique_id == dnrstc1 or message.sticker.file_unique_id == dnrstc2:
        bot.send_message(message.chat.id, f'Приятного аппетита, {message.from_user.first_name}!')

def start(update, context):
    firstname = update.message.from_user.first_name
    bot.send_message(chat_id=update.message.chat_id, text=("Hey " + firstname + ", send me any picture containing text and I will OCR it for you!"))

def echo(update, context):
    message = update.message.text
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id, text="Try sending me a picture with any text in it and I will OCR it for you!")

def receive_doc(update, context):
    message = update.message
    file_id = message.document.file_id
    chat_id = update.message.chat_id
    ocr_file(bot,update,file_id,chat_id)

def receive_image(update, context):
    message = update.message
    file_id = message.photo[-1].file_id
    chat_id = update.message.chat_id
    ocr_file(bot,update,file_id,chat_id)
    
def ocr_file(update, context, file_id, chat_id):
    filepath = os.path.expanduser('~') + '/' + file_id
    print(filepath)
    bot.send_message(chat_id=chat_id, text="Please hold on...")
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    file = bot.get_file(file_id).download(filepath)
    
    ocr_text = visionocr.read_image(filepath)
    bot.send_message(chat_id=chat_id, text='Here you go:\n\n' + str(ocr_text))
    os.remove(filepath)


# handlers
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)
doc_handler = MessageHandler(Filters.document, receive_doc)
image_handler = MessageHandler(Filters.photo, receive_image)

#dispatchers
#тызаебеш
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(doc_handler)
dispatcher.add_handler(image_handler)

bot.polling(none_stop=True)
