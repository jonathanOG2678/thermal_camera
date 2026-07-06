import numpy
import json
import socket
import cv2
port = 5555
host = '10.0.0.87'

WIDTH = 32
HEIGHT = 24

DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 480

# Fixed temperature range for display.
# Good for room/human testing:
MIN_TEMP = 20.0
MAX_TEMP = 40.0

# For electronics heating later, try something like:
# MIN_TEMP = 25.0
# MAX_TEMP = 80.0

previous_frame = None 	# Save previous frame for blending with current

# This function was adapted from ChatGPT with my custom recvall() function 
# from C++. This modification allows to separate frames if inbound data contains
# more than one frame because of TCP byte stream (partial one frame, exact one 
# frame, 1+ frames). Any leftover bytes will be temporarily held for the next frame,
# as this is the next frame
def recvall(s, buffer):
	CHUNK_SIZE = 5000

	while b"\n" not in buffer:
		chunk = s.recv(CHUNK_SIZE)

		if chunk == b"": # If nothing is returned, an error has occured and closed socket
			raise ConnectionError("socket closed")
		
		buffer += chunk

	frame_data, buffer = buffer.split(b"\n", 1)
	return frame_data,buffer
	
def process_thermal_frame(frame):
	global previous_frame
	# Reshape frame array to 32x24
	print(type(frame))
	print(len(frame)) 
	frame2D = numpy.array(frame, dtype=numpy.float32).reshape((HEIGHT, WIDTH))

	# temportal smoothing to reduce slow frame switching
	if previous_frame is None:
		smoothed = frame2D
	else:
		alpha = 0.35 # higher = more responsive, lower = smoother
		smoothed = (alpha * frame2D) + ((1 - alpha) * previous_frame) # Some part of new frame meshed with some from part of previous
	previous_frame = smoothed

	# Normalize temp ranges from 0-255
	clipped = numpy.clip(smoothed, MIN_TEMP, MAX_TEMP)
	normalized = (clipped - MIN_TEMP) / (MAX_TEMP - MIN_TEMP)
	grayscale = (normalized * 255).astype(numpy.uint8) # convert floats to int

	# Resizes image and interpolates values to fit into desired width and height
	enlarged = cv2.resize(
		grayscale,
		(DISPLAY_WIDTH, DISPLAY_HEIGHT),
		interpolation=cv2.INTER_CUBIC
	)

	# Convert the grayscale intensity to BGR color using openCV
	colored = cv2.applyColorMap(enlarged, cv2.COLORMAP_PLASMA)
	
	return colored

# -----------------MAIN------------------#
# Configure socket to receive data from Raspberry Pi
s = socket.socket(socket.AF_INET)
s.connect((host, port))
print('Connected to', host)

# receive and decode data to process into opencv
buffer = b""
while True:
	data, buffer = recvall(s, buffer)
	print(data)
	frame = json.loads(data.decode())

	#process image and display
	image = process_thermal_frame(frame)
	if image is None:
		continue
		
	cv2.imshow("Thermal Camera", image)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

cv2.destroyAllWindows()
s.close()
