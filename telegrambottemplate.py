import random
import telebot
from telebot import types


bot = telebot.TeleBot('токен вашего бота, брать в bot father')

answers = ['17:21 не понял, что ты хочешь сказать.', 'Извини, 17:21 тебя не понимает.', '17:21 не знает такой команды.', 'Мой разработчик не говорил, что отвечать в такой ситуации... >_<']


@bot.message_handler(commands=['start'])
def welcome(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🛍 Товары')
    button3 = types.KeyboardButton('📄 Помощь')
    
    markup.row(button1)
    markup.row(button3)

    if message.text == '/start':
        
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\n\nЖелаете что-либо купить?', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Перекинул тебя в главном меню! Выбирай!', reply_markup=markup)


@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото :(')

@bot.message_handler()
def info(message):
    if message.text == '🛍 Товары':
        goodsChapter(message)
    elif message.text == '📄 Помощь':
        infoChapter(message)
    
    elif message.text == '🔹 Картхолдер Louis Vuitton':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_photo(message.chat.id, photo=open('ссылка на директорию в вашем пк', 'rb'))
        bot.send_message(message.chat.id, 'О товаре:\n🔹_Отличное качество_\n🔹_5 различных расцветок по вашему желанию_\n🔹_5 карманов_\n\nЦена:\n🔹_599 руб._', reply_markup=markup, parse_mode="Markdown")
    
    elif message.text == '🔹 Ремень Louis Vuitton':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_photo(message.chat.id, photo=open('ссылка на директорию в вашем пк', 'rb'))
        bot.send_message(message.chat.id, 'О товаре:\n_🔹Ремень из высококачественной эко-кожи премиум класса, который станет супер дополнением к вашей одежде\n🔹Высокое качество материалов\n🔹Удобство и комфорт\n🔹Универсальность\n🔹Унисекс\n🔹Длина ремня : 110 см_\n\nЦена:\n🔹_799 руб._', reply_markup=markup, parse_mode="Markdown")
        
    
    elif message.text == '🔹 Сумка Trapstar':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_photo(message.chat.id, photo=open('ссылка на директорию в вашем пк', 'rb'))
        bot.send_message(message.chat.id, 'О товаре:\n_🔹Отличное качество\n🔹Брендированный ремень\n🔹Металлическая заклепка_\n\nЦена:\n🔹_1199 руб._', reply_markup=markup, parse_mode="Markdown")
    
    elif message.text == '✏️ Написать разработчику':
        bot.send_message(message.chat.id, 'тг-ссылка на админа\n_Admin_', parse_mode="Markdown")
    elif message.text == '💳 Купить':
        bot.send_message(message.chat.id, 'тг-ссылка на саппорта\n_Support_', parse_mode="Markdown")
    
    elif message.text == '↩️ Назад':
        goodsChapter(message)
    elif message.text == '↩️ Назад в меню':
        welcome(message)
    
    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])

# Функция, отвечающая за раздел товаров в наличии.
def goodsChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🔹 Картхолдер Louis Vuitton')
    button2 = types.KeyboardButton('🔹 Ремень Louis Vuitton')
    button3 = types.KeyboardButton('🔹 Сумка Trapstar')
    button5 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3)
    markup.row(button5)

    bot.send_message(message.chat.id, 'Вот все товары, которые сейчас находятся в продаже:', reply_markup=markup)



# Функция, отвечающая за раздел помощи
def infoChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('✏️ Написать разработчику')
    button2 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    bot.send_message(message.chat.id, 'Раздел помощи.\nЗдесь ты можешь написать моему разработчику по интересующим вопросам.', reply_markup=markup)

# Запускаем бота (можно поставить на хостинг)
bot.polling(none_stop=True)