import Jetson.GPIO as GPIO
import time

# Set the GPIO mode to BOARD numbering
GPIO.setmode(GPIO.BOARD)

# Set pin 18 as an output pin
led_pin = 18
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # Turn on the LED
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)  # Wait for 1 second

        # Turn off the LED
        GPIO.output(led_pin, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
