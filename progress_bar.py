import time
import tkinter.ttk as ttk
from tkinter import * 


root = Tk()
root.title("Yongmin's GUI")
root.geometry("600x400")

# # progressbar = ttk.Progressbar(root, maximum=100, mode = "indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode = "determinate")
# progressbar.start(10) # 10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()
    
# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01 초 대기

        p_var2.set(i) # progress bar의 값 설정
        progressbar2.update() # 업데이트
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()