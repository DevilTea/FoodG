import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

from pprint import pprint

from util import Util


class BotOutput():
    @staticmethod
    def send_plain_text(bot, user, text, reply_markup=None):
        return bot.sendMessage(user.chat_id, text, reply_markup=reply_markup,
                               disable_web_page_preview=True)

    @staticmethod
    def send_markdown_text(bot, user, text, reply_markup=None):
        return bot.sendMessage(user.chat_id, text, parse_mode="Markdown", disable_web_page_preview=True, reply_markup=reply_markup)

    @staticmethod
    def edit_markdown_text(bot, user, toedit, text, reply_markup=None):
        return bot.editMessageText(telepot.message_identifier(toedit), text, parse_mode="Markdown", disable_web_page_preview=True, reply_markup=reply_markup)

    @staticmethod
    def send_plain_text_remove_reply_keyboard(bot, user, text, reply_markup=None):
        r = ReplyKeyboardRemove()
        return BotOutput.send_plain_text(bot, user, text, r)

    @staticmethod
    def send_markdown_text_remove_reply_keyboard(bot, user, text, reply_markup=None):
        r = ReplyKeyboardRemove()
        return BotOutput.send_markdown_text(bot, user, text, r)

    @staticmethod
    def edit_markdown_text_remove_reply_keyboard(bot, user, toedit, text, reply_markup=None):
        r = ReplyKeyboardRemove()
        return BotOutput.edit_markdown_text(bot, user, text, r)

    @staticmethod
    def send_plain_text_with_reply_keyboard(bot, user, text, reply_keyboard_matrix):
        reply_markup = ReplyKeyboardMarkup(
            keyboard=reply_keyboard_matrix, resize_keyboard=True)
        return bot.sendMessage(user.chat_id, text, reply_markup=reply_markup,
                               disable_web_page_preview=True)

    @staticmethod
    def send_plain_text_with_inline_keyboard(bot, user, text, inline_keyboard_matrix):
        reply_markup = InlineKeyboardMarkup(
            inline_keyboard=inline_keyboard_matrix)
        return bot.sendMessage(user.chat_id, text, reply_markup=reply_markup,
                               disable_web_page_preview=True)

    @staticmethod
    def send_restaurant_info(bot, user, restaurant):
        if user.saved_info_message:
            return BotOutput.edit_markdown_text(bot, user, user.saved_info_message, Util.get_restaurant_info_md(user, restaurant))
        else:
            return BotOutput.send_markdown_text(
                bot, user, Util.get_restaurant_info_md(user, restaurant))

    @staticmethod
    def get_restaurant_list(user, restaurants):
        inline_keyboard_matrix = []
        temp = []
        for restaurant in restaurants.values():
            temp.append(InlineKeyboardButton(
                text=restaurant['name'] + " - " + str(int(Util.getDistance(restaurant['location'], user.location))) + "m", callback_data=restaurant['name']))
        temp.append(InlineKeyboardButton(text='算了當我沒說', callback_data='stop'))

        i = 0
        while i < len(temp):
            j = 0
            row = []
            while i < len(temp) and j < 2:
                row.append(temp[i])
                i += 1
                j += 1
            inline_keyboard_matrix.append(row)

        return inline_keyboard_matrix

    @staticmethod
    def send_restaurant_list(bot, user, restaurants):
        inline_keyboard_matrix = BotOutput.get_restaurant_list(
            user, restaurants)
        return BotOutput.send_plain_text_with_inline_keyboard(
            bot, user, "選一家店吧！", inline_keyboard_matrix)

    @staticmethod
    def sendYesNo(bot, user, text):
        inline_keyboard_matrix = [[InlineKeyboardButton(
            text="要", callback_data="yes"), InlineKeyboardButton(text="不要", callback_data="no")]]
        return BotOutput.send_plain_text_with_inline_keyboard(
            bot, user, text, inline_keyboard_matrix)

    @staticmethod
    def sendYesNo2(bot, user, text):
        inline_keyboard_matrix = [[InlineKeyboardButton(text="好", callback_data="yes"), InlineKeyboardButton(
            text="隨便", callback_data="whatever"), InlineKeyboardButton(text="不好", callback_data="no")]]
        return BotOutput.send_plain_text_with_inline_keyboard(
            bot, user, text, inline_keyboard_matrix)
