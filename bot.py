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
        # elif content_type == 'sticker':
        #     if msg['sticker']['file_id'] in ['CAADBQADCAADF7xqFrI3Fj2Gc75ZAg',
        #                                      'CAADBQADCwADF7xqFhjJUZGZun80Ag',
        #                                      'CAADBQADDAADF7xqFuNH4B8OGk_rAg']:
        #         bot.sendPhoto(chat_id, 'AgADBQAD3agxG49V4VcI5YK25kdyqyIu1TIABIaCKA1TYOaijAsDAAEC')
        #         bot.sendPhoto(chat_id, 'AgADBQAD3qgxG49V4VfyHlSjhPaNOlNA1jIABCvBWXhpy_GR5AIDAAEC')
        #         bot.sendPhoto(chat_id, 'AgADBQAD4KgxG49V4VeP6Ep7wdkI-I0v1TIABFBpcafNC1UugAUDAAEC')
        #         bot.sendPhoto(chat_id, 'AgADBQAD4agxG49V4VfNpYSCTEQqJelN1TIABFKObaseDY-a9vwCAAEC')
        #         bot.sendPhoto(chat_id, 'AgADBQAD4qgxG49V4VeteSPc-iCtDJhD1jIABNtDEpJxTyXII_oCAAEC')
        #         bot.sendPhoto(chat_id, 'AgADBQAD46gxG49V4VfSW1ntVkAlr-2c1jIABJbBpgrzzFpA2X0BAAEC')
        #         bot.sendPhoto(chat_id, 'AgADBQAD5KgxG49V4VcnU1Ey0SpUqxgw1TIABGkDCO6NG7sNBAgDAAEC')
        #         bot.sendPhoto(chat_id, 'AgADBQAD6KgxG49V4VdFtTCOhPY35BYx1TIABCcZuWydVF6hPQMDAAEC')
        #     elif msg['sticker']['file_id'] == 'CAADBQADAQADF7xqFuFr3IshozvPAg':
        #         bot.sendPhoto(chat_id, 'AgADBQAD5agxG49V4Ve2jp03-BktG8Cs1jIABCQPeXiMP2i4AX4BAAEC')
        #         bot.sendPhoto(chat_id, 'AgADBQAD5qgxG49V4VduuYmO9-NSn0ij1jIABHubaV15DxCC5IIBAAEC')
        #         bot.sendPhoto(chat_id, 'AgADBQAD56gxG49V4VeFMGLg5KQCDNyc1jIABK-lltai5981eoIBAAEC')
        #         bot.sendPhoto(chat_id, 'AgADBQAD6agxG49V4VeDagYzpSI3U00o1TIABPotq2cnpxr50wYDAAEC')
        #         bot.sendPhoto(chat_id, 'AgADBQAD6qgxG49V4VdIgmDmDMrvCXKg1jIABC7rUxLudXCvNIQBAAEC')
        #         bot.sendPhoto(chat_id, 'AgADBQAD66gxG49V4VdUwbWJaibp-O9K1TIABFyiU2EwV9jyif0CAAEC')
        #     elif msg['sticker']['file_id'] == 'CAADBQADDQADF7xqFulLfqNKcL9mAg':
        #         bot.sendMessage(chat_id, '(笑容逐漸母湯)')
        #         bot.sendSticker(chat_id, 'CAADBQADDQADF7xqFulLfqNKcL9mAg')
        #         bot.sendPhoto(chat_id, 'AgADBQAD7KgxG49V4VfqChpBpxGLF02s1jIABL2juZcqHRLTuYMBAAEC')
        #         bot.sendPhoto(chat_id, 'AgADBQAD7agxG49V4VeMkpM7EmJhMPYs1TIABMbGHFBzmYaikgQDAAEC')
        #         bot.sendPhoto(chat_id, 'AgADBQAD7qgxG49V4VcNfCKNXRbu_KSd1jIABNIYnNohQmcUwYEBAAEC')
        elif content_type == 'text':
            if '區塊鏈' in msg['text']:
                bot.sendPhoto(chat_id, 'https://i.imgur.com/qcVrYtG.jpg')
                bot.sendMessage(chat_id, "我不太清楚那是什麼OAO\n不過我知道昨天有教授被滿嘴區塊鏈的高中生氣走喔！")
                bot.sendSticker(chat_id, 'CAADBQADDQADF7xqFulLfqNKcL9mAg')

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
