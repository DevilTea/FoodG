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
        query_id, from_id, query_data = telepot.glance(
            msg, flavor='callback_query')
        if query_data == '/quit':
            user.next_status = '輸入指令'
        elif query_data == 'yes':
            QuestionManager.remove_all_food_not_with_tag(user, user.temp_tag)
            pass
        elif query_data == 'no':
            QuestionManager.remove_all_food_with_tag(user, user.temp_tag)
            pass
        elif query_data == 'whatever':
            QuestionManager.add_whatever_tag(user, user.temp_tag)
            pass

        if QuestionManager.is_all_tags_disable(user):
            BotOutput.send_plain_text(bot, user, 'e04 什麼都隨便 去用/random啦')
            user.reset()
            return

        if QuestionManager.has_question_completed(user):
            BotOutput.sendYesNo(bot, user, '你要不要吃 ' +
                                user.remaining_foods_name[0] + '呢？')
            user.next_status = '輸出店家清單'
            return

        user.temp_tag = QuestionManager.get_proper_tag_for_ask(user)
        statment = DatabaseHelper.get_the_statement_by_tag(user.temp_tag)
        yesno2_message = None
        if statment == 0:
            yesno2_message = BotOutput.sendYesNo2(bot, user, '妳現在想吃' + user.temp_tag + '嗎?')
        elif statment == 1:
            yesno2_message = BotOutput.sendYesNo2(bot, user, '覺得' + user.temp_tag + '的食物好嗎?')
        elif statment == 2:
            yesno2_message = BotOutput.sendYesNo2(bot, user, '是' + user.temp_tag + '嗎?')
        elif statment == 3:
            yesno2_message = BotOutput.sendYesNo2(bot, user, '覺得' + user.temp_tag + '嗎?')
        user.saved_yesno2_message = yesno2_message

    def on_inline_query(self, bot, user, msg):
        pass

    def on_chosen_inline_result(self, bot, user, msg):
        pass
