from microbit import *

while True:
    if display.read_light_level() < 50:
        display.show("!")
    sleep(500)
