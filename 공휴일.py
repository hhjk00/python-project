import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getHoliDeInfo'
key = 'ub4QuQhtgvHUPfDOeHTqn77ldYRLAurjYf1wu6VIJkcqA4yx8yN8NqZP1NR7Fb7+OgmhZ+L80rYq9xJKF5AOgQ=='
year = list(range(2004, 2025))
days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

df = pd.DataFrame()
title = []
date = []
day = []

for y in year:
  params = {'serviceKey' : key,
        'solYear' : y,
        'numOfRows' : 100,
        }
  response = requests.get(url, params=params)

  soup = BeautifulSoup(response.content, "lxml")
  items = soup.find_all("item")

  for item in items:
    title.append(item.datename.text)
    date.append(int(item.locdate.text))

    date_s = item.locdate.text
    yy = int(date_s[:4])
    mm = int(date_s[4:6])
    dd = int(date_s[6:8])

    d = days[datetime.date(yy, mm, dd).weekday()]
    day.append(d)


df['title'] = title
df['date'] = date
df['day'] = day

print(df)
df.to_csv('./holiday.csv')
