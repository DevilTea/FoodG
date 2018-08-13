class User():
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.location = None
        self.distance = 500
        self.status = '輸入指令'
        self.next_status = '輸入指令'
        self.temp_tag = None
        self.remaining_foods_name = []
        self.restaurants = {}

    def update_status(self):
        self.status = self.next_status

    def reset(self):
        self.status = '輸入指令'
        self.next_status = '輸入指令'
        self.temp_tag = None
        self.remaining_foods_name = []
        self.food_name_to_search = None
        self.restaurants = {}