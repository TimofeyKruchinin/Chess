import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, bg='white', width=400, height=400)
for i in range(50, 450, 50):
    canvas.create_line((0, i), (400, i), fill='black')
for a in range(0, 400, 50):
    canvas.create_line((a, 0), (a, 400), fill='black')
canvas.pack()
win.mainloop()