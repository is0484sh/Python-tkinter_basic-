from tkinter import * 

root = Tk()
root.title("Yongmin's GUI")
root.geometry("600x400")

listbox = Listbox(root, selectmode="extended", height=0) 
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(0)

    # print(listbox.size(),"in the list.")

    # 항목 확인
    # print("1번쨰부터 3번째까지의 항목: ",listbox.get(0,2))

    # 선택된 항목 확인 (위치로 반환 ex(0,1,2,3))
    print("선택된 항목 : ",listbox.curselection())
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()