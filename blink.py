import os
import time



os.system('echo 79 > /sys/class/gpio/export')
os.system('echo out > /sys/class/gpio/gpio79/direction')

i = 0

while i<10:
        os.system('echo 1 > /sys/class/gpio/gpio79/value')
        time.sleep(2)
        os.system('echo 0 > /sys/class/gpio/gpio79/value')
        time.sleep(2)
        i = i +1