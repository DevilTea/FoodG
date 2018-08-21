import telepot

from bot_output import BotOutput
from place_data_helper import PlaceDataHelper
from database_helper import DatabaseHelper
from tasks.base_task import BaseTask
from user import User


class InputFoodName(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸入食物名稱"

    def on_chat(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/quit':
                BotOutput.send_plain_text(bot, user, "好吧那...需要再叫我囉(ouo)")
                BotOutput.sendSticker(bot, user, 'CAADBQADCQADF7xqFircCNnjOCp4Ag')
                user.reset()
            else:
                if DatabaseHelper.does_food_name_exist(msg_text):
                    BotOutput.send_plain_text(bot, user, "我來找找看～")
                else:
                    BotOutput.send_plain_text(
                        bot, user, "雖然我不太確定你說的東西，但讓我來找找看～")
                    BotOutput.sendSticker(bot, user, 'CAADBQADBgADF7xqFjTecVxyW5ITAg')
                user.restaurants = PlaceDataHelper.get_restaurants(
                    user.location, user.distance, msg_text)
                if len(user.restaurants) > 1:
                    BotOutput.send_restaurant_list(bot, user, user.restaurants)
                    user.next_status = '輸入店家名稱'
                else:
                    BotOutput.send_plain_text(bot, user, "這附近沒有你要的店家！")
                    BotOutput.send_plain_text(bot, user, "你想要再查詢什麼食物呢？")
        else:
            BotOutput.send_plain_text(bot, user, "你想要再查詢什麼食物呢？")

    def on_callback_query(self, bot, user, msg):
        pass

    def on_inline_query(self, bot, user, msg):
        pass

    def on_chosen_inline_result(self, bot, user, msg):
        pass
