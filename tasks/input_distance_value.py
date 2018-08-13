import telepot

from bot_output import BotOutput
from place_data_helper import PlaceDataHelper
from tasks.base_task import BaseTask
from user import User

class InputDistanceValue(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸入距離"

    def excute(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/help':
                pass
            elif False: # msg_text.isDigit()
                pass
            elif False: # 100 < int(msg_text) < 1000
                pass
            else:
                # user.distance = int(msg_text)
                pass
            
        else:
            pass