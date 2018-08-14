import telepot

from bot_output import BotOutput
from tasks.base_task import BaseTask
from user import User
from database_helper import DatabaseHelper


class InputCommand(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸入指令"

    def excute(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/help':
                BotOutput.send_plain_text(bot, user, "foodge提供的服務有：\n\n /set - 更改設定\n /advice - 利用問答題幫你挑食物\n /random - 直接幫你選一種食物\n /tourist - 告訴你附近有什麼美食\n /locate - 告訴你它在哪裡"")
            elif msg_text == '/advise':
                # user.next_status = '連續問答'
                # user.remaining_foods_name = DatabaseHelper.get_all_food_name();
                pass
            elif msg_text == '/random':
                # user.next_status = '輸出店家清單'
                # user.remaining_foods_name.append(DatabaseHelper.get_rand_food())
                pass
            elif msg_text == '/tourist':
                # user.next_status = '輸入店家名稱'
                pass
            elif msg_text == '/locate':
                if user.location:
                    BotOutput.send_plain_text(bot, user, "告訴我一個你想找的食物名稱？")
                    user.next_status = '輸入食物名稱'
                else:
                    BotOutput.send_plain_text(bot, user, "請先將你的位置發給我喔～")
            elif msg_text == '/set':
                # BotOutput.send_plain_text(bot, user, "想要讓foodge屬於你嗎(o´罒`o)\n 歡迎使用我們的set功能，\n 只要輸入以下的英文單字，就可以客製化你自己的foodge囉!!\n\n distance －『設定搜尋範圍』，預設是500公尺內。\n\n所以你想要更改什麼設定呢～？")
                # user.next_status = '輸入修改參數名'
                pass
            else:
                pass
