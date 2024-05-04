import Jetson.GPIO as GPIO
import time

# Define GPIO pins for the ultrasonic sensor
TRIG_PIN = 23  # GPIO pin for the trigger
ECHO_PIN = 24  # GPIO pin for the echo

# Set GPIO mode to BOARD numbering
GPIO.setmode(GPIO.BOARD)

# Setup GPIO pins
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def distance():
    # Send a 10us pulse to trigger the ultrasonic sensor
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Measure the duration of the pulse from the echo
    start_time = time.time()
    stop_time = time.time()
    
    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()
        
    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()

    # Calculate the distance based on the time difference
    elapsed_time = stop_time - start_time
    distance_cm = (elapsed_time * 34300) / 2  # Speed of sound in cm/s is 34300

    return distance_cm

try:
    while True:
        dist = distance()
        print("Distance: {:.2f} cm".format(dist))
        time.sleep(1)  # Wait for 1 second before the next reading

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
