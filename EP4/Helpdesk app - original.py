import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

def save_data():
    # รับค่าจาก Entry widgets
    title = title_entry.get()
    description = description_entry.get()
    user = user_entry.get()
    department = department_var.get()
    location = location_var.get()
    phone = phone_entry.get()

    # รับวันที่และเวลาปัจจุบัน
    now = datetime.now()
    date = now.strftime('%d-%m-%Y')
    time = now.strftime('%H:%M:%S')

    # เขียนข้อมูลเป็นไฟล์ CSV
    with open('data.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, time, title, description, user, department, location, phone])

    # ล้างค่า Entry widgets
    title_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    department_dropdown.configure(text='Select department')
    location_dropdown.configure(text='Select location')
    phone_entry.delete(0, tk.END)

    # แสดงข้อความเมื่อบันทึกข้อมูลสำเร็จ
    messagebox.showinfo(title='Success', message='บันทึกข้อมูลลงในระบบเรียบร้อยแล้ว!')

# สร้างฟังก์ชันเพื่อแก้ไขข้อมูล
def edit_data(table):
    # ดึงข้อมูลจากตาราง
    selected_row = table.focus()
    if not selected_row:
        messagebox.showerror(title='Error Message')
        return

    # ดึงข้อมูลจากแถวที่เลือก
    data_row = table.item(selected_row)['values']

    # กำหนดค่าให้กับช่องกรอกข้อมูล
    title_entry.delete(0, tk.END)
    title_entry.insert(0, data_row[2])
    description_entry.delete(0, tk.END)
    description_entry.insert(0, data_row[3])
    user_entry.delete(0, tk.END)
    user_entry.insert(0, data_row[4])
    department_dropdown.configure(text=data_row[5])
    location_dropdown.configure(text=data_row[6])
    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, data_row[7])


def load_data():
    # อ่านข้อมูลจากไฟล์ CSV
    data = []
    with open('data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    # สร้างหน้าต่างใหม่เพื่อแสดงข้อมูล
    view_window = tk.Toplevel(app)
    view_window.title('View data')

    # สร้างตารางเพื่อแสดงข้อมูล
    table = tk.Frame(view_window)
    table.pack()

    # สร้างหัวตาราง
    headers = ['Date', 'Time', 'Title', 'Description', 'User', 'Department', 'Location', 'Phone']
    for i, header in enumerate(headers):
        label = tk.Label(table, text=header)
        label.grid(row=0, column=i, padx=5, pady=5)

    # แสดงข้อมูลในตาราง
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            label = tk.Label(table, text=item)
            label.grid(row=i+1, column=j, padx=5, pady=5)

    # สร้างปุ่มแก้ไขข้อมูล
    edit_button = tk.Button(view_window, text='Edit', command=lambda: edit_data(table))
    
    # เพิ่มปุ่ม edit_button ให้กับกรอบตาราง
    edit_button.grid(row=len(data)+1, column=0, pady=10)

    # Pack the table frame to show all widgets
    table.pack()

# ตรวจสอบ widgets ของ user_entry ที่ป้อนจะต้องมีเฉพาะตัวอักษรและช่องว่างเท่านั้น
def validate_user(text):
    if text.isalpha() or ' ' in text:
        return True
    else:
        return False

# ตรวจสอบ widgets ของ phone_entry ที่ป้อนจะต้องมีเฉพาะตัวเลขเท่านั้น
def validate_phone_number(input):
    if input.isdigit() or input == "":
        return True
    else:
        return False
    
app = tk.Tk() #หน้าจอหลักของโปรแกรม
app.title('Helpdesk app') #ชื่อโปรแกรม
app.geometry('1280x900') #ขนาดหน้าจอแสดงผลของโปรแกรม

# สร้าง fields แบบฟอร์ม
# สร้างช่องกรอกเรื่องปัญหา
title_label = tk.Label(app, text='Title:')
title_entry = tk.Entry(app)
title_label.pack()
title_entry.pack()

# สร้างช่องกรอกรายละเอียดปัญหา
description_label = tk.Label(app, text='Description:')
description_entry = tk.Entry(app)
description_label.pack()
description_entry.pack()

# สร้างช่องกรอกชื่อผู้แจ้ง
user_label = tk.Label(app, text='User name:')
user_var = tk.StringVar()
user_entry = tk.Entry(app, textvariable=user_var, validate='key', validatecommand=(app.register(validate_user), '%S'))
user_label.pack()
user_entry.pack()

# สร้าง departments dropdown
departments = ['Sales', 'Marketing', 'IT', 'Finance']
department_label = tk.Label(app, text='Department:')
department_var = tk.StringVar(value='Select')
department_dropdown = tk.OptionMenu(app, department_var, *departments)
department_dropdown.configure(text='Select department')
department_label.pack()
department_dropdown.pack()

# สร้าง locations dropdown
locations = ['Bangkok', 'Chonburi', 'Samut Prakran', 'Samut Sakhon', 'Pathum Thani', 'Nonthaburi']
location_label = tk.Label(app, text='Location:')
location_var = tk.StringVar(value='Select')
location_dropdown = tk.OptionMenu(app, location_var, *locations)
department_dropdown.configure(text='Select location')
location_label.pack()
location_dropdown.pack()

# สร้างช่องกรอกหมายเลขโทรศัพท์
phone_validation = (app.register(validate_phone_number), '%P')
phone_label = tk.Label(app, text='Phone:')
phone_entry = tk.Entry(app, validate='key', validatecommand=phone_validation)
phone_label.pack()
phone_entry.pack()

# สร้างปุ่ม Save
save_button = tk.Button(app, text='Save', command=save_data)
save_button.pack()

app.mainloop()