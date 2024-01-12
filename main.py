# proxy maker 
import requests
from bs4 import BeautifulSoup

def proxy_maker():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    proxies = []
    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) > 1:
            proxies.append(cols[0].text + ':' + cols[1].text)
    return proxies

proxies = proxy_maker()

def get_proxies():
    return proxies

def set_proxies(proxies):
    global _proxies
    _proxies = proxies
    return _proxies
if __name__ == '__main__':
    print(get_proxies())