import pycountry
import phonenumbers
from phonenumbers import carrier, timezone, region_code_for_country_code

class PhoneNumber:
    def __init__(self):
        self.number = input('\n [+] Enter phone: ').replace('+', '').strip()
        self.output()

    def default_info(self):
        """Получение основной информации о номере телефона."""
        try:
            phone_num = phonenumbers.parse(f'+{self.number}', None)
        except phonenumbers.NumberParseException:
            raise ValueError('Номер введён неверно')

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
            print(f''' =====================================
   Номер:         +{self.number}
   Страна:        {data['country']}
   Оператор:      {data['operator']}
   Часовой пояс:  {data['timezone']}
 =====================================''')
        except ValueError as e:
            print(f'Ошибка: {e}')
        input()

# Пример использования класса
if __name__ == "__main__":
    PhoneNumber()
