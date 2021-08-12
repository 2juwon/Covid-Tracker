import json
import requests
import urllib3

urllib3.disable_warnings()

naver_client_info = {
    "ID" : 'yqzkt8lqam',
    "SECRET" : 'RtiiXX9xPfpduPA1RWd85AEG65IGaZwv5VUtHESd'
}

naver_header_map = {
    "Accept": "application/json",
    "Content-Type": "application/json;charset=utf-8",
    "X-NCP-APIGW-API-KEY-ID": naver_client_info["ID"],
    "X-NCP-APIGW-API-KEY": naver_client_info["SECRET"]
}

def parse_geocode(address):
    query = requests.utils.quote(address)
    url = f'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={query}'

    try:
        response = requests.get(url, headers=naver_header_map, verify=False, timeout=5)

        try:
            json_data = json.loads(response.text)
            addresses = json_data.get("addresses")
            if(len(addresses) > 0):
                for address in addresses:
                    x = address.get("x")
                    y = address.get("y")
                    return {'lon' : x, 'lat' : y}
        except json.decoder.JSONDecodeError as decodeerror:
            print("JSONDecodeError : ", decodeerror)
            print("JSON string : ", response.text)
            
    except requests.exceptions.Timeout as timeouterror:
        print("Timeout Error : ", timeouterror)

    except requests.exceptions.SSLError as sslerror:
        print("SSL Error : ", sslerror)

    except requests.exceptions.ConnectionError as connectionerror:
        print("Connection Error : ", connectionerror)
        # See psf/requests#5430 to know why this is necessary.                

    except requests.exceptions.HTTPError as httperror:
        print("Http Error : ", httperror)

    except requests.exceptions.RequestException as error:
        print("AnyException : ", error)

    return None