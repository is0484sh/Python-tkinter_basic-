import tkinter.ttk as ttk
from tkinter import * 


root = Tk()
root.title("Yongmin's GUI")
root.geometry("600x400")

values = [str(i) + "일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()