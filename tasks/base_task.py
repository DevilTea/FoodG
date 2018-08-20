class BaseTask():
    def __init__(self):
        pass

    def is_enable(self, user, msg):
        pass

    def on_chat(self, bot, user, msg):
        pass

    def on_callback_query(self, bot, user, msg):
        pass

    def on_inline_query(self, bot, user, msg):
        pass

    def on_chosen_inline_result(self, bot, user, msg):
        pass
