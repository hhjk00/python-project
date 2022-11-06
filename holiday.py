from tkinter import *
import tkinter.font as font
from tkinter.ttk import Notebook,Style
from tkinter import scrolledtext
import csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root=Tk()
root.geometry("800x640")
root.title('Holiday')
root.resizable(False, False)

font1= font.Font(family="화이트데이10", size = 14)

def search():
    f = open('holiday.csv', 'r', encoding='utf-8')
    data = csv.reader(f)

    year = list(range(2004, 2025)) 
    value = entry1.get()

    resultBox.delete('0.0', END)

    for row in data:
        if(row[1] == value):
            resultBox.insert(END, row[1] + '년 ' + row[2] + '월 ' + row[3] + '일 ' + row[4] + ' - ' + row[0] + '\n')

    f.close()


def back():
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
notebook.add(tab1, text="연도별 휴일 찾기")

padding = Label(tab1).pack(pady=10)

label1=Label(tab1, text="찾고싶은 연도를 입력하세요.", font=font1)
label1.pack(pady=10)

padding = Label(tab1).pack(pady=1)

tab1_search=Frame(tab1)
tab1_search.pack()

entry1=Entry(tab1_search, width=15, font=font1, text="2004 ~ 2024")
entry1.insert(END, "ex) 2004~2024")
entry1.grid(row=0, column=0)

photo = PhotoImage(file="search.png").subsample(1)
btn1=Button(
    tab1_search,
    width=30,
    height=30,
    cursor='hand2',
    font=font1,
    relief='flat',
    image=photo,
    command=search
    )
btn1.grid(row=0, column=1, padx=7)

padding = Label(tab1).pack(pady=10)

resultBox = scrolledtext.ScrolledText(
    tab1,
    width=38,
    height=15, 
    border='1', 
    font=font1,
    )
resultBox.insert(END, "검색 결과를 출력합니다.")
resultBox.pack()


# ───────────────────── 탭2 ─────────────────────
tab2=Frame(notebook)
notebook.add(tab2, text="연도별 휴일 그래프")

padding = Label(tab2).pack(pady=10)

label2=Label(tab2, text="연도별 휴일 그래프 (2004~2024)", font=font1)
label2.pack(pady=10)

f = open('holiday.csv', 'r', encoding='utf-8')
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

figure = Figure(figsize=(10,4), dpi=100, facecolor="#F0F0F0")
subplot = figure.add_subplot(111)
canvas = FigureCanvasTkAgg(figure, tab2)
canvas.get_tk_widget().pack(fill=BOTH, expand=0)
subplot.plot(year, day, color='#FABC3D', linewidth=3, marker='o', markerfacecolor='#0C7367', markersize=9)
subplot.set_xlim([2003.1, 2025.8])
subplot.grid()

f.close()

# ───────────────────── 탭3 ─────────────────────
tab3=Frame(notebook)
notebook.add(tab3, text="메뉴")

padding = Label(tab3).pack(pady=90)

Button(
  tab3,
  text="Home",
  command=back,
  width=14,
  height=2,
  cursor='hand2',
  font=font1,
  relief='groove',
  overrelief='solid',
  bg='white',
).pack()

padding = Label(tab3).pack(pady=3)

Button(
  tab3,
  text="Exit",
  command=back,
  width=14,
  height=2,
  cursor='hand2',
  font=font1,
  relief='groove',
  overrelief='solid',
  bg='white',
).pack()

root.mainloop()