import socket
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, UDP

def request_file_chunk(filename, server, port):
    ip = IP(dst=server)
    transport = UDP(dport=port)
    dns = DNS(rd=1, qd=DNSQR(qname=filename, qtype="TXT"))
    response = sr1(ip / transport / dns, timeout=5)
    if response and response.haslayer(DNSRR):
        return response[DNS].an.rdata
    else:
        return None

def receive_file(filename, server, port):
    with open("primit_" + filename, "wb") as f:
        while True:
            chunk = request_file_chunk(filename, server, port)
            if chunk:
                f.write(chunk)
                if len(chunk) < 512:  # Assuming 512 is the max size for each chunk
                    break
            else:
                break

if _name_ == "_main_":
    server_ip = "127.0.0.1"  # Sau IP-ul serverului tău
    server_port = 5331  # Portul disponibil afișat de server
    receive_file("testfile", server_ip, server_port)