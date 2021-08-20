import pymysql
from config import db_info

INFO_TABLE = "covid_info"


def insertInfo(data_list):
    db = pymysql.connect(
        user=db_info['user'],
        passwd=db_info['passwd'],
        host=db_info['host'],
        db=db_info['db'],
        charset=db_info['charset']
    )

    cursor = db.cursor()
    try:
        for data in data_list:
            place = data["place"]
            geocode = place["geocode"]
            date_info = data["date"]['date']

            if(geocode == None):
                longitude = 0
                latitude = 0
            else:
                longitude = geocode['lon']
                latitude = geocode['lat']

            if(date_info == None):
                date_info = ''
            else:
                date_info = date_info

            for date in date_info:
                sql = f"SELECT COUNT(1) FROM {INFO_TABLE} WHERE longitude={longitude} AND latitude={latitude} AND date='{date}'"
                cursor.execute(sql)

                result = cursor.fetchone()

                if result[0]:
                    print(f'이미 있는 데이터 입니다. {data}')
                else:
                    sql = f"INSERT INTO {INFO_TABLE} (si, gu, address, name, date, longitude, latitude) VALUES ('{data['si']}', '{data['gu']}', '{place['address']}', '{data['name']}', '{date}',{longitude}, {latitude})"
                    cursor.execute(sql)
        db.commit()

        print(cursor.rowcount, 'record inserted')
        db.affected_rows()

    finally:
        db.close()
