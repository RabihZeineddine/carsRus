# Remember to pip install pymysql or else it will cause errors
import pymysql

def accessDB(sql_script):
    # Database info
    ENDPOINT = "cars-r-us.cn4isacgue1x.us-east-2.rds.amazonaws.com"
    USER = "admin"
    PASSWORD = "CPSC362project"
    DATABASE = "Cars-R-Us"
    try:
        connection = pymysql.connect(
            host=ENDPOINT,
            port=3306,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        cursor = connection.cursor()
        cursor.execute(sql_script)
        output = cursor.fetchall()
        cursor.close()
        connection.close()
        return output
    except pymysql.Error as e:
        print("Error:", e)
