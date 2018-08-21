import pymysql
class DatabaseHelper():

    # connect to db
    db = pymysql.connect("localhost", "root", "", "foodge")

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
        cursor = DatabaseHelper.cursor
        cursor.execute(sql)
        foodName = cursor.fetchone()[0]
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
        nameFOOD = '""" + _food + '\')'
        cursor = DatabaseHelper.cursor
        cursor.execute(sql)
        exist = cursor.fetchone()[0]

        if exist is 1:
            return True
        else:
            return False

    # get a list that contain all food names
    # return list<string>
    #        if any error occurred, return None
    #        if no any food in DB, return an empty list
    @staticmethod
    def get_all_food_name():
        all = list()
        sql = """SELECT nameFOOD FROM food"""
        cursor = DatabaseHelper.cursor
        cursor.execute(sql)
        row = cursor.fetchone()[0]

        while row is not None:
            all.append(row)
            temp = cursor.fetchone()
            if temp is None:
                break
            row = temp[0]

        return all

    # check if the food have the tag from input
    # input : string food
    #         string tag
    # return boolen
    #        if any error occurred, return None, like
    #           the food name do not exist
    @staticmethod
    def do_food_have_tag(food, tag):

        attID = """SELECT idATTRIBUTE
        FROM attribute
        WHERE nameATTRIBUTE = '""" + tag + '\''
        cursor = DatabaseHelper.cursor
        cursor.execute(attID)
        tag = cursor.fetchone()[0]

        foodID = """SELECT idFOOD
        FROM food
        WHERE nameFOOD = '""" + food + '\''
        cursor.execute(foodID)
        food = cursor.fetchone()[0]

        sql = """SELECT
                EXISTS(SELECT * 
                FROM food_has_attribute
                WHERE FOOD_idFOOD = %d AND ATTRIBUTE_idATTRIBUTE = %d)""" % (food, tag)
        cursor.execute(sql)
        data = cursor.fetchone()[0]
        return data

    # get all tags of the food name from input
    # input string food
    # return list<string>
    #        if any error occurred, return None
    #        if the food has no tag, return an empty list
    @staticmethod
    def get_all_tags_of_food(food):
        alltag = list()

        tag = """SELECT nameATTRIBUTE
        FROM attribute, food_has_attribute, food
        WHERE food.nameFOOD = '""" + food + "\'" + """AND
        food.idFOOD = food_has_attribute.FOOD_idFOOD AND
        food_has_attribute.ATTRIBUTE_idATTRIBUTE = attribute.idATTRIBUTE """
        cursor = DatabaseHelper.cursor
        cursor.execute(tag)
        row = cursor.fetchone()[0]

        while row is not None:
            alltag.append(row)
            temp = cursor.fetchone()
            if temp is None:
                break
            row = temp[0]

        return alltag


    #get the statement by tag
    @staticmethod
    def get_the_statement_by_tag(tag):
        sql = """SELECT statement
                FROM attribute
                WHERE nameATTRIBUTE = '""" + tag + '\''
        cursor = DatabaseHelper.cursor
        cursor.execute(sql)
        data = cursor.fetchone()[0]
        return data

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
