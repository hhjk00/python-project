from tkinter import *
import tkinter.font as font

root = Tk()
root.geometry('800x640')
root.title('home')
root.resizable(False, False)

font1= font.Font(family="화이트데이10", size = 16)
font2= font.Font(family="Octarine-bold", size = 30)

def data1(): 
    root.destroy()
    import holiday

def data2():
    root.destroy()
    import leisure

def exit():
    root.destroy()
    
f1 = Frame(
    root,
    width=500,
    height=640,
).place(relwidth=0.6,relheight=1)

f2 = Frame(
    root,
    width=300,
    height=640,
    bg='white',
).place(relx=0.6,relwidth=0.4,relheight=1)

image =  PhotoImage(file="logo.png").subsample(3)
img_label = Label(root, image=image)
img_label.place(relx=0.1,rely=0.3, relwidth=0.4, relheight=0.4)

txt_label = Label(root, text="Next Holiday", font=font2)
txt_label.place(relx=0.13, rely=0.25)

Button(
  root,
  text="Holiday",
  command=data1,
  width=14,
  height=2,
  cursor='hand2',
  font=font1,
  relief='groove',
  overrelief='solid',
  bg='white',
).place(relx=0.69,rely=0.3)

Button(
  root,
  text="Leisure", 
  command=data2,
  width=14,
  height=2,
  cursor='hand2',
  font=font1,
  relief='groove',
  overrelief='solid',
  bg='white',
).place(relx=0.69,rely=0.42)

Button(
  root,
  text="Exit", 
  command=exit,
  width=14,
  height=2,
  cursor='hand2',
  font=font1,
  relief='groove',
  overrelief='solid',
  bg='white'
).place(relx=0.69,rely=0.54)

root.mainloop()

