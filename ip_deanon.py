import socket
import threading
import requests
import ipaddress
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

# Инициализация colorama
init()

# Определение цветов
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
cyan = Fore.CYAN
reset = Style.RESET_ALL
bright = Style.BRIGHT

class IpInfo:
    def __init__(self):
        self.ip = input(f'{green}\n [+] IP For Scan: {reset}')
        try:
            ipaddress.ip_address(self.ip)
        except ValueError:
            raise ValueError(f'{red}IP адрес введён неверно{reset}')
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

        for port in range(1, 1025):  # Оптимизировано до 1024 портов
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

        print(f' {cyan}=' * design_len + f'''
  {yellow}IP address:{reset}  {self.ip}
  {yellow}Country:{reset}     {api.get("country", "N/A")}
  {yellow}Region:{reset}      {api.get("region", "N/A")}
  {yellow}City:{reset}        {api.get("city", "N/A")}
  {yellow}Zip:{reset}         {api.get("zip", "N/A")}
  {yellow}Latitude:{reset}    {api.get("lat", "N/A")}
  {yellow}Longitude:{reset}   {api.get("lon", "N/A")}
  {yellow}Timezone:{reset}    {api.get("timezone", "N/A")}
  {yellow}ISP:{reset}         {api.get("isp", "N/A")}
  {yellow}Org:{reset}         {api.get("org", "N/A")}
  {yellow}Host:{reset}        {host}
  {yellow}Open ports:{reset}  {', '.join(open_ports) if open_ports else f'{red}Нет открытых портов{reset}'}
  {yellow}Minecraft:{reset}   {self.minecraft()}
  {yellow}CS:GO:{reset}       {self.csgo()}
  {yellow}Unturned:{reset}    {self.unturned()}
  {yellow}Arma 3:{reset}      {self.arma()}
 ''' + f' {cyan}=' * design_len)

        input(f'{green}Введите любой символ для продолжения... {reset}')

def bssid_info():
    """Получение геолокации по BSSID."""
    query = input(f'{green}  BSSID: {reset}')
    try:
        response = requests.get(f"https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid={query}")
        data = response.json()
        if data["result"] == 200:
            lat, lon = data["data"]["lat"], data["data"]["lon"]
            print(f'{green}  Latitude:{reset} {lat}\n  {green}Longitude:{reset} {lon}')
        else:
            print(f'{red}  Error:{reset} {data.get("desc", "Неизвестная ошибка")}')
    except Exception as e:
        print(f'{red} Ошибка запроса: {e}{reset}')
    input(f'{green}Введите любой символ для продолжения... {reset}')
