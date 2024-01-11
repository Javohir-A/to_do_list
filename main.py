import telebot
from menu_btns import create_menu
from file_handling import *

token = '6983726010:AAG4xD1m76fNQSR6S7t8gtZrzb0BOo0bURc'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    with open('welcome_en.txt', 'r') as welcome_file:
        welcome_message = welcome_file.read()
    bot.send_message(message.chat.id, welcome_message)
    #Call menu buttons from menu_btns.py
    menu = create_menu()
    bot.send_message(message.chat.id, 'Choose an option', reply_markup=menu)

@bot.message_handler(func=lambda message: message.text == 'Add Tasks')
def add_tasks(message):
    create_new_btn = telebot.types.KeyboardButton('Create new task')
    back_btn = telebot.types.KeyboardButton('Back')
    add_task_menu_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    add_task_menu_markup.add(create_new_btn, back_btn)
    bot.send_message(message.chat.id, 'Choose an option', reply_markup=add_task_menu_markup)

@bot.message_handler(func=lambda message: message.text == 'Create new task')
def save_to_file(message):
    bot.reply_to(message, 'Send me a task.')
    global new_task_pressed 
    new_task_pressed = True
    @bot.message_handler(func=lambda message: new_task_pressed)
    def save_to_file2(message):
        global new_task_pressed
        new_task_pressed = False
        print(f"Saving task: {message.text}")
        with open('user_to_.txt', 'a') as save_to_file:
            save_to_file.write(str(message.chat.id) + ' : ' + message.text + '\n')
        bot.reply_to(message, 'Task added successfully!')

@bot.message_handler(func=lambda message: message.text == 'Back')
def back_to_menu(message):
    send_welcome(message)

@bot.message_handler(func=lambda message: message.text == 'View Tasks')
def view_tasks(message):
    # print(message)
    content = send_list_for_view('user_to_.txt', message.chat.id)
    content_viewer = ''
    for i,x in enumerate(content):
        content[i] = str(i+1) + '.' + x
    for x in content:
        content_viewer = '\n'.join(content)

    print(content)
    if content_viewer:
        bot.send_message(message.chat.id, content_viewer)
    else:
        bot.send_message(message.chat.id, 'No tasks available.')
@bot.message_handler(func= lambda message : message.text == 'Remove Task')
def remove_task(message):
    view_tasks(message)
    global remove_task_btn_pressed
    remove_task_btn_pressed = True
    bot.send_message(message.chat.id, "Send the index of the task you want to remove.")
    @bot.message_handler(func=lambda message : remove_task_btn_pressed)
    def get_index(message):
        global remove_task_btn_pressed
        remove_task_btn_pressed = False
        index = message.text
        
bot.infinity_polling()


# %%
