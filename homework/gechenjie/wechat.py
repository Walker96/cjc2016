# coding=utf-8
import re
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
file_object = open('1.html', 'w')
url1 = 'http://mp.weixin.qq.com/s?src=3&timestamp=1463193360&ver=1&signature=VqOGyWi-x1lMTuPd2nEa4u9ciwJKaw-qjgY1xwlrGpQ4aBBmEtSwGXIBHoN7o5bYcl4mgC2iaq1pO6VrYqZAU4xELLr27AdiC3EUf0ZIx*nIzpb4XCHVoTZxXnl3gRCY5-Bnun-38Vqqti6R6tplTqcBbx3aPSsba5FQyudYU4k='
driver = webdriver.PhantomJS(executable_path='C:/Users/Administrator/AppData/Roaming/npm/node_modules/phantomjs/lib/phantom/bin/phantomjs.exe')
# laptop:'C:/Users/Administrator/AppData/Roaming/npm/node_modules/phantomjs/lib/phantom/bin/phantomjs.exe'
# small:'C:/Users/Patrick/AppData/Roaming/npm/node_modules/phantomjs/lib/phantom/bin/phantomjs.exe'
driver.get(url1)
p1 = re.compile('<img[^>]+data-src="([^"]+)"')
p2 = re.compile('/0\?wx\_fmt\=')
p3 = re.compile('([0-9]+)x([0-9]+)')
p4 = re.compile('<(?!img|br).*?>')
p5 = re.compile('<img[^>]+data-src="[^"]+"[^>]+\ssrc="([^"]+)"')
p6 = re.compile('<img[^>]+data-src[^>]+>')
page_content = driver.find_element_by_class_name('rich_media_content')
rich_content = page_content.get_attribute("innerHTML")
print rich_content
yueduliang = driver.find_element_by_css_selector('sg_readNum3')
# print yueduliang
imglist = re.findall(p1, rich_content)
imglistsrc = re.findall(p5, rich_content)
imgitems = re.findall(p6, rich_content)
imglen = len(imglist)
picscreenshot = []
plain_text = re.sub(p4, '', rich_content)
for i in range(0, imglen):
    driver.get(imglist[i])
    # filename = str(i)+'.png'
    pictitle = re.search(p3, driver.title)
    picwidth = pictitle.group(1)
    picheight = pictitle.group(2)
    driver.set_window_size(picwidth, picheight)
    # print picwidth + ',' + picheight
    picscreenshot.append(driver.get_screenshot_as_base64())
    # print picscreenshot[0] + '\n *****************************'
    plain_text = plain_text.replace(imglistsrc[i], str(picscreenshot[i]))
file_object.write(plain_text)
file_object.close()
# post data
# r = requests.post(,)
# postcode = r.status_code
driver.quit()
