from request import parse_geocode
from common import extract_date

print(parse_geocode('중앙대로29번길 2-11 뚱보집'))

print(extract_date("2021.7.30(금)"))
print(extract_date("~ 7.30(금)"))
print(extract_date("7.29(목) 14:00분경 현금수납 손님태운 택시기사"))
