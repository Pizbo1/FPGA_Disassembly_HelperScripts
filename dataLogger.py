import serial
import csv

f = open("data.csv", "w")
ser = serial.Serial('COM6', 115200)


while(True):
    line = ser.readline().decode('utf-8')
    if "Done" in line:
        break

    if line:
        f.write(line)
        print(line)

ser.close()
f.close()
