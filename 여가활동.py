import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'Malgun Gothic'

df = pd.read_csv('leisure.csv', encoding='cp949', skiprows=3)
df.replace('-', 0, inplace=True)
df.set_index('항목',inplace=True)
df = df.astype('float')
df = df.reset_index()

year = ["2000", "2004","2007","2009","2011","2013","2015","2017","2019","2021"]
total = []
items = []

for data in range(0,18):
  total.append(list(df.iloc[data][1:11]))
  items.append(df.iloc[data][0])

total_result = pd.DataFrame(total, index=items, columns=year)
total_avg = (total_result.mean(axis=1)).sort_values(ascending = False).head(10)

# total_avg.plot.pie(figsize=(5,5), autopct='%0.1f%%', title='휴일 여가활용방법 (2000~2021)')
# total_avg.plot.barh(title='휴일 여가활용방법 (2000~2021)')
plt.show()