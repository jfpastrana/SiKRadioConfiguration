import time
import serial

port_com = "COM1"
baud = "57600"

rf = serial.Serial(port_com, 9600, EIGHTBITS, PARITY_NONE, STOPBITS_ONE, timeout=5, xonxoff=False, rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None)
try:
	time.sleep(0.5)
	rf.write(b'+++')
	time.sleep(3)
	response = rf.readall()
	print(response)
	rf.write(b'RT\r\n')
	time.sleep(1)
	response = rf.readall()
	print(response)
	"""
	RT&F
	RTS1=19
	RTS2=19
	RTS3=20
	RTS4=20
	RTS5=1
	RTS6=0
	RTS8=414000
	RTS9=427000
	RTS10=50
	RTS11=100
	RT&W
	RTZ
	
	
	
finally:
	rf.close()
