import telepot

from bot_output import BotOutput
from tasks.base_task import BaseTask
from user import User
from question_manager import QuestionManager
from database_helper import DatabaseHelper


class AnswerQuestions(BaseTask):
    def is_enable(self, user, msg):
        return user.status == "連續問答"

    def on_chat(self, bot, user, msg):
        pass
    

    def on_callback_query(self, bot, user, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        if query_data == '/quit':
            user.next_status = '輸入指令'
        elif query_data == '好':
            # QuestionManager.remove_all_food_not_with_tag(user, user.temp_tag)
            pass
        elif query_data == '不好':
            # QuestionManager.remove_all_food_with_tag(user, user.temp_tag)
            pass
        elif query_data == '隨便':
            # QuestionManager.add_whatever_tag(user, user.temp_tag)
            pass
        
        # if QuestionManager.is_all_tags_disable(user):
        #     bot_output.too_whatever()
        #     user.reset()
        #     return

        # if QuestionManager.has_question_completed(user):
        #     bot_output.ask_whether_list(user): void
        #     user.next_status = '輸出店家清單'

        user.temp_tag = QuestionManager.get_proper_tag_for_ask(user)
        statment = DatabaseHelper.get_the_statement_by_tag(user.temp_tag)
        if statment == 0:
            BotOutput.sendYesNo2(bot, user, '妳現在想吃' + user.temp_tag + '嗎?')
        elif statment == 1:
            BotOutput.sendYesNo2(bot, user, '覺得' + user.temp_tag + '的食物好嗎?')
        elif statment == 2:
            BotOutput.sendYesNo2(bot, user, '是' + user.temp_tag + '嗎?')
        elif statment == 3:
            BotOutput.sendYesNo2(bot, user, '覺得' + user.temp_tag + '嗎?')
        

    def on_inline_query(self, bot, user, msg):
        pass

    def on_chosen_inline_result(self, bot, user, msg):
        pass