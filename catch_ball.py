from  tkinter import *
from random import randrange as rn, choice
import time

root = Tk()

c = Canvas(root, bg='grey',width=800, height=800)
c.pack() #fill=BOTH,expand=1)

colors = ['black','red','grey','lightgreen','green','cyan','yellow','orange','brown','red','blue','pink']

def ball_create():
    global x,y,r
    c.delete(ALL)
    x = rn(100,700)
    y = rn(100,700)
    r = rn(20,100)
    c.create_oval(x-r,y-r,x+r,y+r,fill=choice(colors))
    root.after(1000, ball_create)

def click(event):
    if (event.x*event.x+event.y*event.y<=(x-r)*(x-r)+(y-r)*(y-r)) or (event.x*event.x+event.y*event.y<=(x-r)*(x-r)+(y-r)*(y-r)):
    print('Popal')

ball_create()
c.bind('<Button-1>', click)
mainloop()
