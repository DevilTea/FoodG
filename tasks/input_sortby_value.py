import telepot

from bot_output import BotOutput
from place_data_helper import PlaceDataHelper
from tasks.base_task import BaseTask
from user import User


class InputSortbyValue(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸入排序依據"

    def on_chat(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/help':
                BotOutput.send_plain_text(
                    bot, user, "ლ(´•д• ̀ლ必須要是 distance 或是 rating，預設是 distance。")
            elif msg_text == '/quit':
                BotOutput.send_plain_text(bot, user, "好吧那...需要再叫我囉(ouo)")
                BotOutput.sendSticker(bot, user, 'CAADBQADAQADF7xqFuFr3IshozvPAg')
                user.reset()
            elif msg_text != 'distance' and msg_text != 'rating':
                BotOutput.send_plain_text(
                    bot, user, "難怪你會沒朋友，就跟你說要 distance 或是 rating 齁\n所以你想要的範圍是？（拜託算我求你，給我 distance 或是 rating 吧～）")
                BotOutput.sendSticker(bot, user, 'CAADBQADDAADF7xqFuNH4B8OGk_rAg')
            else:
                user.sortby = msg_text
                BotOutput.send_plain_text(
                    bot, user, "設定成功囉(๑´ㅁ`)\nfoodge已經是你的人了(誤)")
                user.reset()
        else:
            BotOutput.send_plain_text(bot, user, "輸入 /help 獲得幫助")

    def on_callback_query(self, bot, user, msg):
        pass

    def on_inline_query(self, bot, user, msg):
        pass

    def on_chosen_inline_result(self, bot, user, msg):
        pass
