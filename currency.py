import requests
from datetime import datetime
from datetime import date
from bs4 import BeautifulSoup
from colorama import Fore


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

rub_url = 'https://www.google.com/search?rlz=1C1CHZL_enRU818RU818&sxsrf=ALeKk02vy1K6w-_gkKbw3CvuSzzCDLrDyA%3A1604230233347&ei=WZyeX-rXFMvKrgTphLWABA&q=%241+to+rub&oq=%241+to+rub&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIFCAAQyQMyCAgAEBYQChAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46AggAOgcIIxDJAxAnOgQIABBDOgkIIxAnEEYQggJQs7gBWJHIAWDiyQFoAXAAeACAAZkBiAG0CJIBAzMuN5gBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwiq6Mipn-HsAhVLpYsKHWlCDUAQ4dUDCA0&uact=5'
eur_url = 'https://www.google.com/search?rlz=1C1CHZL_enRU818RU818&sxsrf=ALeKk029M4mB-NXlSW3SMjwxRNmE_uojMQ%3A1604230265072&ei=eZyeX5PrA9CFrwSJg5eADw&q=%241+to+eur&oq=%241+to+eur&gs_lcp=CgZwc3ktYWIQAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwA1AAWABg4qQRaABwAHgAgAGgAYgBjQKSAQMwLjKYAQCqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwjTi9m4n-HsAhXQwosKHYnBBfAQ4dUDCA0&uact=5'


def get_cur(page):
    full_page = requests.get(page, headers=headers)
    soap = BeautifulSoup(full_page.content, 'html.parser')
    cur = soap.findAll(
        "span", {"class": "DFlfde", "class": "SwHCTb", 'data-precision': 2})[0].text
    return cur


today = date.today()
current_date = today.strftime("%d.%m.%Y")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print('On date ' + Fore.BLUE + current_date + ' ' + current_time + ':' +
      Fore.GREEN + ' $1' + Fore.WHITE + ' equal ' + Fore.GREEN + get_cur(rub_url) + ' RUB' + Fore.WHITE)
print('On date ' + Fore.BLUE + current_date + ' ' + current_time + ':' +
      Fore.GREEN + ' $1' + Fore.WHITE + ' equal ' + Fore.GREEN + get_cur(eur_url) + ' EUR' + Fore.WHITE)
