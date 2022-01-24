# Add your Python code here. E.g.
from microbit import *


while True:
    uart.write(str(temperature())+" "+str(display.read_light_level())+" "+'\n')
    sleep(30000)