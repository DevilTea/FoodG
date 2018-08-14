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
                BotOutput.send_plain_text(bot, user, "foodge提供的服務有：\n\n /set - 更改設定\n /advice - 利用問答題幫你挑食物\n /random - 直接幫你選一種食物\n /tourist - 告訴你附近有什麼美食\n /locate - 告訴你它在哪裡")
            elif msg_text == '/quit':
                BotOutput.send_plain_text(bot, user, "好吧那...需要再叫我囉(ouo)")
                user.reset()
            elif True: # database is_food_name_exist(food_name): boolean
                BotOutput.send_plain_text(bot, user, "我來找找看～")
                user.restaurants = PlaceDataHelper.get_restaurants(user.location, user.distance, msg_text)
                if len(user.restaurants) > 0:
                    BotOutput.send_restaurant_list(bot, user, user.restaurants)
                    user.next_status = '輸入店家名稱'
                else:
                    BotOutput.send_plain_text(bot, user, "這附近沒有你要的店家！")
                    BotOutput.send_plain_text(bot, user, "你想要再查詢什麼食物呢？")
                    # user.next_status = '輸入指令'
            else:
                # bot_output 食物不存在訊息
                # BotOutput.send_plain_text(bot, user, "見識淺薄的foodge不知道這個食物欸｡ﾟヽ(ﾟ´Д`)ﾉﾟ｡\n換種食物或是換個說法告訴我吧！\n\n所以你想找的食物是？")
                pass
        else:
            pass
