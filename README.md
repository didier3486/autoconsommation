# autoconsommation
obtenir un indicateur (LED) d'autoconsommation d'électricité dans le cas d'installation de panneaux solaires

matériel:
1 raspberry Pi3 ou Pi4 avec Python 2.x utilisé comme serveur
1 raspberry Pi3 ou Pi4 avec Python 2.x utilisé comme client et relié à la téléinformation client d'un compteur linky par l'intermédiaire d'une clé usb branchée sur le port usb du Pi3 ou Pi4(1)
1 LED verte avec résistance 220 ohms branchée sur Pin3 du serveur (SDA)
1 LED rouge avec résistance 220 ohms branchée sur Pin5 du client (SCL)

mode d'emploi:
exécuter le fichier tcpserver.py sur le serveur
exécuter le fichier serial_read6.py sur le client

bibliographie:
(1) ENI éditions, vidéo, Raspberry Pi - Apprenez à récupérer les données de votre compteur Linky
livre Elektor. Learning Python with Raspberry Pi
