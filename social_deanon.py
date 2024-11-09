import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

# Инициализация colorama
init()

class SocialDeanon:
    def __init__(self):
        self.nickname = input(f'{Fore.GREEN}\n [+] Enter nickname: {Style.RESET_ALL}').replace('@', '').strip()
        self.red = Fore.RED
        self.green = Fore.GREEN
        self.magenta = Fore.MAGENTA
        self.reset = Style.RESET_ALL

        self.output()

    def telegram(self):
        """Проверка наличия никнейма в Telegram."""
        url = f'https://t.me/{self.nickname}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')
            quote = soup.find('div', class_="tgme_page_description")
            if quote and "If you have Telegram" not in quote.text:
                return f"  {url}\n"
        except requests.RequestException:
            return ""
        return ""

    def availability(self):
        """Проверка наличия никнейма в популярных социальных сетях."""
        req_list = [
            'https://www.instagram.com/',
            'https://github.com/',
            'https://rt.pornhub.com/users/',
            'https://ok.ru/',
            'https://vk.com/',
            'https://soundcloud.com/',
            'https://www.tumblr.com/blog/view/',
            'https://twitter.com/',
            'https://ask.fm/',
            'https://znanija.com/app/profile/',
            'https://www.deviantart.com/',
            'https://www.flickr.com/',
            'https://ru.linkedin.com/in/',
            'https://myspace.com/',
            'https://www.pinterest.com/',
            'https://www.reddit.com/r/',
            'https://www.reddit.com/user/'
        ]

        req_answer = []
        for req_url in req_list:
            social_url = req_url + self.nickname
            try:
                res = requests.get(social_url)
                if res.ok:
                    print(self.green + '  ' + social_url)
                    req_answer.append(social_url)
                else:
                    print(self.red + '  ' + social_url)
            except requests.RequestException:
                print(self.magenta + '  ' + social_url)

        print(self.reset)
        return req_answer

    def output(self):
        """Вывод результатов поиска."""
        req_answer = self.availability()
        telegram_result = self.telegram()

        len_design = max(35, len(self.nickname) + 35)

        if req_answer or telegram_result:
            print('\n' + '=' * len_design)
            print(f'  Результат для никнейма: {self.nickname}')
            print('-' * len_design)
            for url in req_answer:
                print(f'  {url}')
            if telegram_result:
                print(telegram_result, end="")
        else:
            print(f'{self.red}\n Этот ник в социальных сетях не найден!{self.reset}')

        print('=' * len_design)
        input(f'{Fore.GREEN}Введите любой символ для продолжения... {self.reset}')

# Пример использования класса
if __name__ == "__main__":
    SocialDeanon()
