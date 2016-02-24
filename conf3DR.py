import time
import serial
import configparser

config = configparser.ConfigParser()
config.read('configuration.ini')

#SERIAL CONFIGURATION
PORT = config['SERIAL_CONF']['PORT_COM']
BAUD = config['SERIAL_CONF']['BAUDRATE']

#RF CONFIGURATION
SERIAL_SPEED = config['RF_CONF']['SERIAL_SPEED_AIR']
SPEED_AIR = config['RF_CONF']['SPEED_AIR']
ID = config['RF_CONF']['NET_ID']
DBM = config['RF_CONF']['POWER']
ECC = config['RF_CONF']['ECC']
APM = config['RF_CONF']['APM']
F_MIN = config['RF_CONF']['F_MIN']
F_MAX = config['RF_CONF']['F_MAX']
CHANNELS = config['RF_CONF']['CHANNELS']
RT_DC = config['RF_CONF']['RT_DUTY_CYCLE']
AT_DC = config['RF_CONF']['AT_DUTY_CYCLE']

#PORT CONFIGURATION
rf = serial.Serial(port=PORT, baudrate=BAUD, bytesize=8, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=5, xonxoff=False, rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None)
print ("Puerto (%s): %s" % (PORT,rf.portstr))

#START SENDING AT COMMAND
time.sleep(0.5)
rf.write('+++'.encode('utf-8'))
time.sleep(3)
response = rf.read(6)
print("Entrado en modo de configuracion")
print(response)

#RT MODE
rf.write(b'RT\r\n')
time.sleep(1)
response = rf.read(6)
print("Entrado en modo RT...")
print(response)

command = "RTS1=" + SERIAL_SPEED + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando serial speed air %s..." % SERIAL_SPEED)
print(response)

command = "RTS2=" + SPEED_AIR + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando air speed %s..." % SPEED_AIR)
print(response)

command = "RTS3=" + ID + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando ID de la red %s..." % ID)
print(response)

command = "RTS4=" + DBM + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando potencia %s dBm..." % DBM)
print(response)

command = "RTS5=" + ECC + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando ECC = %s..." % ECC)
print(response)

command = "RTS6=" + APM + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando APM Mavlink = $s..." % APM)
print(response)

command = "RTS8=" + F_MIN + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando frecuencia minima a %s..." % F_MIN)
print(response)

command = "RTS9=" + F_MAX + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando frecuencia maxima a %s..." % F_MAX)
print(response)

command = "RTS10=" + CHANNELS + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando numero de canales %s..." % CHANNELS)
print(response)

command = "RTS11=" + RT_DC + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando Duty Cycle %s..." % RT_DC)
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

#AT MODE
rf.write(b'AT\r\n')
time.sleep(1)
response = rf.read(6)
print("Entrado en modo AT...")
print(response)

command = "ATS1=" + SERIAL_SPEED + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando serial speed air %s..." % SERIAL_SPEED)
print(response)

command = "ATS2=" + SPEED_AIR + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando air speed %s..." % SPEED_AIR)
print(response)

command = "ATS3=" + ID + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando ID de la red %s..." % ID)
print(response)

command = "ATS4=" + DBM + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando potencia %s dBm..." % DBM)
print(response)

command = "ATS5=" + ECC + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando ECC = %s..." % ECC)
print(response)

command = "ATS6=" + APM + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando APM Mavlink = $s..." % APM)
print(response)

command = "ATS8=" + F_MIN + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando frecuencia minima a %s..." % F_MIN)
print(response)

command = "ATS9=" + F_MAX + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando frecuencia maxima a %s..." % F_MAX)
print(response)

command = "ATS10=" + CHANNELS + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando numero de canales %s..." % CHANNELS)
print(response)

command = "ATS11=" + AT_DC + "\r\n"
rf.write(command.encode('utf-8'))
time.sleep(1)
response = rf.read(6)
print("Configurando Duty Cycle %s..." % RT_DC)
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

#CLOSING PORT
rf.close()
