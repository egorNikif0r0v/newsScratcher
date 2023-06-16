
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from topics import Topics
from news import News
import urllib


def __initBrowser(driver: str =\
                 'driver/chromedriver.exe') -> Chrome:
    option = Options()
    option.add_argument("--disable-infobars") 
    option.add_argument('headless')
    service = Service(driver)

    return webdriver.Chrome(service=service, options=option)


#link >>> https://www.bbc.com/news/
def getNewsBBC(    topic: Topics,\
                newsCount: int = 6) -> list[News]:
    
    browser = __initBrowser()
    browser.get(f'https://www.bbc.com/news/{topic.value}')
    print(f'https://www.bbc.com/news/{topic.value}')
    basePath: str = f'//*[@id="topos-component"]/div[3]/div[2]/div[1]/div/div/div/div[3]/div'
    newss: list[News] = []

    for item in range(1, newsCount):
        title: str = browser.find_element(By.XPATH, f'{basePath}/div[{item}]/div/div[2]/div[1]/a/h3')\
            .get_attribute('textContent')
        discription: str = browser.find_element(By.XPATH, f'{basePath}/div[{item}]/div/div[2]/div[1]/p')\
            .get_attribute('textContent')
        link: str = browser.find_element(By.XPATH, f'{basePath}/div[{item}]/div/div[2]/div[1]/a')\
            .get_attribute('href')
        time: str = browser.find_element(By.XPATH, f'{basePath}/div[{item}]/div/div[2]/div[2]/ul/li[1]')\
            .get_attribute('textContent')
        theme: str = browser.find_element(By.XPATH, f'{basePath}/div[{item}]/div/div[2]/div[2]/ul/li[2]')\
            .get_attribute('textContent')
        
        news: News = News(
                link=link,
                head=title,
                discription=discription,
                time=time,
                theme=theme,
            )
        news.log()
        src = browser.find_element(By.XPATH, f'{basePath}/div[{item}]/div/div[1]/div/div/img').get_attribute('src')
        urllib.request.urlretrieve(src, f'image/{news.getHash()}newsImage.png')
        newss.append(news)
        

    return newss