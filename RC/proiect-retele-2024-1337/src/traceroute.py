import socket
import traceback
import requests
import folium
import pandas as pd
"""
Pentru a realiza harta am folosit biblioteca folium si am urmat
documentatia de la https://python-graph-gallery.com/312-add-markers-on-folium-map/
Harta este salvata intr-un fisier html harta.html
"""

lat_list, long_list, text_list = [], [], []


class Adresa:
    def __init__(self, ttl, ip):
        self.ttl = ttl
        self.ip = ip
        self.fake_HTTP_header = {
            'referer': 'https://ipinfo.io/',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
        }
        req = requests.get(f'http://ip-api.com/json/{ip}?fields=status,country,regionName,city,lat,lon',
                           headers=self.fake_HTTP_header)
        self.info = req.json()

    def __str__(self):
        if self.info['status'] == 'success':
            long_list.append(self.info['lon'])
            text_list.append(f"{self.ttl}")
            lat_list.append(self.info['lat'])
            return f"{self.ttl}\t{self.ip}\t{self.info['city']}, {self.info['regionName']}, {self.info['country']}"
        else:
            return f"{self.ttl}\t{self.ip}\t"  # (?) adresa privata (nu stiu daca toate care au status failed)


def printIP():
    for b in adrese:
        print(b)


# socket de UDP
udp_send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)

# socket RAW de citire a răspunsurilor ICMP
icmp_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
# setam timout in cazul in care socketul ICMP la apelul recvfrom nu primeste nimic in buffer
icmp_recv_socket.settimeout(3)
adrese = []


def traceroute(ip, port):
    ttl = 1
    try:
        while True:
            # setam TTL in headerul de IP pentru socketul de UDP
            udp_send_sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)

            # trimite un mesaj UDP catre un tuplu (IP, port)
            udp_send_sock.sendto(b'salut de la unibuc', (ip, port))

            # asteapta un mesaj ICMP de tipul ICMP TTL exceeded messages
            # in cazul nostru nu verificăm tipul de mesaj ICMP
            # puteti verifica daca primul byte are valoarea Type == 11
            # https://tools.ietf.org/html/rfc792#page-5
            # https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Header

            addr = 'done!'
            data, addr = icmp_recv_socket.recvfrom(63535)
            if ttl > 1 and adrese[-1].ip == addr[0]:
                return
            adrese.append(Adresa(ttl, addr[0]))
            if data[1] != 11:
                ttl += 1
    except Exception as e:
        pass


traceroute("104.18.24.105", 33434)
printIP()
harta = folium.Map(location=[20, 0], tiles="OpenStreetMap", zoom_start=2)
checkpointuri = pd.DataFrame({
    'lon': long_list,
    'lat': lat_list,
    'name': text_list
}, dtype=str)
for i in range(0, len(checkpointuri)):
    folium.Marker(
        location=[checkpointuri.iloc[i]['lat'], checkpointuri.iloc[i]['lon']],
        popup=checkpointuri.iloc[i]['name'],
        icon=folium.DivIcon(html=f"""<div style="font-family: roboto; color: blue; font-size:16px">{checkpointuri.iloc[i]['name']}</div>""")
    ).add_to(harta)
harta.save('harta.html')

'''
 Exercitiu hackney carriage (optional)!
    e posibil ca ipinfo sa raspunda cu status code 429 Too Many Requests
    cititi despre campul X-Forwarded-For din antetul HTTP
        https://www.nginx.com/resources/wiki/start/topics/examples/forwarded/
    si setati-l o valoare in asa fel incat
    sa puteti trece peste sistemul care limiteaza numarul de cereri/zi

    Alternativ, puteti folosi ip-api (documentatie: https://ip-api.com/docs/api:json).
    Acesta permite trimiterea a 45 de query-uri de geolocare pe minut.
'''

# exemplu de request la IP info pentru a
# obtine informatii despre localizarea unui IP
fake_HTTP_header = {
    'referer': 'https://ipinfo.io/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
}
# informatiile despre ip-ul 193.226.51.6 pe ipinfo.io
# https://ipinfo.io/193.226.51.6 e echivalent cu
# raspuns = requests.get('https://ipinfo.io/widget/193.226.51.6', headers=fake_HTTP_header)
# print(raspuns.json())

# # pentru un IP rezervat retelei locale da bogon=True
# raspuns = requests.get('https://ipinfo.io/widget/172.64.144.177', headers=fake_HTTP_header)
# print(raspuns.json())

# req = requests.get(f'http://ip-api.com/json/72.14.216.212fields=status,country,regionName,city', headers=fake_HTTP_header)
# info = req.json()
# print(info)
