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
    def edit_plain_text_with_inline_keyboard(bot, user, toedit, text, inline_keyboard_matrix):
        reply_markup = InlineKeyboardMarkup(
            inline_keyboard=inline_keyboard_matrix)
        return bot.editMessageText(telepot.message_identifier(toedit), text, reply_markup=reply_markup,
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
        restaurants = list(restaurants.values())
        if user.sortby == 'distance':
            restaurants.sort(key=lambda restaurant: restaurant['distance'])
            for restaurant in restaurants:
                temp.append(InlineKeyboardButton(
                    text=restaurant['name'] + "\n - 距離約" + str(restaurant['distance']) + "m", callback_data=restaurant['name']))
        elif user.sortby == 'rating':
            restaurants.sort(
                key=lambda restaurant: restaurant['rating'], reverse=True)
            for restaurant in restaurants:
                temp.append(InlineKeyboardButton(
                    text=restaurant['name'] + "\n - 評分" + str(restaurant['rating']) + "⭐️", callback_data=restaurant['name']))

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

        if not user.saved_yesno2_message:
            return BotOutput.send_plain_text_with_inline_keyboard(
                bot, user, text, inline_keyboard_matrix)
        else:
            return BotOutput.edit_plain_text_with_inline_keyboard(
                bot, user, user.saved_yesno2_message, text, inline_keyboard_matrix)

    @staticmethod
    def sendSticker(bot, user, sticker_id):
        bot.sendSticker(user, sticker_id)
    
    @staticmethod
    def sendPhoto(bot, user, photo_id):
        bot.sendPhoto(user, photo_id)
