import telepot

import bot_output
from tasks.base_task import BaseTask
from user import User
from question_manager import QuestionManager


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
                # QuestionManager.remove_all_food_not_with_tag(user, user.temp_tag)
                pass
            elif msg_text == '不好':
                # QuestionManager.remove_all_food_with_tag(user, user.temp_tag)
                pass
            elif msg_text == '隨便':
                # QuestionManager.add_whatever_tag(user, user.temp_tag)
                pass
            else:
                # bot_output 不是要求的回答
                pass
            # if QuestionManager.is_all_tags_disable(user):
            #     bot_output.too_whatever()
            #     user.reset()

            # if QuestionManager.has_question_completed(user): # is_complete(user): boolean
            #     bot_output.ask_whether_list(user): void
            #     user.next_status = '輸出店家清單'
        else:
            pass