import telepot

from bot_output import BotOutput
from tasks.base_task import BaseTask
from user import User
from database_helper import DatabaseHelper
from place_data_helper import PlaceDataHelper


class InputCommand(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸入指令"

    def excute(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/start':
                BotOutput.send_plain_text(bot, user, "Hello 我是 Foodge，\n輸入 /help 來瞭解怎麼操\n作我喔 <3")
            elif msg_text == '/help':
                BotOutput.send_plain_text(bot, user, "foodge提供的服務有：\n\n /set - 更改設定\n /advice - 利用問答題幫你挑食物\n /random - 直接幫你選一種食物\n /tourist - 告訴你附近有什麼美食\n /locate - 告訴你它在哪裡")
            elif msg_text == '/set':
                BotOutput.send_plain_text(bot, user, "想要讓foodge屬於你嗎(o´罒`o)\n歡迎使用我們的set功能，\n 只要輸入以下的英文單字，\n就可以客製化你自己的foodge囉!!\n\ndistance－『設定搜尋範圍』，預設是500公尺內。\n\n所以你想要更改什麼設定呢～？")
                user.next_status = '輸入修改參數名'
            elif not user.location:
                BotOutput.send_plain_text(bot, user, "請先將你的位置發給我喔～")
            elif msg_text == '/advise':
                # user.remaining_foods_name = DatabaseHelper.get_all_food_name();
                user.next_status = '連續問答'
            elif msg_text == '/random':
                food_name = DatabaseHelper.get_rand_food()
                user.remaining_foods_name.append(food_name)
                BotOutput.send_plain_text_with_reply_keyboard(bot, user, '你要不要吃 ' + food_name + '呢？', [['要', '不要']])
                user.next_status = '輸出店家清單'
            elif msg_text == '/tourist':
                BotOutput.send_plain_text(bot, user, "我來隨便找找看 ㄏㄏ")
                food_name = DatabaseHelper.get_rand_food()
                user.restaurants = PlaceDataHelper.get_restaurants(user.location, user.distance, food_name)
                BotOutput.send_restaurant_list(bot, user, user.restaurants)
                user.next_status = '輸入店家名稱'
            elif msg_text == '/locate':
                BotOutput.send_plain_text(bot, user, "告訴我一個你想找的食物名稱？")
                user.next_status = '輸入食物名稱'
            else:
                BotOutput.send_plain_text(bot, user, "輸入 /help 獲得幫助")
        else:
            BotOutput.send_plain_text(bot, user, "輸入 /help 獲得幫助")
