import telepot

from bot_output import BotOutput
from tasks.base_task import BaseTask
from user import User


class InputCommand(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸入指令"

    def excute(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/help':
                pass
            elif msg_text == '/advise':
                # user.next_status = '連續問答'
                pass
            elif msg_text == '/random':
                # user.next_status = '輸出店家清單'
                pass
            elif msg_text == '/tourist':
                # user.next_status = '輸入店家名稱'
                pass
            elif msg_text == '/locate':
                if user.location:
                    BotOutput.send_plain_text(bot, user, "你想要查詢什麼食物呢？")
                    user.next_status = '輸入食物名稱'
                else:
                    BotOutput.send_plain_text(bot, user, "請先將你的位置發給我喔～")
            elif msg_text == '/set':
                # user.next_status = '輸入修改參數名'
                pass
            else:
                pass