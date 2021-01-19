from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.my_tumblr

import time

### option 적용 ###
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

# 셀레니움을 실행하는데 필요한 크롬드라이버 파일을 가져옵니다.
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
url = 'http://search.danawa.com/dsearch.php?k1=%ED%85%80%EB%B8%94%EB%9F%AC&module=goods&act=dispMain'
driver.get(url)
time.sleep(3)
scroll_n_times = 10


for i in range(scroll_n_times):
    h = 'document.body.scrollHeight/%d'%scroll_n_times
    driver.execute_script("window.scrollTo(0, %s * %d);"%(h, i+1))
    time.sleep(0.5)

soup = BeautifulSoup(driver.page_source, 'html.parser')
lis = soup.select('li.prod_item')

for li in lis:
    try:
        thumb_div_tag = li.select_one('div.thumb_image')
        thumb_a_tag = thumb_div_tag.select_one('a')
        thumb_img_tag = thumb_a_tag.select_one('img')
        name_div_tag = li.select_one('p.prod_name')
        name_a_tag = name_div_tag.select_one('a')
        price_p_tag = li.select_one('p.price_sect')
        price_a_tag = price_p_tag.select_one('a')

        href = thumb_a_tag['href']
        image_url = thumb_img_tag['src']
        name = name_a_tag.text
        price = price_a_tag.text

        if 'noImg_160.gif' in image_url:
            continue
        # print(href, image_url, name, price)
        doc = {
            'url': href,
            'img': image_url,
            'name': name,
            'price': price# DB에는 숫자처럼 생긴 문자열 형태로 저장됩니다.
        }
        db.prod_info.insert_one(doc)

    except:
        pass

driver.quit()

