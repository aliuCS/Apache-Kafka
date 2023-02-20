import time
import cv2
from kafka import KafkaProducer

# Connect to Kafka
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Assign a topic
topic = 'my-topic'

def video_emitter(video):
    # Open the video
    video = cv2.VideoCapture(video)
    print('emitting.....')

    # Read the file
    while video.isOpened():
        # Read the image in each frame
        success, image = video.read()
        # Check if the file has read to the end
        if not success:
            break
        # Convert the image to PNG
        ret, jpeg = cv2.imencode('.png', image)
        # Convert the image to bytes and send to Kafka
        producer.send(topic, jpeg.tobytes())
        # To reduce CPU usage create sleep time of 0.2sec  
        time.sleep(0.2)
        
    # Clear the capture
    video.release()
    print('done emitting')

video_emitter('https://www.youtube.com/watch?v=WXsD0ZgxjRw')

