import gc
from os import stat
import bs4
import requests
from requests_html import HTMLSession


class Processor:

    def __init__(self, i):
        self.index = i
        self.url = "https://app.ens.domains/search/{}"
        self.session = HTMLSession()
        print(f"{self.index} ready.")

    def __str__(self):
        print(f'Worker {self.index}')

    def process(self, name):
        self.url = 'https://google.com/search?q=9780747532743&hl=en'
        query = self.url.format(name)
        res = self.session.get(query)
        res.html.render()
        status = res.html.find('div')
        for s in status:
            print(s.text)
        return ({'status': True}, self)
        # if res.status_code == 200:
        #     soup = bs4.BeautifulSoup(res.text, features='html.parser')
        #     div = soup.find_all("div", {"class": "css-0 e1736otp5"})
        #     for d in div:
        #         print(d.text)
        #     response = {'status': True, 'name': name, 'res': True}
        # else:
        #     response = {'status': False, 'response': res.status_code}
        # return (response, self)