import telepot

from bot_output import BotOutput
from place_data_helper import PlaceDataHelper
from tasks.base_task import BaseTask
from user import User


class InputDistanceValue(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "輸入距離"

    def on_chat(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/help':
                BotOutput.send_plain_text(
                    bot, user, "必須要是 100 ~ 1000 內正整數，預設值為 500(m)")
                BotOutput.sendSticker(bot, user, 'CAADBQADAQADF7xqFuFr3IshozvPAg')
            elif msg_text == '/quit':
                BotOutput.send_plain_text(bot, user, "好吧那...需要再叫我囉(ouo)")
                BotOutput.sendSticker(bot, user, 'CAADBQADCQADF7xqFircCNnjOCp4Ag')
                user.reset()
            elif not msg_text.isdigit():
                BotOutput.send_plain_text(
                    bot, user, "你輸入的不是數字呢！必須要是 100 ~ 1000 內正整數")
                BotOutput.sendSticker(bot, user, 'CAADBQADAwADF7xqFlN7n_Y1L8-AAg')
            elif int(msg_text) < 100 or int(msg_text) > 1000:
                BotOutput.send_plain_text(
                    bot, user, "難怪你會沒朋友，就跟你說要“100~1000“內齁\n所以你想要的範圍是？（拜託算我求你，給我個100~1000內正整數吧～）")
                BotOutput.sendSticker(bot, user, 'CAADBQADAwADF7xqFlN7n_Y1L8-AAg')
            else:
                user.distance = int(msg_text)
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
