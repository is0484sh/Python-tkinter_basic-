from tkinter import * 

root = Tk()
root.title("Yongmin's GUI")
root.geometry("640x480+500+300") # 가로 * 세로 + 좌표

# root.resizable(False,False) # x(너비),  y(너비) 조정 금지

btn1 = Button(root, text="Button1")
btn1.pack()

btn2 = Button(root,padx=5,pady=10,text="Button2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="Button3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="button4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="button5")
btn5.pack()

photo = PhotoImage(file="gui_basic/check_img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("Button clicked")

btn7 = Button(root, text="Button working",command = btncmd)
btn7.pack()

root.mainloop()