
import serial 
from time import sleep


ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
ser.flush()

def gpsVal(val):
	line = '0'
	if val == 1:
		ser.write(b"AT+CGNSINF\r\n")
		
		
		while "+CGNSINF: 1,1,2023" not in line:
			line = ser.readline().decode('utf-8').rstrip()
	
		line = line[10::]
		arr = line.split(",")
		ser.close()
		return [arr[3],arr[4],arr[6],arr[7]]


