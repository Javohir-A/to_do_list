from telebot import types

def create_menu():
    add_task_btn = types.KeyboardButton('Add Tasks')
    view_tasks_btn = types.KeyboardButton('View Tasks')
    set_reminder_btn = types.KeyboardButton('Set Reminder')
    help_instructions_btn = types.KeyboardButton('Help / Instructions')
    categories_btn = types.KeyboardButton('Categories (if implemented)')
    statistics_btn = types.KeyboardButton('Statistics')
    settings_btn = types.KeyboardButton('Settings')
    language_btn = types.KeyboardButton('Language')
    remove_task_btn = types.KeyboardButton('Remove Task')
    menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_markup.add(add_task_btn, view_tasks_btn, set_reminder_btn, help_instructions_btn,
                    categories_btn, statistics_btn, settings_btn, language_btn,remove_task_btn)

    return menu_markup
