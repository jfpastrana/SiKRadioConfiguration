import time
import serial

port_com = "COM3"
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

rf.write(b'RTS2=24\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando air speed 24...")
print(response)


rf.write(b'RTS3=16\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando ID de la red 16...")
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

rf.write(b'RTS6=1\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando APM Mavlink = 1...")
print(response)

rf.write(b'RTS8=433050\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando frecuencia minima a 433050...")
print(response)

rf.write(b'RTS9=434790\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando frecuencia maxima a 434790...")
print(response)

rf.write(b'RTS10=10\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando numero de canales 10...")
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

rf.write(b'ATS2=24\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando air speed 24...")
print(response)

rf.write(b'ATS3=16\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando ID de la red 16...")
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

rf.write(b'ATS6=1\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando APM Mavlink = 1...")
print(response)

rf.write(b'ATS8=433050\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando frecuencia minima a 433050...")
print(response)

rf.write(b'ATS9=434790\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando frecuencia maxima a 434790...")
print(response)

rf.write(b'ATS10=10\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando numero de canales 10...")
print(response)

rf.write(b'ATS11=10\r\n')
time.sleep(1)
response = rf.read(6)
print("Configurando Duty Cycle 10...")
print(response)

rf.write(b'AT&W\r\n')
time.sleep(1)
response = rf.read(6)
print("Escribiendo en los registros...")
print(response)

rf.write(b'ATZ\r\n')
time.sleep(1)
response = rf.read(6)
print("Reiniciando receptor(USB)...")
print(response)


rf.close()
