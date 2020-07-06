import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	print(GPIO.input(12))
	time.sleep(1)


print("Done")
