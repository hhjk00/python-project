# 🏖️ Next Holiday
> Python을 활용하여 공휴일 데이터와 휴일 여가 활용 방법 데이터를 분석한 데이터를 시각화하여 GUI로 표현했습니다.

### 데이터 출처
- 한국천문연구원_특일 정보 : https://www.data.go.kr/data/15012690/openapi.do
- 주말·휴일의 여가활용 방법  : https://gsis.kwdi.re.kr/statHtml/statHtml.do?orgId=338&tblId=DT_1LHB021#

### 기술 스택
`python` `tkinter` `matplotlib` `pandas` `BeautifulSoup` `requests`

<br>

# 📝 데이터 분석
Google Colab을 활용하여 데이터를 분석하고 python에 적용시켰습니다.
## 공휴일 데이터
```py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getHoliDeInfo'
key = '발급받은 key'

years = list(range(2004, 2025))
days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

# 데이터 프레임을 생성합니다.

df = pd.DataFrame()
title = []
year = []
month = []
date = []
day = []

for y in years:
  params = {'serviceKey' : key,
        'solYear' : y,
        'numOfRows' : 100,
        }
  response = requests.get(url, params=params)

  soup = BeautifulSoup(response.content, "lxml")
  items = soup.find_all("item")
  
  # 불러온 데이터를 파싱하여 item 태그의 데이터를 추출합니다.

  for item in items:
    title.append(item.datename.text)

    date_all = item.locdate.text
    yy = int(date_all[:4])
    mm = int(date_all[4:6])
    dd = int(date_all[6:8])
    d = days[datetime.date(yy, mm, dd).weekday()]
    
    year.append(yy)
    month.append(mm)
    date.append(dd)
    day.append(d)
    
    # 추출된 데이터에서 필요한 정보를 분할하여 배열에 데이터를 추가합니다.

df['title'] = title
df['year'] = year
df['month'] = month
df['date'] = date
df['day'] = day

# 데이터 프레임 각 columns에 값을 대입합니다.

print(df)
df.to_csv('./holiday.csv', index=None)

# 완성 된 데이터 프레임을 csv파일로 저장합니다.
```

<br>

```py
import csv

# 저장한 csv 파일을 불러옵니다.

f = open('/content/holiday.csv', 'r', encoding='utf-8')
data = csv.reader(f)

year = list(range(2004, 2025))

search = input('연도 검색 : ')

for row in data:
  if(row[1] == search):
    print(row[1] + '년 ' + row[2] + '월 ' + row[3] + '일 ' + row[4] + ' - ' + row[0])
    
# 검색 결과를 출력합니다.
```

<br>

```py
import csv
import matplotlib.pyplot as plt

# 저장한 csv 파일을 불러옵니다.

f = open('/content/holiday.csv', 'r', encoding='utf-8')
data = csv.reader(f)

next(data)

year = list(range(2004, 2025))
len = 0
year_num = []
day = []

for row in data:
  year_num.append(int(row[1]))

for i in range(0,21):
  day.append(year_num.count(year[i]))
  
  # 데이터의 연도와 일치하는 행을 count하여 배열에 해당 연도의 휴일 수를 대입합니다.

plt.figure(figsize=(10,4))
plt.grid(True)
plt.plot(year, day, color='orange')
plt.xlim([2003.1, 2025.8]) 
plt.show()

# 데이터를 원 그래프로 출력합니다.
```

<br>

## 여가활동 데이터
```py
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 한글 폰트 깨짐 방지
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('/content/leisure.csv', encoding='cp949', skiprows=3)
df.replace('-', 0, inplace=True)
df.set_index('항목',inplace=True)
df = df.astype('float')
df = df.reset_index()

# 데이터가 없는 곳의 값을 - 에서 0 으로 변환시키고, int 값을 float로 변환합니다.

year = ["2000", "2004","2007","2009","2011","2013","2015","2017","2019","2021"]
total = []
woman = []
man = []
items = []

for data in range(0,18):
  total.append(list(df.iloc[data][1:11]))
  items.append(df.iloc[data][0])
  
# 불러온 데이터에서 특정 구간의 데이터를 추출하여 배열에 추가합니다.

total_result = pd.DataFrame(total, index=items, columns=year)
total_avg = (total_result.mean(axis=1)).sort_values(ascending = False).head(10)

# 2차원 배열을 데이터 프레임 구조로 변환하여 각 행의 평균을 구한 후 내림차순으로 정렬합니다.

total_avg.plot.pie(figsize=(5,5), autopct='%0.1f%%')
plt.show()

# 데이터를 선 그래프로 출력합니다.
```

<br>

# 💻 화면 시연
Tkinter를 활용하여 GUI를 만들었고 Frame과 Notebook을 이용하여 화면을 구성했습니다.

## 🏖️ HOME
![image](https://user-images.githubusercontent.com/97223653/212536730-6962aa59-8fdf-4043-8497-46424ecc2d4e.png)

버튼을 클릭하면 현재 화면을 destroy 하여 종료하고 해당되는 화면을 import 하여 창을 띄웁니다.

<br>

## 🏖️ Holiday
![image](https://user-images.githubusercontent.com/97223653/212536760-7c7eae6c-ed35-4831-9ae3-0d026e8ca88d.png)
 
![image](https://user-images.githubusercontent.com/97223653/212536781-e15f9741-9146-45e1-90df-fa73c4e163a8.png)

분석한 데이터를 이용하여 휴일 정보를 검색합니다. 2004년~2024년의 정보를 검색할 수 있습니다.

<br>

![image](https://user-images.githubusercontent.com/97223653/212536791-e694fd71-9b90-47e6-90f0-46af40145d53.png)

연도 별 휴일 수를 선 그래프로 보여줍니다.

![image](https://user-images.githubusercontent.com/97223653/212536800-ba138417-d1d4-41af-afb2-146b31ac0d20.png)

메뉴 탭에는 홈으로 돌아갈 수 있는 버튼과 종료 버튼이 있습니다.

<br>

## 🏖️ Leisure
![image](https://user-images.githubusercontent.com/97223653/212536808-cdb0fdb0-7869-4ff5-953e-adca689ef076.png)

여가 활동 항목 데이터의 평균 데이터를 원 그래프로 나타냅니다.

