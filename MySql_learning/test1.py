import mysql.connector

try:
    with open('Password.txt', 'r') as get_file_info:
        passwd = get_file_info.read()
except FileNotFoundError as file_err:
    print('Error occurred while opening file!: ', file_err)

mydb_dic = {
    "host": "localhost",
    "passwd": passwd,
    "user": "root"
}

try:
    with mysql.connector.connect(**mydb_dic) as get_access:
        my_cursor = get_access.cursor()
        
        my_cursor.execute('CREATE DATABASE IF NOT EXISTS user_info')
        # print('Database created successfully')
        
        # my_cursor.execute("USE user_info")
        
        my_cursor.execute("SELECT * FROM user_info")

        for x in my_cursor:
            print(x)

except mysql.connector.Error as err:
    print(f"MySQL Connector error: {err}")

# %%
