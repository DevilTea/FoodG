import telepot


from tasks.base_task import BaseTask
from user import User
from bot_output import BotOutput
from place_data_helper import PlaceDataHelper


class OutputRestaurants(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸出店家清單"

    def excute(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/quit':
                BotOutput.send_plain_text(bot, user, "好吧那...需要再叫我囉(ouo)")
                user.reset()
            elif msg_text == '要':
                food_name = user.remaining_foods_name[0]
                user.restaurants = PlaceDataHelper.get_restaurants(user.location, user.distance, food_name)
                BotOutput.send_plain_text(bot, user, "我來找找看～")
                BotOutput.send_restaurant_list(bot, user, user.restaurants)
                user.next_status = '輸入店家名稱'
            elif msg_text == '不要':
                BotOutput.send_plain_text(bot, user, "好吧那...需要再叫我囉(ouo)")
                user.reset()
            else:
                BotOutput.send_plain_text(bot, user, "請告訴我「要」或「不要」喔 (ㆆᴗㆆ)و")
        else:
            BotOutput.send_plain_text(bot, user, "請告訴我「要」或「不要」喔 (ㆆᴗㆆ)و")
