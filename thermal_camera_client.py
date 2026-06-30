'''
THis would run on computer
would ask the pi to connect via a socket
receives one raw data frame from the thermal camera module
make into a 2D array (24x32) using numpy
scale the data with grayscale values 0-255
Interpolate data to make denser pixels for smoother images
use open cv to visualize 2D array in RGB

'''

'''
-import socket python libreary
-create a socket using socket.socket()
-select a port num
-use socket.connect(()'IP', port)) to establish connection with PI
-save data in a buffer to process using socket.recv(BYTENUM).decode()), loop this just like networking, review this
-close socket when done


'''
import os
import numpy
import json
import socket
import cv2


