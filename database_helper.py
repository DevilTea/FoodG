import pymysql
class DatabaseHelper():

    # connect to db
    db = pymysql.connect("localhost", "e1018e1018", "eric1315", "foodge")

    # create cursor
    cursor = db.cursor()

    # get a random food name
    # return string
    #        if any error occurred, return None, like
    #           no any food in DB
    @staticmethod
    def get_rand_food():
        sql = """SELECT nameFOOD
        FROM food
        ORDER BY RAND()
        LIMIT 1"""

        cursor.excute(sql)
        foodName = cursor.fetchone()
        return foodName

    # check if the food name exist
    # input : string food
    # return boolean
    @staticmethod
    def does_food_name_exist(_food):
        sql = """SELECT
        EXISTS(SELECT * FROM
        food
        WHERE
        nameFOOD = _food)"""
        cursor.excute(sql)
        exist = cursor.fetchone()
        return exist

    # get a list that contain all food names
    # return list<string>
    #        if any error occurred, return None
    #        if no any food in DB, return an empty list
    @staticmethod
    def get_all_food_name():
        all = list()

        count = """SELECT *
        FROM food
        COUNT(*)"""
        cursor.excute(count)
        num = cursor.fetchone()

        for i in range(num):
            sql = """SELECT *
            FROM food
            WHERE nameFOOD"""
            cursor.excute(sql)
            data = cursor.fetchone()
            all.append(data)

        return all

    # check if the food have the tag from input
    # input : string food
    #         string tag
    # return boolen
    #        if any error occurred, return None, like
    #           the food name do not exist
    @staticmethod
    def do_food_have_tag(food, tag):
        pass

    # get all tags of the food name from input
    # input string food
    # return list<string>
    #        if any error occurred, return None
    #        if the food has no tag, return an empty list
    @staticmethod
    def get_all_tags_of_food(food):
        pass
        
    # not necessary
    # # get random tag names in the number of num
    # # input : int num
    # # return list<string>
    # #        if any error occurred, return None
    # @staticmethod
    # def get_rand_tags_list(, num):
    #     pass

    # not necessary
    # # to see how many foods have the tag from input in the foods list
    # # parameter : list<> foods
    # #             string tag
    # # return int
    # #        if any error occurred, return -1
    # @staticmethod
    # def get_num_of_foods_that_have_tag(, foods, tag):
    #     pass

    # not necessary
    # # get all tags that the food have
    # # parameter : list<food>
    # # return list<tuple<string, int>>
    # #        if any error occurred, return None
    # #
    # # example :
    # #   parameter :
    # #       foods = ['炒飯', '炒麵']
    # #   in database :
    # #       food :               tag:                   connection:
    # #           +---+--------+      +----+------+           +----------+
    # #           | id| name   |      | id | name |           |food | tag|
    # #           |---|--------|      |----+------|           |-----+----|
    # #           | 3 | '炒飯' |      | 4  | '熱食' |          | 3   | 4  |
    # #           | 7 | '炒麵' |      | 9  | '飯'   |          | 7   | 4  |
    # #               .               |10 | '麵'   |           | 3   |  9 |
    # #               .                   .                    | 7   |  10|
    # #               .                   .                       .
    # #               .                   .                       .
    # #   return :
    # #       [('熱食', 2) , 
    # #        ('飯'  , 1) ,
    # #        ('麵'  , 1)]       
    # @staticmethod
    # def get_tags_and_counts_of_foods(foods):
    #     pass
