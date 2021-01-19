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

driver = webdriver.Chrome('chromedriver',options=options)
##################

# 셀레니움을 실행하는데 필요한 크롬드라이버 파일을 가져옵니다.
driver = webdriver.Chrome('/usr/local/bin/chromedriver')

url = 'http://search.danawa.com/dsearch.php?k1=%ED%85%80%EB%B8%94%EB%9F%AC&module=goods&act=dispMain'

driver.get(url)

time.sleep(2)


tum_imgs = driver.find_elements_by_class_name('click_log_product_standard_img_')
driver.get(tum_imgs[0].get_attribute('src'))
req = driver.page_source

soup = BeautifulSoup(req, 'html.parser')
img_urls = soup.select("body > img")
print(img_urls)



# tumblrs = soup.select('#productListArea > div.main_prodlist.main_prodlist_list > ul > li')
# for tumblr in tumblrs:
#     a_tag = tumblr.select_one('div > div > a > img')['alt']
#     if a_tag is not None:
#         print(a_tag)
