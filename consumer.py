from flask import Flask, Response
from kafka import KafkaConsumer
import cv2
import numpy as np

# connect to Kafka server and pass the topic we want to consume
consumer = KafkaConsumer('my-topic', group_id='view', bootstrap_servers=['localhost:9092'])

# Continuously listen to the connection and print messages as received
app = Flask(__name__)

@app.route('/')
def index():
    # return a multipart response
    return Response(kafka_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed')
def video_feed():
    return Response(kafka_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

def kafka_stream():
    for msg in consumer:
        # Read the message as an image using OpenCV
        nparr = np.frombuffer(msg.value, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # Convert the image to JPEG and yield it to the client
        ret, jpeg = cv2.imencode('.jpg', img)
        yield (b'--frame\r\n'
               b'Content-Type: image/png\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
