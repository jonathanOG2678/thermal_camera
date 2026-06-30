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

'''
-try to create a socket using socket.socket()
-set up port for communication
-set up connection with the PI

while True:
    -call to recv() to get data from the PI, in pieces and save as frame here
    -reshape the frame array into 24x32 using numpy.reshape()
    -smoothen current frame to blend in with previous frame
    -Normalize values into 0-255 grayscale values
    -interpolates the frame data to a larger image
    -convert frame data from grayscale to RGB/BGR using opencv (image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
)
    -call imshow() to update the frame of image

-BreakAllwindows() to close opencv image viewer
-close socket using socket.close()


'''


'''
### A possible way to reveive data until no data is left, have an escape character at end of frame data ###
int recvall(int s, char *buf, int *len)
{
	int total = 0;
	int bytesleft = *len;
	int n;

	while(total < *len)
	{
		n = recv(s, buf + total, bytesleft, 0);
		if (n == -1)
		 {
			break;
		 } else if(n == 0 )
		 {
			break;
		 }
		total += n;
		bytesleft -= n;
	

	}

	*len = total;

	
	return n ==-1?-1:0;
}
'''
