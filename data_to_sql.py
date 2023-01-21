import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

empdata = pd.read_csv('us-500.csv', index_col=False, delimiter = ',')
empdata.head()

try:
    # give your own DB details 
    conn = mysql.connect(host='localhost', database='employee', user='root', password='*******')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS employee_data;')
        print('Creating table....')
        
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO employee.employee_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)
    
