import pika
def get_connection_rabbit():
    credentials = pika.PlainCredentials('raphael_rabbit', 'raphael7')
    connection_params = pika.ConnectionParameters(host='172.30.79.83', credentials=credentials)
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    return channel