import AltitudeLogging
import random
import csv

al = AltitudeLogging.AltitudeLogger()

for i in range(100):
    al.LogAltitude(random.random())

al.ExportAltitudeLogsToCsv(r"C:\Users\tihanewi\Downloads\TestCsv.csv")
print("Done")
