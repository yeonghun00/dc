from selenium import webdriver
import time
import random
import os

class Macro():
    def __init__(self, name='ㅇㅇ', password='abcabc',title='tk',context='aaaa'):
        self.driver_path = '/Users/yeonghun/chromedriver' #PATH
        self.driver = webdriver.Chrome(executable_path = self.driver_path)

        self.link = 'https://gall.dcinside.com/board/write/?id=neostock' #write link
        self.driver.get(self.link)

        self.login(name, password)
        self.context(title,context)
        self.submit()

        time.sleep(.5)
        self.driver.quit()

    def login(self, name, password):
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)

    def context(self, title, content):
        self.driver.find_element_by_xpath('//*[@id="subject"]').send_keys(title)

        self.driver.find_element_by_xpath('//*[@id="chk_html"]').click()
        self.driver.find_element_by_xpath('//*[@id="tx_canvas_source"]').send_keys(content)

        self.driver.find_element_by_xpath('//*[@id="tx_image"]/a').click()

    def submit(self):
        self.driver.find_element_by_xpath('//*[@id="write"]/div[4]/button[2]').click()
titles = ['또 삼성전자 계약 체결ㅋㅋㅋㅋ', '삼성전자 호재 떴다 ㅋㅋㅋㅋ', '이재용 석방', '삼전 시외가 상승ㅋㅋㅋㅋㅋ']
image_url = ''
content = '응 아니야~'
context = '<img src="{}" alt="random"> \n <p>{}</p>'.format(image_url, content)

macro = Macro(title=title, context=context)
