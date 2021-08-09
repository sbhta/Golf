from tkinter import *

root = Tk()
root.geometry("600x600")

c = Canvas(master=root, width=600, height=600)
c.pack()

class Ball():
    def __init__(self, x, y):
        self.ball_pos = {x, y}
        c.create_oval(x, y, x+20, y+20, fill="black")


ball = Ball(300,300)

while True:
    root.update()