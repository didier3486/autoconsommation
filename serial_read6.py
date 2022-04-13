
# programme python pour afficher la consommation electrique du compteur linky
# 4 avril 2022

import serial
import time
import socket
# ouverture de socket vers le serveur Pi3 muni de LED
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("IP du serveur", 5000))
try:
# ouverture du port serie usb en liaison avec le linky
        with serial.Serial('/dev/ttyUSB0') as ser:
                print("Ouverture de port OK!\n")
                ser.baudrate = 1200
                ser.parity = 'E'
                ser.stopbits = 1
                ser.bytesize = 7
                ser.timeout = None
                ser.xonxoff = 0
                ser.rtscts = 0
                data =[]
                i=0
                print("entrer control+C pour finir le programme:\n")
# extraire les mesures de puissance
                while True:
                        data = ser.readline()
                        if data[0] == 'P' and data[1] == 'A' and data[2] == 'P' and data[3] == 'P':
                                print("mesure numero: %u" %(i))
                                print("consommation en Watts = %s" %(data[5:10]))
# indication autoconsommation ou non
                                if data[5] == '0' and data[6] == '0' and data[7] == '0' and data[8] == '0' and data[9] == '0':
                                        print("AUTOCONSOMMATION BRAVO!\n")
                                        allumage="VERT"
                                else:
                                        print("PAS BIEN!\n")
                                        allumage="ROUGE"
                                sock.send(allumage)
                                i=i+1
except KeyboardInterrupt:
        print("\nFin du programme")
