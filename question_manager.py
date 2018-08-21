import trace
import random

from database_helper import DatabaseHelper
from user import User

class QuestionManager():

    @staticmethod
    def has_question_completed(user):
        if len(user.remaining_foods_name) == 0:
            return 2
        return len(user.remaining_foods_name) == 1

    @staticmethod
    def remove_all_food_with_tag(user, tag):
        l = len(user.remaining_foods_name)
        user.remaining_foods_name = [x for x in user.remaining_foods_name
                                     if not DatabaseHelper.do_food_have_tag(x, tag)]
        if len(user.remaining_foods_name) == l:
            return None

    @staticmethod
    def remove_all_food_not_with_tag(user, tag):
        l = len(user.remaining_foods_name)
        user.remaining_foods_name = [x for x in user.remaining_foods_name
                                     if DatabaseHelper.do_food_have_tag(x, tag)]
        if len(user.remaining_foods_name) == l:
            return None

    @staticmethod
    def get_proper_tag_for_ask(user):
        l = len(user.remaining_foods_name)
        tmp_tags = {}
        for x in user.remaining_foods_name:
            tags = DatabaseHelper.get_all_tags_of_food(x)
            for y in tags:
                if y in user.not_ask_tags:
                    continue
                if not tmp_tags.get(y):
                    tmp_tags[y] = 0
                tmp_tags[y] += 1
        if len(tmp_tags) == 0:
            return None

        re = random.choice(list(tmp_tags.keys()))
        for key, value in tmp_tags.items():
            re = key if abs(value - (l / 2)) < abs(tmp_tags[re] - (l / 2)) else re
        return re

    @staticmethod
    def is_all_tags_disable(user):
        for x in user.remaining_foods_name:
            tags = DatabaseHelper.get_all_tags_of_food(x)
            for y in tags:
                if y not in user.not_ask_tags:
                    return False
        return True

    @staticmethod
    def add_whatever_tag(user, tag):
        if tag in user.not_ask_tags:
            return
        user.not_ask_tags.append(tag)
        
    @staticmethod
    def get_rand_food():
        return DatabaseHelper.get_rand_food()