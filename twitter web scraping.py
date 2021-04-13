from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time

path = r"/path/chromedriver"

# ใส่ option don't show chromedriver  แต่อาจได้ผลลัพธ์ไม่เหมือนเปิด
'''
opt = webdriver.ChromeOptions()
opt.add_argument('headless')

driver = webdriver.Chrome(path,options=opt)
'''

driver = webdriver.Chrome(path)

def twitter(twitter_name):

    url = "https://twitter.com/{}".format(twitter_name)

    driver.get(url)

    time.sleep(3)

    
    # คำสั่งเลือน scroll
    pixel = 10000

    for i in range(6):
        driver.execute_script('window.scrollTo(0,{})'.format(pixel))
        time.sleep(3)
        pixel += 10000
    

    """
    for i in range(3):
        driver.execute_script('window.scrollTo(0,10000)')
        time.sleep(3)
    """


    page_html = driver.page_source

    data = soup(page_html, 'html.parser')


    posts = data.find_all('span',{'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})


    founddot = False
    allpost = []


    for p in posts:
        txt = p.text

        if founddot == True:
            allpost.append(txt)
            founddot = False

        if txt == "·":
            founddot = True

    
    return allpost

twittername = ['elonmusk','SpaceX','BillGates']

for tn in twittername:
    textto = ''
    post = twitter(tn)
    print("----- {} -----".format(tn))
    for a in post:
        textto += a + '\n\n'

    print(textto)
        


driver.close()
print('##### complete #####')