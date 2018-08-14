import telepot


from tasks.base_task import BaseTask
from user import User
from bot_output import BotOutput


class OutputRestaurants(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸出店家清單"

    def excute(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        BotOutput.send_plain_text(bot, user, "要不要告訴你它在哪邊、風評如何呀～？")
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/help':
                BotOutput.send_plain_text(bot, user, "foodge提供的服務有：\n\n /set - 更改設定\n /advice - 利用問答題幫你挑食物\n /random - 直接幫你選一種食物\n /tourist - 告訴你附近有什麼美食\n /locate - 告訴你它在哪裡")
            elif msg_text == '/quit':
                user.reset()
            elif msg_text == '要':
                # BotOutput.send_restaurants(bot, user)
                pass
            elif msg_text == '不要':
                user.next_status = '輸入指令'
                pass
            else:
                # BotOutput 不是要求的回答
                BotOutput.send_plain_text(bot, user, "請告訴我「要」或「不要」喔 (ㆆᴗㆆ)و")

        else:
            pass
