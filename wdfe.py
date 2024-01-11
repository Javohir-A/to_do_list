import mysql.connector 

mydb = mysql.connector.connect(
    host = 'localhost',
    passwd = 'Javohir2002+',
    user = 'root',
    database = 'test4'
)


my_cursor = mydb.cursor()  

# my_cursor.execute('CREATE DATABASE test4')
# my_cursor.execute('SHOW DATABASES')
my_cursor.execute('CREATE TABLE students (name VARCHAR(25), age INT(10))')

sqlFourmula = "INSERT INTO students (name, age) VALUES (%s, %s)"

student1 = {('Javohir', 21),
            ('Dilshod', 18),
            ('Shavkat', 18)}

my_cursor.executemany(sqlFourmula, student1)

mydb.commit()
# for x in my_cursor:
#     print(x)