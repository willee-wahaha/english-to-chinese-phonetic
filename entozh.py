import tkinter as tk
from tkinter import Label
from PIL import ImageTk, Image

list1 = ["ㄅ","ㄆ","ㄇ","ㄈ","ㄉ","ㄊ","ㄋ","ㄌ","ㄍ","ㄎ","ㄏ","ㄐ","ㄑ","ㄒ","ㄓ","ㄔ","ㄕ","ㄖ","ㄗ","ㄘ","ㄙ","ㄧ","ㄨ","ㄩ","ㄚ","ㄛ","ㄜ","ㄝ","ㄞ","ㄟ","ㄠ","ㄡ","ㄢ","ㄣ","ㄤ","ㄥ","ㄦ"," ","ˊ","ˇ","ˋ","˙"]
list2 = ["1","q","a","z","2","w","s","x","e","d","c","r","f","v","5","t","g","b","y","h","n","u","j","m","8","i","k",",","9","o","l",".","0","p",";","/","-"," ","6","3","4","7"]

def change():
    thein=str(a.get())

    lista = list(thein)

    for i in range(0,len(thein)):
        for j in range(0,42):
            if(lista[i] == list2[j]):
                lista[i] = list1[j]
                break

    b.set("".join(lista))

win = tk.Tk()
try:
    iconpic = 'icon.ico'
    win.iconbitmap(iconpic)
except Exception as e:
    None
win.title('英文轉注音')
win.resizable(False, False)

w = 600
h = 350

try:
    try:
        backpic = 'back.png'
        backtemp = Image.open(backpic)
    except Exception as e:
        backpic = 'back.jpg'
        backtemp = Image.open(backpic)
    except Exception as e2:
        NONE
    (w,h) = backtemp.size
    if(int(600/w*h) > 600):
        w = int(600/h*w)
        h = 600
    else:
        h = int(600/w*h)
        w = 600
    bc = ImageTk.PhotoImage(backtemp.resize((w,h)))
    panel = Label(win, image = bc)
    panel.place(x=0, y=0)
except Exception as e:
    None

geo = str(w) + 'x' + str(h)
win.geometry(geo)

fm = tk.Frame(win, bg='white', width=200, height=20)
if(h >= 408):
    the_y = h/2-112
else:
    the_y = h/4-10

if(w <= 380):
    the_x = w/2-100
else:
    the_x = w-250
fm.place(x=the_x, y=the_y)

a =tk.StringVar(None, '')
ent = tk.Entry(fm, width=200, justify='left', textvariable=a)
ent.place(x=0, y=0)

fmb = tk.Frame(win, bg='white', width=70, height=50)
if(w <= 380):
    the_x = w/2-35
else:
    the_x = w-185
fmb.place(x=the_x, y=h/2-25)

btnstr = tk.StringVar()
btnstr.set('   轉換   ')
btn = tk.Button(fmb, bg='#CCCCCC', fg='black', textvariable=btnstr, font=('微軟正黑體', 12), command=change, pady=10)
btn.place(x=0, y=0)

fmo = tk.Frame(win, bg='white', width=200, height=20)
if(h >= 408):
    the_y = h/2+92
else:
    the_y = h/4*3-10

if(w <= 380):
    the_x = w/2-100
else:
    the_x = w-250
fmo.place(x=the_x, y=the_y)

b = tk.StringVar(None, ' ')
out = tk.Entry(fmo, width=200, font=('微軟正黑體', 8), justify='left', textvariable=b)
out.place(x=0, y=0)

win.mainloop()

