import telepot

from bot_output import BotOutput
from place_data_helper import PlaceDataHelper
from tasks.base_task import BaseTask
from user import User


class InputParameterName(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸入修改參數名"

    def on_chat(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/help':
                BotOutput.send_plain_text(
                    bot, user, "foodge提供的可自訂參數有：\n" + \
                                "\n distance －『設定搜尋範圍(m)』，必須要是100~1000內正整數，預設是500公尺。" + \
                                "\n sortby －『設定店家排序依據』，必須要是 distance 或是 rating，預設是 distance。")
            elif msg_text == '/quit':
                BotOutput.send_plain_text(bot, user, "好吧那...需要再叫我囉(ouo)")
                BotOutput.sendSticker(bot, user, 'CAADBQADCQADF7xqFircCNnjOCp4Ag')
                user.reset()
            elif msg_text == 'distance':
                BotOutput.send_plain_text(
                    bot, user, "請輸入你要的搜尋距離喔～！必須要是100~1000內正整數")
                user.next_status = "輸入距離"
            elif msg_text == 'sortby':
                BotOutput.send_plain_text(
                    bot, user, "請輸入你要的店家排序依據喔～！必須要是 distance 或是 rating")
                user.next_status = "輸入排序依據"
            else:
                BotOutput.send_plain_text(bot, user, "輸入 /help 獲得幫助")
                BotOutput.sendSticker(bot, user, 'CAADBQADDAADF7xqFuNH4B8OGk_rAg')
        else:
            BotOutput.send_plain_text(bot, user, "輸入 /help 獲得幫助")
            BotOutput.sendSticker(bot, user, 'CAADBQADDAADF7xqFuNH4B8OGk_rAg')

    def on_callback_query(self, bot, user, msg):
        pass

    def on_inline_query(self, bot, user, msg):
        pass

    def on_chosen_inline_result(self, bot, user, msg):
        pass
