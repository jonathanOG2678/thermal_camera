# Name: Jonathan Ortiz Guzman

# Project: Thermal Camera 

## Description
A thermal camera that takes temperature readings in celsius from the environment and makes a visual to a remote device via a Raspberry Pi.

The Raspberry PI hosts a connection to where it sends the camera data to a client and the client processes the data to give a visual using OpenCV image viewing.


## Items Used
- Adafruit mlx90640 Thermal Camera Module with StemmaQT
- StemmaQT male cable
- Raspberry PI 4B
- Windows Computer
- OpenCV
- Python 3.11


### Notes


### Things That I Learned
- For the mlx90640 module, the member functions were quite simple to use. The pattern that I learned was that the IC2 connection needs to be established, an optional check to see if address exists (which pauses any communication to do this), and then a function called getFrame(), which returns as a collection.
-

