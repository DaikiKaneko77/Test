import os
import json
import zipfile
import tkinter as tk

with zipfile.ZipFile("kabeposter.zip", "r") as zip_ref:  #zipファイルの展開
    zip_ref.extractall()
def load_frame(frame_num):
    filename = f"kabeposter/kabeposter_{frame_num:012d}_keypoints.json" #jsonファイルを読み込む
    with open(filename) as f:  
        data = json.load(f)
    return data
# 骨格の接続関係
skeleton = [
    (0, 1),  
    (1, 2), (2, 3), (3, 4),  
    (1, 5), (5, 6), (6, 7),  #姿勢の接続関係を示す
    (1, 8),  
    (8, 9), (9, 10), (10, 11),  
    (8, 12), (12, 13), (13, 14),  
]
# tkinterウィンドウの初期化
root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=1000)  # Adjust canvas size if necessary
canvas.pack()
def draw_frame(frame_num): #アニメーションのフレームを壁画
    canvas.delete("all")  
    data = load_frame(frame_num)
    # 各人の骨格を取得して描画
    for i, person_data in enumerate(data["people"]):
        keypoints = person_data["pose_keypoints_2d"]
        keypoints = [(keypoints[i], keypoints[i+1]) for i in range(0, len(keypoints), 3)]  # リストを座標のペアに変換
        # 人物ごとに色を変える
        color = "red" if i == 0 else "blue"
        # 骨格を描画
        for (i, j) in skeleton:
            if keypoints[i] != (0, 0) and keypoints[j] != (0, 0):  
                canvas.create_line(keypoints[i][0], keypoints[i][1], keypoints[j][0], keypoints[j][1], fill=color)
    if frame_num < 99:  
        root.after(100, draw_frame, frame_num + 1)  
draw_frame(0)  # Start the animation
root.mainloop()