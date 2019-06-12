from cv2 import cv2
import numpy as np
import socket
import sys
import pickle
import struct 
import threading

def display():
    while True:
        ret,frame=cap.read()
        cv2.imshow('your_frame',frame)
        key = cv2.waitKey(10)
        if (key == 27) or (key == 113):
            break 

cap=cv2.VideoCapture(0)
uploader=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
uploader.connect(('localhost',8089))
t = threading.Thread(target = display)
t.start()
while True:
    ret,frame=cap.read()
    data = pickle.dumps(frame) 
    uploader.sendall(struct.pack("L", len(data))+data) 
    