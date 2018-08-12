import telepot

from bot_output import BotOutput
from place_data_helper import PlaceDataHelper
from tasks.base_task import BaseTask
from user import User


class InputFoodName(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸入食物名稱"

    def excute(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/help':
                pass
            elif msg_text == '/quit':
                user.reset()
            elif True: # database is_food_name_exist(food_name): boolean
                user.restaurants = PlaceDataHelper.get_restaurants(user.location, user.distance, msg_text)
                if len(user.restaurants) > 0:
                    BotOutput.send_restaurant_list(bot, user, user.restaurants)
                    user.next_status = '輸入店家名稱'
                else:
                    BotOutput.send_plain_text(bot, user, "這附近沒有你要的店家！")
                    user.next_status = '輸入指令'
            else:
                # bot_output 食物不存在訊息
                pass
        else:
            pass