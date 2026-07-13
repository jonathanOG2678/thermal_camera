import socket
import board
import busio
import adafruit_mlx90640
import json

#Set up the I2C connection with the thermal module
i2c = busio.I2C(board.SCL, board.SDA)

while not i2c.try_lock(): # Attempts to stop other communication to allow list of all connected devices
    pass
try:
    print('--------Connected Addresses---------')
    print(x for x in i2c.scan())
finally:
    i2c.unlock()
    
mlx = adafruit_mlx90640.MLX90640(i2c)
mlx.refreshrate = adafruit_mlx90640.RefreshRate.REFRESH_1_HZ

frame = [0] * 768 # Camera has 32*24 frames


# Configure socket to bind and listen for any clients to receive data
sock = socket.socket()
port = 5555

sock.bind(('',port))
print('host binded port', port)
sock.listen(5)
print('host listening')
s, addr = sock.accept() # Establish connection with the client
print('Client', addr, 'accepted')

#The following try finally block is an implentation to safely close the socket
try:
    while True:
        try:
            mlx.getFrame(frame) # Attempts to get frame from thermal module, sometimes may return invalid results
            # print(frame)
            jframe = json.dumps(frame) + "\n" #converts frame data to json formatted string, delim of EOF
            #print(jframe)
            s.sendall(jframe.encode())
            #print("frame sent")
        except (BrokenPipeError, ConnectionResetError):
            print("Client disconnected")
            break
        except ValueError:
            print('Invalid frame...Continuing')
            continue
except KeyboardInterrupt:
    print("Server stopped with Ctrl+C")
finally:
    s.close() # End connection with client
