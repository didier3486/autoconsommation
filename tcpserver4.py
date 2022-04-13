#==============================================
#		TCP/IP SERVER
#		=============
#
# This is the TCP/IP server program on Raspberry Pi3
# Allumage de LED verte si on est en autoconsommation
# 
# Date  : 9 avril 2022
#================================================
import socket
import RPi.GPIO as GPIO
# Define BCM2 et BCM3 as output and turn off LED at begining
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LEDVERTE=2
LEDROUGE=3
GPIO.setup(LEDVERTE,GPIO.OUT)
GPIO.output(LEDVERTE,0)
GPIO.setup(LEDROUGE,GPIO.OUT)
GPIO.output(LEDROUGE,0)
# ouverture de socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("IP du serveur", 5000))
sock.listen(1)
# accept connection
client, addr = sock.accept()		
print("Connected to client")
# allumer la LED verte si autoconsommation
# sinon allumer la LED rouge
try:
  while True:
    allumage = client.recv(1024)
    if allumage=="VERT":
      GPIO.output(LEDVERTE,GPIO.HIGH)
      GPIO.output(LEDROUGE,GPIO.LOW)
    else:
      GPIO.output(LEDVERTE,GPIO.LOW)
      GPIO.output(LEDROUGE,GPIO.HIGH)
    if allumage=="ROUGE":
      GPIO.output(LEDROUGE,GPIO.HIGH)
      GPIO.output(LEDVERTE,GPIO.LOW)
    else:
      GPIO.output(LEDROUGE,GPIO.LOW)
      GPIO.output(LEDVERTE,GPIO.HIGH)
except KeyboardInterrupt:
  print("\nClosing connection to client")
  sock.close()



