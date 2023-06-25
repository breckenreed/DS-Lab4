import flask
import pika
import threading

msg = []
msg_lock = threading.Lock()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/messages', methods=['GET'])

def message():
    global msg
    if len(msg) == 0:
        return "Insufficient messages count"
    with msg_lock:
        wiped_msg = msg.copy()
        msg.clear()    
    return ','.join(wiped_msg)
    
def queue():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.18.0.11'))
    channel = connection.channel()
    channel.queue_declare(queue='LAB4')

    def callback(ch, method, properties, body):
        global msg
        with msg_lock:
            msg.append(body.decode())
        print(" [x] Received %r" % body.decode())
        print (','.join(msg))

    channel.basic_consume(queue='LAB4', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    queue_thread = threading.Thread(target = queue)
    queue_thread.start()
    app.run(host='0.0.0.0', port='8021')
    
