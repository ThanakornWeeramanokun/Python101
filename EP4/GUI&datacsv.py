from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
import os

figma_token = os.environ.get('figma_token')

################# CSV ###################
import csv

def writecsv(datalist):
    with open('C:\Python\Python311\Python101\EP4\data.csv', 'a', encoding='utf-8', newline='') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(datalist) # datalist = ['pen', 'pencil', 'eraser']

def readcsv():
    with open('C:\Python\Python311\Python101\EP4\data.csv', encoding='utf-8', newline='') as file:
        fr = csv.reader(file) # fr = file reader
        data = list(fr)
    return data

data = readcsv()
print(data)
#########################################

GUI = Tk() #หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('900x400') #ขนาดหน้าจอแสดงผลของโปรแกรม

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

######### Section Right ###########
LF1 = ttk.LabelFrame(GUI,text='กรอกข้อมูลที่ต้องการ')
LF1.place(x=400,y=50)

v_data = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน GUI
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(pady=10,padx=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() # ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) # บันทึกข้อมูลลง csv
    v_data.set('') # เคลียร์ข้อมูลที่อยู่ในช่องกรอก

B4 = ttk.Button(LF1,text='บันทึก', command=SaveData)
B4.pack(ipadx=20,ipady=20)


GUI.mainloop()