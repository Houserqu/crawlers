# -*- coding:UTF-8 -*-
import requests

if __name__ == '__main__':
    r = requests.get("http://www.baidu.com/")
    r.encoding = 'utf-8'
    print((r.text).encode('utf-8'))