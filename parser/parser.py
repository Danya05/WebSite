import requests
import re
import time
import datetime
from bs4 import BeautifulSoup
from .models import Coins


class parse_bitcoin:
    prev_value = 0

    URL = 'https://coinmarketcap.com/currencies/bitcoin/'

    type = Coins

    while True:
        try:
            page = requests.get(URL, headers={'Cache-Control': 'no-cache', "Pragma": "no-cache"})

            soup = BeautifulSoup(page.content, "html.parser")

            st1 = re.split('<div class="priceValue"><span>', str(soup.find_all('div', class_='priceValue')[0]))[1]

            res = re.split('</span></div>', st1)[0]

            if prev_value != res:
                Coins.objects.filter(id=3).update(cost=res)
                Coins.objects.filter(id=3).update(date=datetime.datetime.now())

            time.sleep(10)
        except:
            continue
