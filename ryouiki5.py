import tkinter as tk

def move_figure():  #図形を水平方向に移動するための関数の定義
    
    dx = 5 #水平方向に移動する量(移動速度の調整)

    # 図形を移動させる
    canvas.move(head, dx, 0)
    canvas.move(body, dx, 0)
    canvas.move(left_leg, dx, 0)
    canvas.move(right_leg, dx, 0)
    canvas.move(left_arm, dx, 0)
    canvas.move(right_arm, dx, 0)

    # 50ミリ秒後に再び移動させる
    canvas.after(50, move_figure)

root = tk.Tk()
root.geometry('700x700')

canvas = tk.Canvas(root, width=700, height=700)
canvas.pack()

# Draw the person figure
head = canvas.create_oval(300, 100, 400, 200, fill='white', width=3)
body = canvas.create_line(350, 200, 350, 300, fill='black', width=3)
left_leg = canvas.create_line(350, 300, 250, 400, fill='black', width=3)
right_leg = canvas.create_line(350, 300, 450, 400, fill='black', width=3)
left_arm = canvas.create_line(350, 240, 280, 200, fill='black', width=3)
right_arm = canvas.create_line(350, 240, 420, 200, fill='black', width=3)

# アニメーションを開始する
move_figure()

root.mainloop()
