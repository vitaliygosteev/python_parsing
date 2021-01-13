import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

rub_url = 'https://www.google.com/search?rlz=1C1CHZL_enRU818RU818&sxsrf=ALeKk00iyVBpYvmyWkVSdaAOV96yukI9Bw%3A1604236848046&ei=MLaeX9W1Au7HrgT1l5HIDA&q=1+rub+to+usd&oq=1+rub&gs_lcp=CgZwc3ktYWIQAxgAMgUIABCRAjIECAAQQzIECAAQQzIECAAQQzICCAAyAggAMgIIADIFCAAQywEyAggAMgIIADoHCAAQRxCwAzoGCAAQBxAeOgQIABAeOgYIABAKEB46BggAEAgQHlD7LljIPGDbRmgAcAB4AIABkwGIAYEDkgEDMC4zmAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab'
usd_url = 'https://www.google.com/search?q=%241+to+rub&rlz=1C1CHZL_enRU818RU818&oq=%241+to+rub&aqs=chrome.0.69i59j0i457j0i10i22i30j0i22i30l5.6318j0j4&sourceid=chrome&ie=UTF-8'


def get_cur(page):
    full_page = requests.get(page, headers=headers)
    soap = BeautifulSoup(full_page.content, 'html.parser')
    cur = soap.findAll(
        "span", {"class": "DFlfde", "class": "SwHCTb"})[0].text
    return cur


def usd_to_rub(inp):
    return inp * get_cur()


def rub_to_usd(inp):
    return inp * get_cur()


def ask_value():
    user_inp = int(input('Provide a number: '))
    return user_inp


def converter():
    req = input('Do you want to convert usd or rub? Choose one: ')
    if req.lower() == 'usd':
        try:
            user_inp = ask_value()
        except:
            print('Must be an integer')
            converter()
        else:
            res = user_inp * float(get_cur(usd_url).replace(',', '.'))
            print('$' + str(user_inp) + ' is ' + str(res) + ' rub')
    elif req.lower() == 'rub':
        try:
            user_inp = ask_value()
        except:
            print('Must be an integer')
            converter()
        else:
            res = user_inp * float(get_cur(rub_url).replace(',', '.'))
            print(str(user_inp) + ' rub is ' + '$' + str(res))
    else:
        print('Please, provide "usd" or "rub"')
        converter()


converter()
