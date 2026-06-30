'''
-This would be run on the pi venv
-It would set up the connection betwen the pi and the thermal camera module
-Test to ensure there is proper communcation between pi and camera module
-Create a socket for listening and binding computer with the pi
-Establish connection
-Create packets to send camera module raw data array
'''

'''
-Uses socket python library
-Uses adafruit mlx library

-try to create a socket using socket.socket()
-set up port for communication
-bind the socket and port using socket.bind()
-listen for any connections using socket.listen()

while True loop to send and accept data
    -use socket.accept() which creates receives a fd and address
    -convert data buffer to network order
    -use fd.send() to send data, example uses send('MESSAGE'.encode()) tosend byte type
    -use fd.close() to close sockcet
    -break out of while loop



'''
import socket
import time
import os
import board
import busio
import adafruit_mlx90640

# hostname = socket.gethostname()
# ip = socket.gethostbyname(hostname)
# print(hostname)
# print(ip)

'''
-create i2c connection using busio.I2C()
-create var to hold camera connection using adafruit_mlx90640.MLX90640(i2c)
-update refresh rate of camera var to 1Hz
-create a frame list that has 768 values of the camera

-try to create a socket using socket.socket()
-set up port for communication
-bind the socket and port using socket.bind()
-listen for any connections using socket.listen()

-while True loop
    -try 
        -to get frame from ccamera var
        -add a delay?

        -accept incoming connections
        -convert frame to json buffer 
        -use fd.send() to send data, example uses send('MESSAGE'.encode()) tosend byte type
        
        -use fd.close() to close sockcet

    if errorVal
        -pass
    if errorOS
        -error getting data from vamera var
        -delay?

    
'''

'''
### MAYBE USE THIS FOR sending data in pieces instead of whole ###
int sendall(int s, char *buf, int *len)
{
	int total = 0;
	int bytesleft = *len;
	int n;
	
	while(total < *len)
	{
		n = send(s, buf + total, bytesleft, 0);
		if (n == -1) 
		{ 
			break; 
		}
		total += n;
		bytesleft-= n;
	}
	*len = total;
	return n==-1?-1:0;
}
'''