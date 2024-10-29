from autres_modules.connection_rabbit import get_connection_rabbit
import pika,json

def publish(method,body,key):
    properties = pika.BasicProperties(method)
    channel=get_connection_rabbit()
    channel.basic_publish(exchange="", routing_key=key, body=json.dumps(body), properties=properties)
    channel.close()
   