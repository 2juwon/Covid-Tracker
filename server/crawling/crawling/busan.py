from selenium import webdriver

from config import driver_path
from request import get_geocode
from common import extract_date
from datasource import insertInfo

import requests
from bs4 import BeautifulSoup

web_path = "https://www.busan.go.kr/covid19/Travelhist.do"

def start_crawling():

    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(url=web_path)

    print(driver.current_url)

    driver.implicitly_wait(time_to_wait=5)

    assert '부산광역시 코로나' in driver.title

    titleEle = driver.find_element_by_class_name('titPage')
    assert '확진자 이동경로' in titleEle.text

    table = driver.find_element_by_class_name('boardList')
    headers = table.find_elements_by_tag_name('th')
    data_list = table.find_elements_by_class_name('m_view')

    header_len = len(headers)
    data_len = len(data_list)

    info_list = []
    list_idx = -1
    for i in range(data_len):
        text = data_list[i].text
        idx = i % (header_len)
        if(idx == 0):
            data = list()
            data.append(text)
            info_list.append(data)
            list_idx += 1
        else:                
            info_list.__getitem__(list_idx).append(text)

    for info in info_list:
        si = info[0]
        gu = info[1]
        type = info[2]
        name = info[3]
        address = info[4]        
        date = extract_date(info[5])
        geocode = get_geocode(address=address)
        print(f"{si} {gu} {address} {name} {date} {geocode}")

    driver.close()

def start_scrapping():
    print("Start Busan Scrapping...")
    req = requests.get(web_path)

    html = req.text

    soup = BeautifulSoup(html, 'html.parser')

    soup.select('#contents > div > div > div > div > div > table > tbody > .m_view')

    si = soup.select('#contents > div > div > div > div > div > table > tbody > tr > td:nth-child(1)')
    gu = soup.select('#contents > div > div > div > div > div > table > tbody > tr > td:nth-child(2)')
    place_type = soup.select('#contents > div > div > div > div > div > table > tbody > tr > td:nth-child(3)')
    store_name = soup.select('#contents > div > div > div > div > div > table > tbody > tr > td:nth-child(4)')
    address = soup.select('#contents > div > div > div > div > div > table > tbody > tr > td:nth-child(5)')
    date = soup.select('#contents > div > div > div > div > div > table > tbody > tr > td:nth-child(6)')
    
    # for d_ele in date:
    #     soup2= BeautifulSoup(d_ele, 'html.parser') 
    #     aa =soup2.select('p')

    info_list = []
    for info in si:
        data = {}
        data["si"] = info.text
        info_list.append(data)

    for idx, el in enumerate(gu):
        info_list[idx]["gu"] = (el.text)

    for idx, el in enumerate(place_type):
        info_list[idx]["type"] = el.text
        
    for idx, el in enumerate(store_name):
        info_list[idx]["name"] = el.text

    for idx, el in enumerate(address):
        info_list[idx]["place"] = {
            "address": el.text,
            "geocode": get_geocode(address=el.text)
        }
        
    for idx, el in enumerate(date):
        info_list[idx]["date"] = {
            "date" : extract_date(el.text),
            "origin": el.text
        }

    print(info_list)

    # insertInfo(info_list)

start_scrapping()