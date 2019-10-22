from  tkinter import *
from random import randrange as rn, choice
import time
import math

root = Tk()

c = Canvas(root, bg='#00ffff',width=800, height=800)
c.pack()

colors = ['black']#,'red','grey','lightgreen','green','cyan','yellow','orange','brown','red','blue','pink']
global x,y,r
ball = dict(x = int(rn(100,700)), y = int(rn(100,700)), r = int(rn(20,100)), vx = int(rn(-15,15)), vy = int(rn(-15,15)), ay = rn(-6,6))


print(ball['x'],' ',ball['y'])

def ball_create():
    global b
    b = c.create_oval(ball['x']-ball['r'],ball['y']-ball['r'],ball['x']+ball['r'],ball['y']+ball['r'],fill=choice(colors))

def click(event):
   # if (abs(event.x-x)<=r)and(abs(event.y-y)<=r):
        print('Popal')
        #ball_create()
        move_ball()

def move_ball():
    c.delete(ALL)
    ball['x'] += ball['vx']*0.2
    ball['y'] += ball['vy']*0.2 + ball['ay']*0.8
    #print(ball['x'],'    ',ball['y'],'    ',ball['r'])
    if ((ball['x'] <= ball['r'] and ball['vx']<0) or (ball['x'] >= 800-ball['r'] and ball['vx']>0)):
        ball['vx'] = (-1)*ball['vx']
        ball['x'] += ball['vx']*0.2
        ball['y'] += ball['vy']*0.2 + ball['ay']*0.8
        #print(ball['x'],'  .  ',ball['y'])
    if ((ball['y'] <= ball['r'] and ball['vy']<0) or  (ball['y'] >= 800-ball['r'] and ball['vy']>0)):
        ball['vy'] = (-1)*ball['vy']
        ball['x'] += ball['vx']*0.2
        ball['y'] += ball['vy']*0.2 + ball['ay']*0.8
        #print(ball['x'],'  _  ',ball['y'])


    #b.move(int(ball['x']),int(ball['y']))
    ball_create()
    root.after(1,move_ball)
    #print(ball['x'],' ',ball['y'])



ball_create()
c.bind('<Button-1>', click)
mainloop()
