from datetime import date
from os import replace
import re

# "2021.8.4(수) 11:16~14:35"
# "7.29(목) 14:00분경 현금수납 손님태운 택시기사"
def extract_date(src):
    # date
    # matches = datefinder.find_dates(src)

    # src = src.replace(" ","")
    # idx = src.find(r'\d[0-9]')
    # if(idx >= 0):
    #     src = src[idx:]

    print(src)
    m = re.search(r"\d{2}(?:\d{2})?.\d{1,2}.\d{1,2}", string=src)
    if m:
        print('FMath found: ', m.group())
        return m.group()
    else:
        m = re.search(r"\d{1,2}.\d{1,2}",string=src)
        if m:
            print('SMath found: ', m.group())
            return f'2021.{m.group()}'
        else:
            print('No match')
