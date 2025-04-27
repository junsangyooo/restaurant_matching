import csv
import requests

API_KEY = "7747416a776a73733439746c764e47"
REGION_CODE = {
    "Yongsan" : "_YS",
    "Gangnam" : "_GN",
    "Gangdong" : "_GD",
    "Gangbuk" : "_GB",
    "Gangseo" : "_GS",
    "Gwanak" : "_GA",
    "Gwangjin" : "_GJ",
    "Guro" : "_GR",
    "a" : "a",
    "b" : "b",
    "c" : "c",
    "d" : "d",
    "e" : "e",
    "g" : "g"
}
region = "Yongsan"
seoul_data_api_url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/xml/LOCALDATA_072404/1/5/"
specific_region_data_api_url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/xml/LOCALDATA_072404{REGION_CODE[region]}/1/5/"
res = requests.get(seoul_data_api_url)
json_data = res.json()

with open('vaccin.csv', 'w', encoding='utf-8')as f:
    wr = csv.DictWriter(f, fieldnames = json_data['data'][0].keys())
    wr.writeheader()
    wr.writerows(json_data['data'])
df = pd.read_json(json_data)
df.to_csv('restaurant_data.csv', encoding='utf-8', index=False)

search_key_word = "한강로동맛집"
naver_map_search_url = f"https://m.map.naver.com/search?query={search_key_word}"

response = requests.get(naver_map_search_url)
response.raise_for_status()