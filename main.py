# This is (an example of) the file you'll want to run on the micro:bit

# Do not remove this import, used by MicroPython to execute their module functions
# See the documentation to use their functions here: https://microbit-micropython.readthedocs.io/en/latest/tutorials/hello.html

from microbit import *

flash_count = 3

# Delay between flash on and flash off
flash_on_duration = 200
flash_off_duration = 200

# Flash the heart image three times
while True:
    for _ in range(flash_count):
        # Display the heart image
        display.show(Image.HEART)
        sleep(flash_on_duration)

        # Clear the display
        display.clear()
        sleep(flash_off_duration)
    # Display a message
    display.show("HI MOM !")
