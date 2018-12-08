#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
def main():
    rospy.init_node('capturing', anonymous=True)
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    height = 480
    width = 640
    camera.resolution = (width, height)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(width, height))
    # allow the camera to warmup
    time.sleep(0.1)       
    image_pub = rospy.Publisher('image', Image, queue_size=1)
    image_msg = Image()
    rate = rospy.Rate(10)
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        image_msg.header.stamp = rospy.get_rostime()
        image_msg.header.frame_id = 'raspicam'
        image_msg.encoding='rgb8'
        image_msg.height=height
        image_msg.width=width
        image_msg.step=width*3
        image_msg.data=image.tostring()
        image_msg.is_bigendian=True 
        image_pub.publish(image_msg)
        rawCapture.truncate(0)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: 
        pass
