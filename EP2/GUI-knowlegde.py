from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดหน้าจอแสดงผลของโปรแกรม

#Original button code
# B1 = Button(GUI,text='เงินมีอยู่กี่บาท')
# B1.pack()

# B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
# B1.pack(ipadx=20,ipady=20) #pack = center

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

####################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 0 บาท!!'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = LabelFrame(GUI, text='Money') #คล้ายกระดาน
FB1.place(x=100,y=80) #place = custom
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท', command=Button2)
B2.pack(ipadx=20,ipady=20,padx=30,pady=30)
####################

def Button3():
    text = 'Python 101, Math'
    messagebox.showinfo('วิขาที่เรียนในวันที่ 10-20 ก.พ.',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=250) #place = custom
B3 = ttk.Button(FB2,text='สัปดาห์นี้เรียนวิชาอะไร', command=Button3)
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()