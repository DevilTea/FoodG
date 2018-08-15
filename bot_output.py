import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove

from util import Util


class BotOutput():
    @staticmethod
    def send_plain_text(bot, user, text):
        reply_markup = ReplyKeyboardRemove()
        bot.sendMessage(user.chat_id, text, reply_markup=reply_markup,
                        disable_web_page_preview=True)

    @staticmethod
    def send_markdown_text(bot, user, text):
        reply_markup = ReplyKeyboardRemove()
        bot.sendMessage(user.chat_id, text, parse_mode="Markdown", reply_markup=reply_markup,
                        disable_web_page_preview=True)

    @staticmethod
    def send_plain_text_with_reply_keyboard(bot, user, text, reply_keyboard_matrix):
        reply_markup = ReplyKeyboardMarkup(
            keyboard=reply_keyboard_matrix, resize_keyboard=True)
        bot.sendMessage(user.chat_id, text, reply_markup=reply_markup,
                        disable_web_page_preview=True)

    @staticmethod
    def send_restaurant_info(bot, user, restaurant):
        info_url = "https://www.google.com/maps/search/?api=1&query=" + \
                    restaurant['name'] + \
                    "&query_place_id=" + \
                    restaurant['place_id']
        distance = "約 " + str(int(Util.getDistance(user.location, restaurant['location']))) + " 公尺"
        BotOutput.send_markdown_text(bot, user, 
            "Foodge找到了～\n\n" + \
            "🍽店名🍽 \t" + restaurant['name'] + "\n\n" + \
            "💡評分💡 \t" + str(restaurant['rating']) + "\n\n" + \
            "🗺地址🗺 \t" + restaurant['vicinity'] + "\n\n" + \
            "📍距離📍 \t" + distance + "\n\n" + \
            "[➡️點擊開啟 Google Map⬅️](" + info_url + ")"
        )

    @staticmethod
    def send_restaurant_list(bot, user, restaurants):
        reply_keyboard_matrix = []
        for name in restaurants.keys():
            reply_keyboard_matrix.append([name])
        reply_keyboard_matrix.append(['算了當我沒說'])
        BotOutput.send_plain_text_with_reply_keyboard(bot, user, "選一家店吧！", reply_keyboard_matrix)
