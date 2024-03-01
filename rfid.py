import network
import socket
from time import sleep
import machine
import mip

ssid = input('Indique your wifi name: ')
password = input('Indiquer votre mot de passe wifi: ')

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    module = input('Name your pip modul: ')
    mip.install(module)

try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()