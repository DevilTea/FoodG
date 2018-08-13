import pymysql

db = pymysql.connect("localhost","e1018e1018","eric1315","foodge" )

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print ("Database version : %s " % data)


sql = """INSERT INTO FOOD(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()

