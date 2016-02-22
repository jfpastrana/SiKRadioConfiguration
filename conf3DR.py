import time
import serial

port_com = "COM6"
baud = 57600

rf = serial.Serial(port=port_com, baudrate=baud, bytesize=8, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=5, xonxoff=False, rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None)
print ("Puerto (%s): %s" % (port_com,rf.portstr))

time.sleep(0.5)
rf.write('+++'.encode('utf-8'))
time.sleep(3)
response = rf.read(6)
print("Entrado en modo de configuracion")
print(response)

rf.write(b'RT\r\n')
time.sleep(1)
response = rf.read(6)
print("Entrado en modo RT...")
print(response)


rf.write(b'RTS1=19\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando serial speed air 19200...")
print(response)

rf.write(b'RTS2=19\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando air speed 19200...")
print(response)


rf.write(b'RTS3=16\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando ID de la red 20...")
print(response)


rf.write(b'RTS4=20\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando potencia 20dBm...")
print(response)

rf.write(b'RTS5=1\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando ECC=1...")
print(response)

rf.write(b'RTS6=0\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando APM Mavlink = 0...")
print(response)

rf.write(b'RTS8=414000\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando frecuencia minima a 414000...")
print(response)

rf.write(b'RTS9=427000\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando frecuencia maxima a 427000...")
print(response)

rf.write(b'RTS10=50\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando numero de canales 50...")
print(response)

rf.write(b'RTS11=100\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando Duty Cycle 100...")
print(response)


rf.write(b'RT&W\r\n')
time.sleep(1)
response = rf.read(6)
print("Escribiendo en los registros...")
print(response)

rf.write(b'RTZ\r\n')
time.sleep(1)
response = rf.read(6)
print("Reiniciando emisor...")
print(response)


rf.write(b'AT\r\n')
time.sleep(1)
response = rf.read(6)
print("Entrado en modo AT...")
print(response)

rf.write(b'ATS1=19\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando serial speed air 19200...")
print(response)

rf.write(b'ATS2=19\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando air speed 19200...")
print(response)

rf.write(b'ATS3=16\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando ID de la red 20...")
print(response)

rf.write(b'ATS4=20\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando potencia 20dBm...")
print(response)

rf.write(b'ATS5=1\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando ECC=1...")
print(response)

rf.write(b'ATS6=0\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando APM Mavlink = 0...")
print(response)

rf.write(b'ATS8=414000\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando frecuencia minima a 414000...")
print(response)

rf.write(b'ATS9=427000\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando frecuencia maxima a 427000...")
print(response)

rf.write(b'ATS10=50\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando numero de canales 50...")
print(response)

rf.write(b'ATS11=10\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando Duty Cycle 100...")
print(response)

rf.write(b'AT&W\r\n')
time.sleep(1)
response = rf.read(6)
print("Escribiendo en los registros...")
print(response)

rf.write(b'ATZ\r\n')
time.sleep(1)
response = rf.read(6)
print("Reiniciando emisor...")
print(response)


rf.close()
