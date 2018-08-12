import telepot


from tasks.base_task import BaseTask
from user import User


class OutputRestaurants(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸出店家清單"

    def excute(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/help':
                pass
            elif msg_text == '/quit':
                user.reset()
            elif msg_text == '要':
                # BotOutput.send_restaurants(bot, user)
                user.next_status = '輸入店家名稱'
            elif msg_text == '不要':
                user.next_status = '輸入指令'
            else:
                # BotOutput 不是要求的回答
                pass
        else:
            pass