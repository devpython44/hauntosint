import socket
import threading
import requests
import ipaddress
from bs4 import BeautifulSoup

class IpInfo:
    def __init__(self):
        self.ip = input('\n [+] IP For Scan: ')
        try:
            ipaddress.ip_address(self.ip)
        except ValueError:
            raise ValueError('IP адрес введён неверно')
        self.output()

    def default_info(self):
        """Получение основной информации об IP и хосте."""
        r = requests.get(f'http://ip-api.com/json/{self.ip}').json()
        try:
            host = socket.gethostbyaddr(self.ip)[0]
        except socket.herror:
            host = "Не удалось определить хост"
        
        return {'api': r, 'host': host}

    def open_ports(self):
        """Сканирование открытых портов."""
        open_ports_list = []
        threads = []

        def scan_port(port):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                if sock.connect_ex((self.ip, port)) == 0:
                    open_ports_list.append(str(port))

        for port in range(1, 1025):  # Оптимизирован до 1024 портов
            thread = threading.Thread(target=scan_port, args=(port,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()  # Дожидаемся завершения всех потоков

        return open_ports_list

    def fetch_game_data(self, url, no_result_msg="Не найдено"):
        """Функция для обработки запросов к игровым сайтам."""
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        result = soup.find('a', class_='s-link') or soup.find('h4', class_='no-margin')
        return result.text.strip() if result else no_result_msg

    def csgo(self):
        return self.fetch_game_data(f'https://www.gametracker.com/search/csgo/?query={self.ip}')

    def minecraft(self):
        return self.fetch_game_data(f'https://mc-servera.net/search?q={self.ip}')

    def unturned(self):
        return self.fetch_game_data(f'https://www.trackyserver.com/unturned-server/1?s={self.ip}')

    def arma(self):
        return self.fetch_game_data(f'https://www.gametracker.com/search/arma3/?query={self.ip}')

    def output(self):
        """Вывод информации об IP."""
        default = self.default_info()
        api = default['api']
        host = default['host']
        open_ports = self.open_ports()

        max_len = max(len(self.csgo()), len(self.minecraft()), len(self.unturned()), len(self.arma()))
        design_len = 15 + max_len

        print(' ' + "=" * design_len + f'''
  IP address:  {self.ip}
  Country:     {api.get("country", "N/A")}
  Region:      {api.get("region", "N/A")}
  City:        {api.get("city", "N/A")}
  Zip:         {api.get("zip", "N/A")}
  Latitude:    {api.get("lat", "N/A")}
  Longitude:   {api.get("lon", "N/A")}
  Timezone:    {api.get("timezone", "N/A")}
  ISP:         {api.get("isp", "N/A")}
  Org:         {api.get("org", "N/A")}
  Host:        {host}
  Open ports:  {', '.join(open_ports) if open_ports else "Нет открытых портов"}
  Minecraft:   {self.minecraft()}
  CS:GO:       {self.csgo()}
  Unturned:    {self.unturned()}
  Arma 3:      {self.arma()}
 ''' + "=" * design_len)
        input()

def bssid_info():
    """Получение геолокации по BSSID."""
    query = input(f'  BSSID: ')
    try:
        response = requests.get(f"https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid={query}")
        data = response.json()
        if data["result"] == 200:
            lat, lon = data["data"]["lat"], data["data"]["lon"]
            print(f'  Latitude: {lat}\n  Longitude: {lon}')
        else:
            print(f'  Error: {data.get("desc", "Неизвестная ошибка")}')
    except Exception as e:
        print(f' Ошибка запроса: {e}')
    input()
