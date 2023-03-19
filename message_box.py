import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Yongmin's GUI")
root.geometry("640x480")

def info():
    msgbox.showinfo("알림","정상적으로 예매 완료되었습니다.")
def warn():
    msgbox.showinfo("경고","해당 좌석은 매진되었습니다.")
def error():
    msgbox.showerror("에러","오류가 발생했습니다.")
def okcancel():
    msgbox.askokcancel("확인 / 취소","해당 좌석은 유아동반석입니다. 예매하시겠습니까?")
def retrycancel():
    msgbox.askokcancel("재시도 / 취소" ,"일시적인 오류입니다. 다시 시도하시겠습니까?\
        ")
def yesno():
    msgbox.askokcancel("예/ 아니오","해당 좌석은 역방향입니다. 예매하시겠습니까?")
def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다. \n저장하시겠습니까?")
    if response == 1:
        print("Yes")
    elif response == 0:
        print("No")
    else:
        print("Cancel")



Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()