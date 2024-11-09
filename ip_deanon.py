import socket
import threading
import requests
import ipaddress
from colorama import init, Fore, Style

# Инициализация цветового оформления
init()

COLORS = {'red': Fore.RED, 'green': Fore.GREEN, 'yellow': Fore.YELLOW, 'cyan': Fore.CYAN, 'reset': Style.RESET_ALL}

class IpInfo:
    def __init__(self):
        self.ip = input(f"{COLORS['green']}\n [+] IP For Scan: {COLORS['reset']}")
        if not self.validate_ip(self.ip):
            print(f"{COLORS['red']}Неверный IP адрес!{COLORS['reset']}")
            return
        self.display_info()

    def validate_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    def get_default_info(self):
        """Получение основной информации по IP через API."""
        try:
            api_data = requests.get(f'http://ip-api.com/json/{self.ip}').json()
            host = socket.gethostbyaddr(self.ip)[0]
        except socket.herror:
            host = "Не удалось определить хост"
        return api_data, host

    def open_ports(self):
        """Сканирование открытых портов."""
        open_ports = []
        def scan_port(port):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                if not sock.connect_ex((self.ip, port)):
                    open_ports.append(port)

        threads = [threading.Thread(target=scan_port, args=(p,)) for p in range(1, 1025)]
        for t in threads: t.start()
        for t in threads: t.join()

        return open_ports

    def check_server_availability(self, url):
        """Проверка доступности игрового сервера по IP."""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return "Доступен"
            return "Не найдено"
        except Exception:
            return "Не найдено"

    def display_info(self):
        """Вывод всей собранной информации об IP."""
        api_data, host = self.get_default_info()
        game_servers = {
            "Minecraft": f"https://mc-servera.net/search?q={self.ip}",
            "CS:GO": f"https://www.gametracker.com/search/csgo/?query={self.ip}",
            "Unturned": f"https://www.trackyserver.com/unturned-server/1?s={self.ip}",
            "Arma 3": f"https://www.gametracker.com/search/arma3/?query={self.ip}"
        }
        open_ports = ', '.join(map(str, self.open_ports())) or f"{COLORS['red']}Нет открытых портов{COLORS['reset']}"

        print(f"""{COLORS['cyan']} {'=' * 40}
    {COLORS['yellow']}IP Address:{COLORS['reset']}  {self.ip}
    {COLORS['yellow']}Country:{COLORS['reset']}     {api_data.get("country", "N/A")}
    {COLORS['yellow']}Region:{COLORS['reset']}      {api_data.get("region", "N/A")}
    {COLORS['yellow']}City:{COLORS['reset']}        {api_data.get("city", "N/A")}
    {COLORS['yellow']}Zip:{COLORS['reset']}         {api_data.get("zip", "N/A")}
    {COLORS['yellow']}Latitude:{COLORS['reset']}    {api_data.get("lat", "N/A")}
    {COLORS['yellow']}Longitude:{COLORS['reset']}   {api_data.get("lon", "N/A")}
    {COLORS['yellow']}Timezone:{COLORS['reset']}    {api_data.get("timezone", "N/A")}
    {COLORS['yellow']}ISP:{COLORS['reset']}         {api_data.get("isp", "N/A")}
    {COLORS['yellow']}Org:{COLORS['reset']}         {api_data.get("org", "N/A")}
    {COLORS['yellow']}Host:{COLORS['reset']}        {host}
    {COLORS['yellow']}Open Ports:{COLORS['reset']}  {open_ports}""")
        
        for game, url in game_servers.items():
            print(f"    {COLORS['yellow']}{game}:{COLORS['reset']} {self.check_server_availability(url)}")
        
        print(f" {COLORS['cyan']}{'=' * 40}{COLORS['reset']}")
        input(f"{COLORS['green']}Нажмите любую клавишу для продолжения... {COLORS['reset']}")

def bssid_info():
    """Получение геолокации по BSSID."""
    query = input(f"{COLORS['green']}  BSSID: {COLORS['reset']}")
    try:
        response = requests.get(f"https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid={query}").json()
        if response.get("result") == 200:
            lat, lon = response["data"]["lat"], response["data"]["lon"]
            print(f"{COLORS['green']}  Latitude:{COLORS['reset']} {lat}\n  {COLORS['green']}Longitude:{COLORS['reset']} {lon}")
        else:
            print(f"{COLORS['red']}  Error:{COLORS['reset']} {response.get('desc', 'Ошибка геолокации')}")
    except Exception as e:
        print(f"{COLORS['red']} Ошибка запроса: {e}{COLORS['reset']}")
    input(f"{COLORS['green']}Введите любой символ для продолжения... {COLORS['reset']}")
