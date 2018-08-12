import telepot

import bot_output
from tasks.base_task import BaseTask
from user import User


class AnswerQuestions(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "連續問答"

    def excute(self, bot, user, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            msg_text = msg['text']
            if msg_text == '/help':
                pass
            elif msg_text == '/quit':
                user.next_status = '輸入指令'
            elif msg_text == '好':
                pass
            elif msg_text == '不好':
                pass
            elif msg_text == '隨便':
                pass
            else:
                # bot_output 不是要求的回答
                pass

            if True: # is_complete(user): boolean
                # bot_output.ask_whether_list(user): void
                user.next_status = '輸出店家清單'
        else:
            pass