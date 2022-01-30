import gc
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Processor:

    def __init__(self, i):
        self.index = i
        options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)
        options.add_argument("--disable-gpu")
        options.add_argument('--headless')
        print(f'{self.index} starting chrome . . .')
        self.driver = webdriver.Chrome(options=options)
        self.url = 'https://app.ens.domains/search/{}'
        print(f'{self.index} Chrome ready.')

    def process(self, name):
        query = self.url.format(name)
        self.driver.get(query)
        delay = 10
        try:
            elements = WebDriverWait(self.driver, delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'css-0')))
            result = (elements.text)
        except Exception as exp:
            result = "Error"
        res = {'name': name, 'result': result}
        return (res, self)

    def __del__(self):
        print(f'{self.index} cleaning up . . . ')
        self.driver.close()
        gc.collect()
