# 原生套件
import time
import json
from pprint import pprint

# 外部套件
import telepot
from telepot.loop import MessageLoop

# 本地套件
from user import User
from tasks.input_command import InputCommand
from tasks.input_food_name import InputFoodName
from tasks.input_restaurant_name import InputRestaurantName
from tasks.answer_questions import AnswerQuestions
from tasks.output_restaurants import OutputRestaurants
from tasks.input_parameter_name import InputParameterName
from tasks.input_distance_value import InputDistanceValue
from tasks.input_sortby_value import InputSortbyValue

BOT_TOKEN = None
with open('./config.json', 'r') as f:
    BOT_TOKEN = json.load(f)['BOT_TOKEN']
    f.close()

users = {}
tasks = [InputCommand(), InputFoodName(), InputRestaurantName(),
         AnswerQuestions(), OutputRestaurants(), InputParameterName(), InputDistanceValue(), InputSortbyValue()]
bot = telepot.Bot(BOT_TOKEN)


def on_chat(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if chat_type == 'private':
        if not users.get(chat_id):
            users[chat_id] = User(chat_id)
        user = users[chat_id]

        if content_type == 'location':
            user.location = msg['location']
            bot.sendMessage(chat_id, "你的位置已更新！")

        for task in tasks:
            if task.is_enable(user, msg):
                task.on_chat(bot, user, msg)

        user.update_status()


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(
        msg, flavor='callback_query')
    if not users.get(from_id):
        users[from_id] = User(from_id)
    user = users[from_id]

    for task in tasks:
        if task.is_enable(user, msg):
            task.on_callback_query(bot, user, msg)
    bot.answerCallbackQuery
    user.update_status()


def on_inline_query(msg):
    pass


def on_chosen_inline_result(msg):
    pass


MessageLoop(bot,
            {
                'chat': on_chat,
                'callback_query': on_callback_query,
                'inline_query': on_inline_query,
                'chosen_inline_result': on_chosen_inline_result
            }
            ).run_as_thread()
print("BOT 動起來")

while True:
    time.sleep(60)
