from selenium import webdriver

from crawling.config import driver_path
from crawling.request import parse_geocode
from crawling.common import extract_date

def start_crawling():
    web_path = "https://www.busan.go.kr/covid19/Travelhist.do"

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
        geocode = parse_geocode(address=address)
        print(f"{si} {gu} {address} {name} {date} {geocode}")

    driver.close()
