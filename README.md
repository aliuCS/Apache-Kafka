# Apache-Kafka

 Uses Apache Kafka to build a distributed messaging system that can handle large volumes of real-time data streams. With Kafka, you can publish and subscribe to streams of records, process them in real-time, and store and operate them without interuption.

The project includes the following components:

Producer: A Python script that generates simulated video frames and sends them to Kafka as messages. 

Consumer: Also written in Python that reads messages from Kafka and decodes the video frames to display them on the console. The frames are displayed as images using the OpenCV library.

Web application: A Flask web application that streams the video frames in real-time over HTTP to send a continuous stream of data to the client, such as video or a sequence of images by sending snippets of data as separate pieces. Replacing and swtiching in new ones, allowing users to display data in real-time without requesting updates. The frames are read from Kafka by the web server and sent to the client browser as they arrive.