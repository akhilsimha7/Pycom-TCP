#client_pycom.py

import time
import network   #In order to enable the use of WiFi
import socket


# WiFi Connectivity
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect('Aurora_3F98', auth=(network.WLAN.WPA2, 'Vegan@26'))   # 2.4 GHz Network
while not wlan.isconnected():
  time.sleep_ms(50)
print(wlan.ifconfig())


HOST = "192.168.0.103"  # The server's hostname or IP address
PORT = 5060  # The port used by the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.send(b"ATOM SENDING A MESSAGE")
data = client.recv(1024)
print('Data received: %s' %(data))
