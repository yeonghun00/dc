from selenium import webdriver
import time
from datetime import date
import random

class Macro():
    def __init__(self, name='ㅇㅇ', password='abcabc',title='title',img ='', content='content'):
        self.driver_path = '/Users/yeonghun/chromedriver' #PATH
        self.driver = webdriver.Chrome(executable_path = self.driver_path)

        self.link = 'https://gall.dcinside.com/mgallery/board/write/?id=kospi' #write link
        self.driver.get(self.link)
        
        self.main_page = self.driver.current_window_handle
        self.popup_page = None

        self.login(name, password)
        self.context(title, img, content)
        self.submit()

        time.sleep(1)
        self.driver.quit()

    def login(self, name, password):
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)

    def context(self, title, img, content):
        self.driver.find_element_by_xpath('//*[@id="subject"]').send_keys(title)

        if img != '': 
            self.driver.find_element_by_xpath('//*[@id="tx_image"]/a').click()
            
            # changing page 
            for handle in self.driver.window_handles: 
                if handle != self.main_page: 
                    self.popup_page = handle
                    
            self.driver.switch_to.window(self.popup_page)
            self.driver.find_element_by_xpath('//*[@id="fileupload"]/div[1]/input').send_keys(img)
            time.sleep(15)
            self.driver.find_element_by_xpath('/html/body/div/div/div[2]/button').click()
            self.driver.switch_to.window(self.main_page)

        self.driver.find_element_by_xpath('//*[@id="chk_html"]').click()
        self.driver.find_element_by_xpath('//html//body').send_keys(content)

    def submit(self):
        self.driver.find_element_by_xpath('//*[@id="write"]/div[5]/button[2]').click()
        

titles = ['프로브의 슬픔','프로브를 아시나요', '프로브', 'date.today().strftime("%Y %m %d 손익인증")',\
          '럴커', '탐사정']
img = '//Users//yeonghun//Desktop//probe.jpg'

for i in range(10):
    wait = random.randint(45, 90)
    time.sleep(wait)
    title = random.choice(titles) 
    content = '.' * random.randint(1,3)
    macro = Macro(title=title, img=img, content=content)
