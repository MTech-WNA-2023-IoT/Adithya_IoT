
import paho.mqtt.client as paho
#pip3 install paho-mqtt
global mqttclient;
global broker;
global port;

broker = "34.93.71.238";
port = 1883;

client_uniq = "pubclient_123"

mqttclient = paho.Client(client_uniq, True) 

def test(client, userdata, message):
  print("client:"+ client)
  print("userdata:"+ userdata)
  print("message:"+ message)

def _on_message(client, userdata, msg):
# 	print("Received: Topic: %s Body: %s", msg.topic, msg.payload)
	print(msg.topic+" "+str(msg.payload))
 
import pymysql
#Create a connection to MySQL Database 
conn =pymysql.connect(database="AdithyaDB1",user="adithya",password="akm",host="localhost")
#Create a MySQL Cursor to that executes the SQLs
cur=conn.cursor()
#Create a dictonary
data={'topic':'sensortemp','mydata':21.0}
#Execute the SQL to write data to the database
cur.execute("INSERT INTO table2(topic, mydata)VALUES(%(topic)s,%(mydata)s);",data)
#Close the cursor
#cur.close()
#Commit the data to the database
conn.commit()
#Close the connection to the database
conn.close()

#Subscribed Topics 
def _on_connect(mqttclient, userdata, flags, rc):
# 	print("New Client: "+str(mqttclient)+ " connected")
# 	print(rc)
	mqttclient.subscribe("IOT/#", qos=0)	
  
mqttclient.message_callback_add("IOT/test", test)

mqttclient.connect(broker, port, keepalive=1, bind_address="")
  
mqttclient.on_connect = _on_connect

mqttclient.loop_forever()
