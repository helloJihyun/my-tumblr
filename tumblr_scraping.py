from selenium import webdriver
import requests
from bs4 import BeautifulSoup

# # 타겟 URL을 읽어서 HTML를 받아오고,
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('http://search.danawa.com/dsearch.php?k1=%ED%85%80%EB%B8%94%EB%9F%AC&module=goods&act=dispMain',headers=headers)
#
# soup = BeautifulSoup(data.text, 'html.parser')


import time

### option 적용 ###
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

# 셀레니움을 실행하는데 필요한 크롬드라이버 파일을 가져옵니다.
driver = webdriver.Chrome('/Users/jeonghan.joo/Downloads/chromedriver')
#driver = webdriver.Chrome('/usr/local/bin/chromedriver')

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
        div_tag = li.select_one('div.thumb_image')
        a_tag = div_tag.select_one('a')
        img_tag = a_tag.select_one('img')
        href = a_tag['href']
        image_url = img_tag['src']

        if 'noImg_160.gif' in image_url:
            continue

        print(href, image_url)
    except:
        pass

driver.quit()

