import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/user/chromedriver/chromedriver.exe')

def scroll_down():
    global driver
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.6)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            time.sleep(0.9)
            new_height = driver.execute_script("return document.body.scrollHeight")

            try:
                driver.find_element_by_class_name("mye4qd").click()
            except:

               if new_height == last_height:
                   break


        last_height = new_height


if __name__ == '__main__':

    keyword_list = ['يغور'] #영어, 학명, 일본어, 독일어/러시아어, 폴란드어 'ヒョウ', 'леопард', 'Lampart plamisty'
    img_url = []
    for keyword in keyword_list:
        url = 'https://www.google.com/search?q={}&hl=ko&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjRiI_RxZX4AhUDMKYKHdMTCuIQ_AUoAXoECAMQAw&biw=1920&bih=969&dpr=1'.format(keyword)
        driver.get(url)

        time.sleep(1)

        scroll_down()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        images = soup.find_all('img', attrs={'class': 'rg_i Q4LuWd'})

        n = 1
        print('number of img tags: ', len(images))
        for i in images:

            try:
                imgUrl = i["src"]
            except:
                imgUrl = i["data-src"]

            if imgUrl in img_url:
                continue
            else:
                img_url.append(imgUrl)

            with urllib.request.urlopen(imgUrl) as f:
                with open('./jaguar/' + keyword +'_' + str(n) + '.jpg', 'wb') as h:
                    img = f.read()
                    h.write(img)

            n += 1


