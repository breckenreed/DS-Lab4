import requests
import json
import flask
import uuid
import pika
import random

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))

def forward_get():
    port_logging = str(8010+random.randint(1,3))
    port_message = str(8020+random.randint(1,2))
    messag_url = "http://127.0.0.1:%s"%port_message
    logs_url = "http://127.0.0.1:%s"%port_logging

    print("...Sending GET to logging service...")
    uuid_make = {
            "uuid":str(uuid.uuid4()),
            "msg":flask.request.json.get('msg')
        }
    logs_response = requests.get(
        "{msg}/logging".format(msg=logs_url),
        json = uuid_make
    )
    print('1. Received response to GET from logging service:', logs_response.content)    

    msg_response = requests.get(
        "{msg}/messages".format(msg=messag_url),
        json = uuid_make
    )
    print('2. Received response to GET from message service:', msg_response.text)
    return msg_response.text

def forward_post():
    port_logging = str(8010+random.randint(1,3))
    logs_url = "http://127.0.0.1:%s"%port_logging
    print("...Sending POST to logging service...")
    try:
        uuid_make = {
            "uuid":str(uuid.uuid4()),
            "msg":flask.request.json.get('msg')
        }
        logs_response = requests.post(
            "{msg}/logging".format(msg=logs_url),
           json = uuid_make
        )
        status = logs_response.status_code
        print('1. Received response to POST from logging service:', status)

        channel = connection.channel()
        channel.queue_declare(queue='LAB4')

        channel.basic_publish(exchange='', routing_key='LAB4', body=flask.request.json.get('msg'))
        print(f" [x] Sent to message queue: %s"%flask.request.json.get('msg'))
        connection.close()

        return app.response_class()

    except Exception as ex:
        raise ex
        flask.abort(400)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET','POST'])
def facade_serv():
    if flask.request.method == 'GET':
        return forward_get()
    elif flask.request.method == 'POST':
        return forward_post()
    else:
        flask.abort(405)

app.run(host='0.0.0.0', port='8000')
