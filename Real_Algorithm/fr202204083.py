from tkinter import *
import random

count = 0
colors = ['red', 'orange', 'green', 'blue', 'indigo', 'violet']

def drawCircle(x,y,r):
    print(x,y,r)
    global count
    count += 1
    #반원으로 변경
    canvas.create_arc(x-r, y-r, x+r, y+r, start=0,extent=180,outline = random.choice(colors))
    # canvas.create_text(x, y-r, text=str(count), fill='black')
    if r >= 5:
        #반원의 시작점과 끝점으로 새로운 반원을 그림
        drawCircle(x-r,y+r//2,r//2)
        drawCircle(x+r,y+r//2,r//2)
    
window = Tk()
wSize = 1000
radius = 200
canvas = Canvas(window, width=wSize, height=wSize, bg='white')
drawCircle(wSize//2,wSize//2,radius)

canvas.pack()
window.mainloop()