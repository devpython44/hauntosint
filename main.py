import os
import time
from colorama import init, Fore, Style
import systemFiles.social_deanon as sd
import systemFiles.ip_deanon as idn
import systemFiles.phone_deanon as phd

# Инициализация colorama для цветного текста
init()
red = Fore.RED
reset = Style.RESET_ALL

def logo():
    """Отображение логотипа с плавной анимацией."""
    logo_text = """\n\n
 ██████╗░███████╗░█████╗░███╗░░██╗░█████╗░███╗░░██╗
 ██╔══██╗██╔════╝██╔══██╗████╗░██║██╔══██╗████╗░██║
 ██║░░██║█████╗░░███████║██╔██╗██║██║░░██║██╔██╗██║
 ██║░░██║██╔══╝░░██╔══██║██║╚████║██║░░██║██║╚████║
 ██████╔╝███████╗██║░░██║██║░╚███║╚█████╔╝██║░╚███║
 ╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    for line in logo_text.split('\n'):
        print(line)
        time.sleep(0.1)
    print(Style.BRIGHT + ' Разработчик: nXoji      v0.1      Made in Ukraine' + reset)
    time.sleep(2)

def menu():
    """Главное меню программы с выбором функционала."""
    options = {
        1: sd.SocialDeanon,
        2: idn.IpInfo,
        3: idn.bssid_info,
        4: phd.PhoneNumber
    }
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
 ╭━╮╭━┳━━━┳━╮╱╭┳╮╱╭╮
 ┃┃╰╯┃┃╭━━┫┃╰╮┃┃┃╱┃┃
 ┃╭╮╭╮┃╰━━┫╭╮╰╯┃┃╱┃┃
 ┃┃┃┃┃┃╭━━┫┃╰╮┃┃┃╱┃┃
 ┃┃┃┃┃┃╰━━┫┃╱┃┃┃╰━╯┃
 ╰╯╰╯╰┻━━━┻╯╱╰━┻━━━╯
        ''')
        print(' Вы в главном меню\n 1) Проверка по нику\n 2) Проверка IP-adress \n'
              ' 3) Проверка BSSID\n 4) Проверка по номеру телефона\n 0) ! ВЫХОД !')
        try:
            choice = int(input('\n [+] Cделайте выбор: '))
            if choice == 0:
                print("Выход из программы. До свидания!")
                break
            elif choice in options:
                options[choice]()
            else:
                print(red + ' Введите существующий пункт меню!' + reset)
        except ValueError:
            print(red + ' Ошибка ввода! Пожалуйста, введите номер пункта меню.' + reset)
            time.sleep(1)

if __name__ == '__main__':
    logo()
    menu()
