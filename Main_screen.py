from tkinter import *
import time
from tkinter import ttk
from click import style
from tkinter.ttk import Progressbar


app = Tk()
app.title("PingPong")


width_of_window = 427
height_of_window = 272
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
app.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

s = ttk.Style()
s.theme_use('clam')
s.configure("blue.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress = Progressbar(app, style ="blue.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, mode='determinate',)

def main_window():
    import game
  

def bar():

    l4=Label(app,text='Loading...',fg='white',bg=a)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    
    import time
    r=0
    for x in range(100):
        progress['value']=r
        app.update_idletasks()
        time.sleep(0.03)
        r=r+1
    
    app.destroy()
    main_window()
        
    
progress.place(x=-10,y=235)


a='#249794'
Frame(app,width=427,height=241,bg=a).place(x=0,y=0)  #249794
b1=Button(app,width=10,height=1,text='Lets Play',command=bar,border=0,fg=a,bg='white')
b1.place(x=170,y=200)

name1=Label(app,text='PingPong',fg='white',bg=a)
lst1=('Calibri (Body)',18,'bold')
name1.config(font=lst1)
name1.place(x=50,y=80)


app.mainloop()

