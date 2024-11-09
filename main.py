import os
import time
from colorama import init, Fore, Style

# Проверка успешности импорта модулей
try:
    import social_deanon as sd
    import ip_deanon as idn
    import phone_deanon as phd
except ImportError as e:
    print(f"Ошибка импорта модуля: {e}")
    exit(1)

# Инициализация colorama для цветного текста
init()

# Цветовые переменные
COLORS = {
    'red': Fore.RED,
    'green': Fore.GREEN,
    'cyan': Fore.CYAN,
    'reset': Style.RESET_ALL,
    'bright': Style.BRIGHT
}

def clear_screen():
    """Очистка экрана в зависимости от операционной системы."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    """Отображение логотипа с плавной анимацией."""
    logo_text = f"""
{COLORS['red']}███████╗██╗░░██╗██████╗░░█████╗░░██████╗███████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██║░░██║╚█████╗░█████╗░░
██╔══╝░░░██╔██╗░██╔═══╝░██║░░██║░╚═══██╗██╔══╝░░
███████╗██╔╝╚██╗██║░░░░░╚█████╔╝██████╔╝███████╗
╚══════╝╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚═════╝░╚══════╝{COLORS['reset']}
    """
    clear_screen()
    for line in logo_text.splitlines():
        print(line)
        time.sleep(0.1)
    print(COLORS['green'] + ' Разработчик: devpython44      v0.1      Made in Ukraine' + COLORS['reset'])
    time.sleep(2)

def main_menu():
    """Главное меню программы с выбором функционала."""
    options = {
        '1': sd.SocialDeanon,
        '2': idn.IpInfo,
        '3': idn.bssid_info,
        '4': phd.PhoneNumber,
        '0': exit_tool
    }

    while True:
        clear_screen()
        print(f"""
{COLORS['red']} ╭━╮╭━┳━━━┳━╮╱╭┳╮╱╭╮
 ┃┃╰╯┃┃╭━━┫┃╰╮┃┃┃╱┃┃
 ┃╭╮╭╮┃╰━━┫╭╮╰╯┃┃╱┃┃
 ┃┃┃┃┃┃╭━━┫┃╰╮┃┃┃╱┃┃
 ┃┃┃┃┃┃╰━━┫┃╱┃┃┃╰━╯┃
 ╰╯╰╯╰┻━━━┻╯╱╰━┻━━━╯
{COLORS['reset']}
{COLORS['cyan']}1) Проверка по нику\n2) Проверка IP-адреса\n3) Проверка BSSID\n4) Проверка по номеру телефона\n{COLORS['red']}0) Выход из тула{COLORS['reset']}
""")
        
        choice = input(COLORS['bright'] + '\n [+] Сделайте выбор: ' + COLORS['reset']).strip()
        
        if choice in options:
            clear_screen()
            options[choice]()  # Вызов соответствующей функции
        else:
            print(COLORS['red'] + 'Введите корректный пункт меню!' + COLORS['reset'])
            time.sleep(1)

def exit_tool():
    """Выход из программы."""
    print(COLORS['red'] + "Выход из тула. До свидания!" + COLORS['reset'])
    exit(0)

if __name__ == '__main__':
    display_logo()
    main_menu()
