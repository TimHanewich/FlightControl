import AltitudeLogging
import random
import csv
import RPi.GPIO as GPIO
import time
import datetime

#############################################
TRIG = 4
ECHO = 18
RunForMinutes = 5
RefreshEverySeconds = 0.50
##############################################


GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(TRIG, True)
GPIO.setup(ECHO, False)

al = AltitudeLogging.AltitudeLogger()

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
    if elapsed_time.minute > RunForMinutes:
        kill = True
    else:
        kill = False
        time_left = RunForMinutes - elapsed_time.minute
        print(str(elapsed_time.minute) + " elapsed. Continuing for " + str(time_left) + " minutes")


print("Exporting to CSV...")
al.ExportAltitudeLogsToCsv("/AltitudeLogs.csv")
print("Program complete.")