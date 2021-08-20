from datetime import date
from os import replace
import re

# Ref. https://regexr.com/
def extract_date(src):
    # date
    # matches = datefinder.find_dates(src)

    # src = src.replace(" ","")
    # idx = src.find(r'\d[0-9]')
    # if(idx >= 0):
    #     src = src[idx:]

    m = re.findall(r"\d{2}(?:\d{2})?[.]\d{1,2}[.]\d{1,2}", string=src)
    prefix = ''
    if len(m) == 0:
        m = re.findall(r"\d{1,2}[.]\d{1,2}",string=src)        
        prefix = '2021.'

    if m:
        dates = []
        for date in m:
            dates.append(f'{prefix}{date}')
        
        return dates

print(extract_date('8.8(일) 18:42-20:12 8.9(월) 14:24-16:53'))
