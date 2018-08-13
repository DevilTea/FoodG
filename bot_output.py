import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove


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
        BotOutput.send_markdown_text(bot, user, 
            "*-=店家資訊=-*\n\n" + \
            "\t\t\t*-=店名=-:*\n\n" + \
            "\t\t\t\t\t\t\t\t\t " + restaurant['name'] + "\n\n" + \
            "\t\t\t*-=地址:=-*\n\n" + \
            "\t\t\t\t\t\t\t\t\t " + restaurant['vicinity'] + "\n\n" + \
            "\t\t\t*-=評分:=-*\n\n" + \
            "\t\t\t\t\t\t\t\t\t " + str(restaurant['rating']) + "\n\n" + \
            "[*在 Google Map 上顯示*](" + info_url + ")"
        )

    @staticmethod
    def send_restaurant_list(bot, user, restaurants):
        reply_keyboard_matrix = []
        for name in restaurants.keys():
            reply_keyboard_matrix.append([name])
        reply_keyboard_matrix.append(['算了當我沒說'])
        BotOutput.send_plain_text_with_reply_keyboard(bot, user, "選一家店吧！", reply_keyboard_matrix)
