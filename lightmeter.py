#!/usr/bin/env python

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import subprocess
import datetime
import RPi.GPIO as GPIO, time, os

log_file = "./log"

DEBUG = 1
GPIO.setmode(GPIO.BCM)

#fileoutput=open('./file', 'w+')

def lightreading (lightpin):
        reading = 0
        GPIO.setup(lightpin, GPIO.OUT)
        GPIO.output(lightpin, GPIO.LOW)
        time.sleep(0.5)

        GPIO.setup(lightpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(lightpin) == GPIO.LOW):
                reading += 1
        return reading

def lightresponse (lighttotal):
        if lighttotal > 2000:
                print 'dark'
                away = subprocess.check_output("./nest.sh")
                if 'True' in away:
                        now = datetime.datetime.now()
                        result = subprocess.check_output("./hue.sh", "On")
                        with open(log_file, "w") as log:
                                log.write(now + result + "\n")

while True:
        lightarray = []
        for i in range(20):
                lightarray.append(lightreading(18))     # Read RC timing using pin #18

        total_light = sum(lightarray)
        lightresponse(total_light)

