# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {'referer': 'https://www.qichacha.com/','authority': 'www.qichacha.com', 'method': 'GET', 'path': '/search?key=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4', "scheme": 'https', 'cookie':'PHPSESSID=ba1c25t2st5dlriopbhh0crb42; UM_distinctid=163b6712cb9124-022a0a54dfca99-336c7706-13c680-163b6712cba1c1; zg_did=%7B%22did%22%3A%20%22163b6712cc58c0-0e786fbe00018b-336c7706-13c680-163b6712cc6c8%22%7D; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1527774261; hasShow=1; acw_tc=AQAAAHqHDSDtyQUAEfWFfNZCt2+y+ZFi; CNZZDATA1254842228=1598150477-1527769681-https%253A%252F%252Fwww.google.com%252F%7C1527775081; _uab_collina=152777591693104384620282; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201527774260431%2C%22updated%22%3A%201527776011372%2C%22info%22%3A%201527774260435%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.google.com%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1527776012'}

    r = requests.get("https://www.qichacha.com/search?key=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4", headers=headers)
    r.encoding = 'utf-8'

    
    print((r.text).encode('utf-8'))
    soup = BeautifulSoup(r.text)
    print(soup.title)
