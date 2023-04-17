#Python Program to input data to mysql database
#Import pymysql module library
import pymysql
#Create a connection to MySQL Database 
conn =pymysql.connect(database="AdithyaDB1",user="adithya",password="akm",host="localhost")
#Create a MySQL Cursor to that executes the SQLs
cur=conn.cursor()
#Create a dictonary
data={'topic':'sensortemp','mydata':36.0}
#Execute the SQL to write data to the database
cur.execute("INSERT INTO table2(topic, mydata)VALUES(%(topic)s,%(mydata)s);",data)
#Close the cursor
#cur.close()
#Commit the data to the database
conn.commit()
#Close the connection to the database
conn.close()

#Open phpMyAdmin and see how the data is stored to the database
