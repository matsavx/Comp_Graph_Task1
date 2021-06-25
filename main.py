from tkinter import *
import time
import math

root = Tk()
width = 400
height = 400
radius = 100
canvas = Canvas(root, width=width, height=height)
canvas.pack()
canvas.create_oval(width / 2 - radius, height / 2 - radius, width / 2 + radius, height / 2 + radius,
                   fill="white")

while 1:
    time_now = time.localtime()  # получаем текущее время в виде
    time_sec = int(time.strftime("%S", time_now))  # получаем секунды из переменной time_now
    sec_angle = 6 * time_sec  # угол отклонения секундной стрелки за 1 секунду

    line_min = canvas.create_line(width / 2, width / 2, width / 2, width / 2 + radius)

    line_sec = canvas.create_line(200,
                                  200,
                                  200 - 90 * math.cos(sec_angle * math.pi / 180 + math.pi / 2),
                                  200 - 90 * math.sin(sec_angle * math.pi / 180 + math.pi / 2),
                                  width=2, fill='red')

    root.update()
    canvas.delete(line_sec)