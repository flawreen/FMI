import socket
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, UDP


def find_free_port(start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind(('0.0.0.0', port))
            s.close()
            return port
        except OSError:
            continue
    return None


def lookup(qname, qtype):
    ip = IP(dst='8.8.8.8')
    transport = UDP(dport=53)
    dns = DNS(rd=1)

    dns_query = DNSQR(qname=qname, qtype=qtype, qclass=1)
    dns.qd = dns_query

    return sr1(ip / transport / dns)


port = find_free_port(5351, 65535)
if port:
    print("Portul disponibil este:", port)
    simple_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)
    simple_udp.bind(('0.0.0.0', port))

    while True:
        request, adresa_sursa = simple_udp.recvfrom(65535)

        try:
            packet = DNS(request)
            dns = packet.getlayer(DNS)

            if dns is not None and dns.opcode == 0:
                print("got: ")
                print(packet.summary())

                qname = dns.qd.qname.decode().strip('.')
                qtype = dns.qd.qtype

                if qname.endswith('flawreen.ninja'):

                    dns_answer = DNSRR(
                        rrname=qname + '.',
                        ttl=330,
                        type="A",
                        rclass="IN",
                        rdata="138.2.178.187"
                    )
                    dns_response = DNS(
                        id=packet[DNS].id,
                        qr=1,
                        aa=1,
                        rcode=0,
                        qd=dns.qd,
                        an=dns_answer
                    )
                    print('response:')
                    print(dns_response.summary())
                    simple_udp.sendto(bytes(dns_response), adresa_sursa)
                else:
                    answer = lookup(dns.qd.qname, dns.qd.qtype)
                    if answer:
                        dns_answer = DNSRR(
                            rrname=dns.qd.qname,
                            ttl=330,
                            type=answer[DNS].an.type,
                            rclass=answer[DNS].an.rclass,
                            rdata=answer[DNS].an.rdata
                        )
                        dns_response = DNS(
                            id=packet[DNS].id,
                            qr=1,
                            aa=0,
                            rcode=0,
                            qd=dns.qd,
                            an=dns_answer
                        )
                        print('response:')
                        print(dns_response.summary())
                        simple_udp.sendto(bytes(dns_response), adresa_sursa)
        except Exception as e:
            print(f"a aparut o eroare {e}")
else:
    print("Nu am gasit port")
