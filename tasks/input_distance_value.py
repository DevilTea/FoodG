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
                BotOutput.send_plain_text(bot, user, "foodge提供的服務有：\n\n /set - 更改設定\n /advice - 利用問答題幫你挑食物\n /random - 直接幫你選一種食物\n /tourist - 告訴你附近有什麼美食\n /locate - 告訴你它在哪裡"")
            elif False: # msg_textw.isDigit()
                BotOutput.send_plain_text(bot, user, "趕快檢查一下自己是不是打錯英文單字了OAO\nfoodge提供的服務有：\n\ndistance －『設定搜尋範圍』，預設是500公尺內。\n\n再告訴我一次你想要更改什麼設定呢～？")
            elif False: # 請求輸入正確的參數值、顯示參數型別
                BotOutput.send_plain_text(bot, user, "嘖嘖你數學不好齁，請給我一個“正整數”\n所以你想要的範圍是？（拜託一定必須要是100~1000內正整數～）")
            elif False: # 100 < int(msg_text) < 1000
                BotOutput.send_plain_text(bot, user, "難怪你會沒朋友，就跟你說要“100~1000“內齁\n所以你想要的範圍是？（拜託算我求你，給我個100~1000內正整數吧～）")
            else:
                # user.distance = int(msg_text)
                BotOutput.send_plain_text(bot, user, "設定成功囉(๑´ㅁ`)\nfoodge已經是你的人了(誤)")
            
        else:
            pass
