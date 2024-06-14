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


def handle_request(qname):
    try:
        with open(qname, "rb") as f:
            data = f.read(512)
        return data
    except FileNotFoundError:
        return None


def main():
    port = find_free_port(5331, 65535)
    if port:
        print("Port disponibil:", port)

        simple_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)
        simple_udp.bind(('0.0.0.0', port))

        while True:
            request, adresa_sursa = simple_udp.recvfrom(65535)

            packet = DNS(request)
            dns = packet.getlayer(DNS)

            if dns is not None and dns.opcode == 0:
                print("got: ")
                print(packet.summary())

                try:
                    file_data = handle_request(dns.qd.qname.decode())
                    if file_data:
                        dns_answer = DNSRR(
                            rrname=dns.qd.qname,
                            ttl=330,
                            type="TXT",
                            rclass="IN",
                            rdata=file_data
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
                    else:
                        print("File not found or read error.")
                except Exception as e:
                    print(f"An error occurred: {e}")
    else:
        print("Nu s-a putut găsi un port liber în intervalul specificat.")


if _name_ == "_main_":
    main()
