import telebot

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
TOKEN = '6983726010:AAG4xD1m76fNQSR6S7t8gtZrzb0BOo0bURc'
bot = telebot.TeleBot(TOKEN)

tasks_file = "tasks.txt"
tasks = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    load_tasks(user_id)

    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    add_button = telebot.types.KeyboardButton('➕ Add Task')
    list_button = telebot.types.KeyboardButton('📋 List Tasks')
    keyboard.add(add_button, list_button)

    bot.send_message(user_id, "Welcome to the To-Do List Bot! How can I assist you?", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == '➕ Add Task')
def add_task(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Enter the task you want to add:")
    bot.register_next_step_handler(message, process_add_task)

def process_add_task(message):
    user_id = message.from_user.id
    task = message.text.strip()
    if task:
        tasks.setdefault(user_id, []).append(task)
        save_tasks(user_id)
        bot.send_message(user_id, f'Task "{task}" added successfully!')
    else:
        bot.send_message(user_id, 'Please provide a task to add.')

    # Remove the custom keyboard after processing the command
    remove_keyboard = telebot.types.ReplyKeyboardRemove()
    bot.send_message(user_id, "How can I assist you now?", reply_markup=remove_keyboard)

@bot.message_handler(func=lambda message: message.text == '📋 List Tasks')
def list_tasks(message):
    user_id = message.from_user.id
    load_tasks(user_id)
    current_tasks = tasks.get(user_id, [])
    if current_tasks:
        task_list = '\n'.join([f"{index + 1}. {task}" for index, task in enumerate(current_tasks)])
        bot.send_message(user_id, f'Your To-Do List:\n{task_list}')
    else:
        bot.send_message(user_id, 'Your To-Do list is empty.')

    # Remove the custom keyboard after processing the command
    remove_keyboard = telebot.types.ReplyKeyboardRemove()
    bot.send_message(user_id, "How can I assist you now?", reply_markup=remove_keyboard)

def save_tasks(user_id):
    with open(tasks_file, 'a') as file:
        for task in tasks.get(user_id, []):
            file.write(f"{user_id}:{task}\n")

def load_tasks(user_id):
    tasks[user_id] = []
    try:
        with open(tasks_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                parts = line.split(':')
                if len(parts) == 2 and parts[0] == str(user_id):
                    tasks[user_id].append(parts[1])
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    bot.polling(none_stop=True)
