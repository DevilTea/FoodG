import telepot

from bot_output import BotOutput
from place_data_helper import PlaceDataHelper
from tasks.base_task import BaseTask
from user import User


class InputRestaurantName(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸入店家名稱"

    def excute(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/help':
                pass
            elif msg_text == '/quit':
                BotOutput.send_plain_text(bot, user, "這樣知道要吃什麼了吧～需要幫忙再叫我齁(ouo)")
                user.reset()
            elif msg_text == '算了當我沒說':
                BotOutput.send_plain_text(bot, user, "對不起嗚嗚foodge幫不上忙啊啊啊(;´༎ຶД༎ຶ`)\n如果原諒我的話隨時可以叫我(´༎ຶД༎ຶ`;)")
                BotOutput.sendSticker(bot, user, 'CAADBQADBwADF7xqFh0D0ccnyeM3Ag')
                user.reset()
            elif PlaceDataHelper.is_restaurant_name_exist(msg_text, user.restaurants):
                restaurant = PlaceDataHelper.get_restaurant_by_name(
                    msg_text, user.restaurants)
                BotOutput.send_restaurant_info(bot, user, restaurant)

                BotOutput.send_plain_text(bot, user, "還想再看其他店嗎？")
                BotOutput.send_restaurant_list(bot, user, user.restaurants)
                # user.next_status = '輸入指令'
            else:
                BotOutput.send_plain_text(bot, user, "不存在的店家名稱，再來一次")
                BotOutput.sendSticker(bot, user, 'CAADBQADBwADF7xqFh0D0ccnyeM3Ag')
                BotOutput.send_restaurant_list(bot, user, user.restaurants)
        else:
            pass
