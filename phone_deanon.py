import pycountry
import phonenumbers
from phonenumbers import carrier, timezone, region_code_for_country_code
from colorama import init, Fore, Style

# Инициализация colorama
init()

# Определение цветов
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW
reset = Style.RESET_ALL

class PhoneNumber:
    def __init__(self):
        self.number = input(f'{green}\n [+] Enter phone: {reset}').replace('+', '').strip()
        self.output()

    def default_info(self):
        """Получение основной информации о номере телефона."""
        try:
            phone_num = phonenumbers.parse(f'+{self.number}', None)
        except phonenumbers.NumberParseException:
            raise ValueError(f'{red}Номер введён неверно{reset}')

        # Получение кода страны и данных о стране
        country_iso = region_code_for_country_code(phone_num.country_code)
        country = pycountry.countries.get(alpha_2=country_iso)
        country_name = country.name if country else "Неизвестная страна"

        # Получение оператора
        operator = carrier.name_for_number(phone_num, 'ru')
        operator = operator if operator else 'Не найдено'

        # Получение часового пояса
        timezones = timezone.time_zones_for_number(phone_num)
        timezone_info = ', '.join(timezones) if timezones else "Не найдено"

        return {
            'country': country_name,
            'operator': operator,
            'timezone': timezone_info
        }

    def output(self):
        """Вывод информации о номере телефона."""
        try:
            data = self.default_info()
            print(f''' {yellow}===================================== {reset}
   {green}Номер:{reset}         +{self.number}
   {green}Страна:{reset}        {data['country']}
   {green}Оператор:{reset}      {data['operator']}
   {green}Часовой пояс:{reset}  {data['timezone']}
 {yellow}===================================== {reset}''')
        except ValueError as e:
            print(f'{red}Ошибка: {e}{reset}')
        input(f'{green}Введите любой символ для продолжения... {reset}')

# Пример использования класса
if __name__ == "__main__":
    PhoneNumber()
