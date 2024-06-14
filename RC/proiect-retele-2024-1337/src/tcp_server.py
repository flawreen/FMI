# TCP Server
import socket
import logging
import time
import os
from scapy.all import *
from libnetfilter import queue
from scapy.layers.inet import IP

queue = NFQ()

logging.basicConfig(format=u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)


def alter_packet(pachet):
    '''Implementați asta ca exercițiu.
    # !atentie, trebuie re-calculate campurile len si checksum
    '''
    if pachet.haslayer(IP):
        del pachet[IP].chksum
        del pachet[IP].len
        pachet[IP].tos = 3
        # pentru a obtine din nou len si chksum, facem rebuild
        # se face automat, de catre scapy
        pachet = IP(pachet.build())
    return pachet


def proceseaza(pachet):
    octeti = pachet.get_payload()
    scapy_packet = IP(octeti)
    print("Pachet inainte: ")
    scapy_packet.show()
    scapy_packet = alter_packet(scapy_packet)
    print("Pachet dupa: ")
    scapy_packet.show()
    pachet.set_payload(bytes(scapy_packet))
    pachet.accept()


port = 10000
adresa = '198.7.0.2'
server_address = (adresa, port)
sock.bind(server_address)
logging.info("Serverul a pornit pe %s si portnul portul %d", adresa, port)
sock.listen(5)
while True:
    logging.info('Asteptam conexiuni...')
    conexiune, address = sock.accept()
    logging.info("Handshake cu %s", address)
    time.sleep(2)
    data = conexiune.recv(1024)
    logging.info('Content primit: "%s"', data)
    conexiune.send(b"Server a primit mesajul: " + data)
    conexiune.close()
sock.close()
