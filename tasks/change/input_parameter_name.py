import telepot

from bot_output import BotOutput
from place_data_helper import PlaceDataHelper
from tasks.base_task import BaseTask
from user import User

class InputParameterName(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸入修改參數名"

    def excute(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/help':
                BotOutput.send_plain_text(bot, user, "foodge提供的服務有：\n\n /set - 更改設定\n /advice - 利用問答題幫你挑食物\n /random - 直接幫你選一種食物\n /tourist - 告訴你附近有什麼美食\n /locate - 告訴你它在哪裡"")
            elif msg_text == 'distance':
                user.status = "輸入距離"
            else:
                pass
        else:
            pass
