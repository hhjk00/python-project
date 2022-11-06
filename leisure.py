from tkinter import *
import tkinter.font as font
from tkinter.ttk import Notebook,Style
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib

root=Tk()
root.geometry("800x640")
root.title('Holiday')
root.resizable(False, False)

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
font1= font.Font(family="화이트데이10", size = 14)

def home():
    root.destroy()
    import home

def exit():
    root.destroy()

style = Style()
style.theme_create( "yummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [0, 8, 0, 0], "background" : "white"} },
        "TNotebook.Tab": {
            "configure": {"padding": [8, 8], "font" : font1},
            "map":       {"background": [("selected", "#FABC3D")],
                          "expand": [("selected", [2, 2, 0, 0])] } } } )

style.theme_use("yummy")

notebook = Notebook(root)
notebook.place(relwidth=1, relheight=1)

# ───────────────────── 탭1 ─────────────────────
tab1=Frame(notebook)
notebook.add(tab1, text="휴일의 여가 활용")

padding = Label(tab1).pack(pady=10)

label1=Label(tab1, text="휴일의 여가 활용 방법 (2000~2021)", font=font1)
label1.pack()

df = pd.read_csv('leisure.csv', encoding='cp949', skiprows=3)
df.replace('-', 0, inplace=True)
df.set_index('항목',inplace=True)
df = df.astype('float')
df = df.reset_index()

year = ["2000", "2004","2007","2009","2011","2013","2015","2017","2019","2021"]
total = []
items = []
label = []

for data in range(0,18):
  total.append(list(df.iloc[data][1:11]))
  items.append(df.iloc[data][0])

total_result = pd.DataFrame(total, index=items, columns=year)
total_avg = (total_result.mean(axis=1)).sort_values(ascending = False).head(10)

for i in range(0,10):
  label.append(total_avg.index[i])

figure = Figure(figsize=(5,5), dpi=100, facecolor="#F0F0F0")
subplot = figure.add_subplot(111)
canvas = FigureCanvasTkAgg(figure, tab1)
canvas.get_tk_widget().pack(fill=BOTH, expand=0)
subplot.pie(total_avg, labels=label, autopct='%0.1f%%')


# ───────────────────── 탭2 ─────────────────────
tab2=Frame(notebook)
notebook.add(tab2, text="메뉴")

padding = Label(tab2).pack(pady=90)

Button(
  tab2,
  text="Home",
  command=home,
  width=14,
  height=2,
  cursor='hand2',
  font=font1,
  relief='groove',
  overrelief='solid',
  bg='white',
).pack()

padding = Label(tab2).pack(pady=3)

Button(
  tab2,
  text="Exit",
  command=exit,
  width=14,
  height=2,
  cursor='hand2',
  font=font1,
  relief='groove',
  overrelief='solid',
  bg='white',
).pack()

root.mainloop()