from selenium import webdriver
import time
import random
import os

class Macro():
    def __init__(self, name='ㅇㅇ', password='abcabc',title='title',img ='', content='content'):
        self.driver_path = '/Users/yeonghun/chromedriver' #PATH
        self.driver = webdriver.Chrome(executable_path = self.driver_path)

        self.link = 'https://gall.dcinside.com/board/write/?id=neostock' #write link
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
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div/div/div[2]/button').click()

            self.driver.switch_to.window(self.main_page)

        self.driver.find_element_by_xpath('//*[@id="chk_html"]').click()
        self.driver.find_element_by_xpath('//*[@id="tx_canvas_source"]').send_keys(content)

    def submit(self):
        self.driver.find_element_by_xpath('//*[@id="write"]/div[4]/button[2]').click()
        
        
titles = ['삼전 호재 떴다 ㄹㅇ','[속보] 삼성전자 아마존과 스마트배송 산업 계약 체결…', '삼성 다시 상승하는데?ㅋ', '삼전충 입꾹닫 보소',\
          '대깨삼', '삼전충들아 말 좀 해봐']
img = '//Users//yeonghun//Desktop//head_break_samsung.jpg'

for i in range(10):
    wait = random.randint(45, 90)
    time.sleep(wait)
    title = random.choice(titles) + 'ㅋ' * random.randint(0,2)
    content = '낄낄' * random.randint(2,8)
    macro = Macro(title=title, img=img, content=content)
