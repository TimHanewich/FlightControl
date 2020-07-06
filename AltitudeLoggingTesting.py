import AltitudeLogging
import random
import csv
import RPi.GPIO as GPIO
import time
import datetime

#############################################
TRIG = 4
ECHO = 18
LED = 21
RunForMinutes = 1
RefreshEverySeconds = 0.50
##############################################


GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT) #indicator light

al = AltitudeLogging.AltitudeLogger()

#turn on indicator
GPIO.output(LED, True)
starttime = datetime.datetime.now()
kill = False
while kill == False:

    # send out signal
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        tstart = time.time()

    while GPIO.input(ECHO) == True:
        tend = time.time()

    sig_time = tend - tstart
    distanceCM = sig_time / 0.000058

    al.LogAltitude(distanceCM)

    # WAIT!
    time.sleep(RefreshEverySeconds)

    elapsed_time = datetime.datetime.now() - starttime
    elapsed_time: datetime.timedelta
    elapsed_mins = elapsed_time.total_seconds() / 60
    if elapsed_mins > RunForMinutes:
        kill = True
    else:
        kill = False
        time_left = RunForMinutes - elapsed_mins
        print(str(elapsed_mins) + " elapsed. Continuing for " + str(time_left) + " minutes")


GPIO.output(LED, False)
print("Exporting to CSV...")
al.ExportAltitudeLogsToCsv("/AltitudeLogs.csv")
print("Program complete.")
