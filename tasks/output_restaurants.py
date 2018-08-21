import telepot
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup

from tasks.base_task import BaseTask
from user import User
from bot_output import BotOutput
from place_data_helper import PlaceDataHelper
from database_helper import DatabaseHelper


class OutputRestaurants(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸出店家清單"

    def on_chat(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/quit':
                BotOutput.send_plain_text(bot, user, "好吧那...需要再叫我囉(ouo)")
                user.reset()
            else:
                BotOutput.send_plain_text(bot, user, "請告訴我「要」或「不要」喔 (ㆆᴗㆆ)و")
        else:
            BotOutput.send_plain_text(bot, user, "請告訴我「要」或「不要」喔 (ㆆᴗㆆ)و")

    def on_callback_query(self, bot, user, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        if query_data == 'yes':
            BotOutput.send_plain_text(bot, user, "我來找找看～")
            BotOutput.sendSticker(bot, user, 'CAADBQADBQADF7xqFpLLOHDNKtayAg')
            food_name = user.remaining_foods_name[0]
            user.restaurants = PlaceDataHelper.get_restaurants(
                user.location, user.distance, food_name)
            if len(user.restaurants) > 1:
                BotOutput.send_restaurant_list(bot, user, user.restaurants)
                user.next_status = '輸入店家名稱'
            else:
                BotOutput.send_plain_text_remove_reply_keyboard(bot, user, "這附近沒有你要的店家！\n我在幫你 random 一下好了")
                food_name = DatabaseHelper.get_rand_food()
                user.remaining_foods_name = [food_name]
                BotOutput.sendYesNo(bot, user, '你要不要吃 ' + food_name + '呢？')
        elif query_data == 'no':
            BotOutput.send_plain_text(bot, user, "好吧那...需要再叫我囉(ouo)")
            BotOutput.sendSticker(bot, user, 'CAADBQADCwADF7xqFhjJUZGZun80Ag')
            user.reset()

    def on_inline_query(self, bot, user, msg):
        pass

    def on_chosen_inline_result(self, bot, user, msg):
        pass
