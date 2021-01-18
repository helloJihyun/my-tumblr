from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.implicitly_wait(2)
driver.get('http://search.danawa.com/dsearch.php?k1=%ED%85%80%EB%B8%94%EB%9F%AC&module=goods&act=dispMain')

locate = '#productItem8006071 > div > div.prod_info > p > a'
element = driver.find_element_by_css_selector(locate)
print(element.text.split('\n'))


