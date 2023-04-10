import paho.mqtt.client as mqtt
#pip3 install paho-mqtt

payload="Hello"
topic="IOT/test"
client = mqtt.Client()
client.connect('35.244.58.37',1883,60)
(rc,mid)=client.publish(topic,payload);
client.disconnect();
