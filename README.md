# Dcinside 

Dcinside is a Korean website similar to Reddit.

**Crawler**

<img width="740" alt="스크린샷 2022-09-26 오후 9 47 42" src="https://user-images.githubusercontent.com/44548828/192280505-019bacd9-595d-4f95-9171-c0b64b9ec25b.png">

**Word Cloud**

```
from konlpy.tag import Hannanum
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class Analyser:
  def __init__(self, df):
    self.df = df

  def get_tokenized(self, text):
    hannanum = Hannanum()
    return hannanum.morphs(text) 

  def get_cleaned(self, text):
    text = ([x for x in text if len(x) > 1])
    d = {i:text.count(i) for i in set(text) if text.count(i) > 1}
    words = ' '.join(d.keys())
    return words

  def get_wordcloud(self, column=''):
    t = analyser.df[column]
    words = self.get_tokenized(' '.join(t))
    words = self.get_cleaned(words)
    words = words.split()
    text = ' '.join(words)
    stop_words = []
    wordcloud = WordCloud(stopwords = stop_words, \
                          font_path='/usr/share/fonts/truetype/NotoSansCJKkr-Medium.otf', \
                          background_color='white', \
                          width=1200, height=800).generate(text)
    plt.figure(figsize=(18,10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
```

```
analyser = Analyser(df)
analyser.get_wordcloud('content')
```

<img width="740" alt="스크린샷 2022-09-26 오후 9 58 01" src="https://user-images.githubusercontent.com/44548828/192282488-076d19d4-d2cf-45b2-843e-071406ac0735.png">

**Macro Writer**

```
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
```

![fir](https://user-images.githubusercontent.com/44548828/188441280-a17bff59-3c78-41f8-9008-e68343108e1e.gif)
![sec](https://user-images.githubusercontent.com/44548828/188441311-92608b5f-05c1-44ab-8b5f-6bb6281da5c6.gif)

