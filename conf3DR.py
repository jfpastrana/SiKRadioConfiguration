import time
import serial
import ConfigParser
import binascii

config = ConfigParser.ConfigParser()
config.read('configuration.ini')

#SERIAL CONFIGURATION
PORT = config.get('SERIAL_CONF','PORT_COM')
BAUD = config.get('SERIAL_CONF','BAUDRATE')

#RF CONFIGURATION
SERIAL_SPEED = config.get('RF_CONF','SERIAL_SPEED_AIR')
SPEED_AIR = config.get('RF_CONF','SPEED_AIR')
ID = config.get('RF_CONF','NET_ID')
DBM = config.get('RF_CONF','POWER')
ECC = config.get('RF_CONF','ECC')
APM = config.get('RF_CONF','APM')
F_MIN = config.get('RF_CONF','F_MIN')
F_MAX = config.get('RF_CONF','F_MAX')
CHANNELS = config.get('RF_CONF','CHANNELS')
RT_DC = config.get('RF_CONF','RT_DUTY_CYCLE')
AT_DC = config.get('RF_CONF','AT_DUTY_CYCLE')

#PORT CONFIGURATION
rf = serial.Serial(port=PORT, baudrate=BAUD, bytesize=8, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=5, xonxoff=False, rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None)
print ("Puerto (%s): %s" % (PORT,rf.portstr))
if rf.is_open:
    print("Puerto abierto correctamente")
    print("\tEntrado en modo de configuracion")
    #START SENDING AT COMMAND
    time.sleep(0.5)
    command = "+++"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(3)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #RT MODE
    print("\tEntrado en modo RT...")
    command = "RT\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)
    
    #SERIAL_SPEED
    print("Configurando serial speed air %s..." % SERIAL_SPEED)
    command = "RTS1=" + SERIAL_SPEED + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #SPEED_AIR
    print("Configurando air speed %s..." % SPEED_AIR)
    command = "RTS2=" + SPEED_AIR + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #NET_ID
    print("Configurando ID de la red %s..." % ID)
    command = "RTS3=" + ID + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #POWER
    print("Configurando potencia %s dBm..." % DBM)
    command = "RTS4=" + DBM + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #ECC
    print("Configurando ECC = %s..." % ECC)
    command = "RTS5=" + ECC + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #APM
    print("Configurando APM Mavlink = %s..." % APM)
    command = "RTS6=" + APM + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #F_MIN
    print("Configurando frecuencia minima a %s..." % F_MIN)
    command = "RTS8=" + F_MIN + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #F_MAX
    print("Configurando frecuencia maxima a %s..." % F_MAX)
    command = "RTS9=" + F_MAX + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #CHANNELS
    print("Configurando numero de canales %s..." % CHANNELS)
    command = "RTS10=" + CHANNELS + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #RT_DUTY CYCLE
    print("Configurando Duty Cycle %s..." % RT_DC)
    command = "RTS11=" + RT_DC + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)
    
    #WRITE REGISTERS
    print("Escribiendo en los registros...")
    command = "RT&W\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #RESET RT
    print("Reiniciando emisor...")
    command = "RTZ\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #AT MODE
    print("Entrado en modo AT...")
    command = "AT\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #SERIAL_SPEED
    print("Configurando serial speed air %s..." % SERIAL_SPEED)
    command = "ATS1=" + SERIAL_SPEED + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #SPEED_AIR
    print("Configurando air speed %s..." % SPEED_AIR)
    command = "ATS2=" + SPEED_AIR + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #NET_ID
    print("Configurando ID de la red %s..." % ID)
    command = "ATS3=" + ID + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #POWER
    print("Configurando potencia %s dBm..." % DBM)
    command = "ATS4=" + DBM + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #ECC
    print("Configurando ECC = %s..." % ECC)
    command = "ATS5=" + ECC + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #APM
    print("Configurando APM Mavlink = %s..." % APM)
    command = "ATS6=" + APM + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #F_MIN
    print("Configurando frecuencia minima a %s..." % F_MIN)
    command = "ATS8=" + F_MIN + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #F_MAX
    print("Configurando frecuencia maxima a %s..." % F_MAX)
    command = "ATS9=" + F_MAX + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #CHANNELS
    print("Configurando numero de canales %s..." % CHANNELS)
    command = "ATS10=" + CHANNELS + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #DUTY CYCLE AT
    print("Configurando Duty Cycle %s..." % AT_DC)
    command = "ATS11=" + AT_DC + "\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #WRITTING REGISTER
    print("Escribiendo en los registros...")
    command = "AT&W\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #RESET AT
    print("Reiniciando receptor(USB)...")
    command = "ATZ\r\n"
    command_bytes = command.encode('utf-8')
    rf.write(command_bytes)
    time.sleep(2)
    response = rf.readline()
    print("\tRespuesta recibida: "+response)

    #CLOSING PORT
    rf.close()
else:
    print("Puerto no abierto");
