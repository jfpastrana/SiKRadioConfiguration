import time
import serial

port_com = "COM1"
baud = "57600"

rf = serial.Serial(port_com,baud, timeout=5)
try:
	time.sleep(0.5)
	rf.write(b'+++')
	time.sleep(3)
	response = rf.readall()
	print(response)	
finally:
	rf.close()
