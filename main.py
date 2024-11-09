import os
import time
from colorama import init, Fore, Style
import social_deanon as sd
import ip_deanon as idn
import phone_deanon as phd

# Инициализация colorama для цветного текста
init()

# Определение цветовых переменных
red = Fore.RED
green = Fore.GREEN
cyan = Fore.CYAN
magenta = Fore.MAGENTA
reset = Style.RESET_ALL
bright = Style.BRIGHT

def clear_screen():
    """Очистка экрана в зависимости от операционной системы."""
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    """Отображение логотипа с плавной анимацией."""
    logo_text = f"""{red}
███████╗██╗░░██╗██████╗░░█████╗░░██████╗███████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██║░░██║╚█████╗░█████╗░░
██╔══╝░░░██╔██╗░██╔═══╝░██║░░██║░╚═══██╗██╔══╝░░
███████╗██╔╝╚██╗██║░░░░░╚█████╔╝██████╔╝███████╗
╚══════╝╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚═════╝░╚══════╝{reset}
    """
    clear_screen()
    for line in logo_text.split('\n'):
        print(line)
        time.sleep(0.1)
    print(green + ' Разработчик: devpython44      v0.1      Made in Ukraine' + reset)
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
        clear_screen()
        print(f"""{red}
 ╭━╮╭━┳━━━┳━╮╱╭┳╮╱╭╮
 ┃┃╰╯┃┃╭━━┫┃╰╮┃┃┃╱┃┃
 ┃╭╮╭╮┃╰━━┫╭╮╰╯┃┃╱┃┃
 ┃┃┃┃┃┃╭━━┫┃╰╮┃┃┃╱┃┃
 ┃┃┃┃┃┃╰━━┫┃╱┃┃┃╰━╯┃
 ╰╯╰╯╰┻━━━┻╯╱╰━┻━━━╯
{reset}""")
        print(f"{cyan}1) Проверка по нику\n2) Проверка IP-адреса\n"
              f"3) Проверка BSSID\n4) Проверка по номеру телефона\n{red}0) Выход из тула{reset}")
        
        choice = input(bright + '\n [+] Сделайте выбор: ' + reset)

        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                print(red + "Выход из тула. До свидания!" + reset)
                break
            elif choice in options:
                clear_screen()  # Очищаем экран перед выводом информации
                options[choice]()  # Вызываем соответствующую функцию
            else:
                print(red + 'Введите существующий пункт меню!' + reset)
        else:
            print(red + 'Ошибка ввода! Пожалуйста, введите номер пункта меню.' + reset)
        time.sleep(1)

if __name__ == '__main__':
    logo()
    menu()
