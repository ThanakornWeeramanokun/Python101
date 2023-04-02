import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from datetime import datetime

# ตรวจสอบความสมบูรณ์ของข้อมูลที่กรอก
def validate_input():
    if (title_entry.get() == '') or (description_entry.get() == '') or (user_entry.get() == '') or \
            (department_var.get() == 'Select') or (location_var.get() == 'Select') or (phone_entry.get() == ''):
        messagebox.showerror(title='Error', message='กรุณากรอกข้อมูลให้ครบทุกช่อง!')
        return False
    else:
        return True

def save_data():
    # ตรวจสอบความสมบูรณ์ของข้อมูลที่กรอก
    is_valid = validate_input()
    if not is_valid:
        return
    
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

    # แสดงข้อความเมื่อบันทึกข้อมูลสำเร็จ
    messagebox.showinfo(title='Success', message='บันทึกข้อมูลลงในระบบเรียบร้อยแล้ว!')

    # ล้างค่า Entry widgets
    title_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    department_var.set('Select')
    location_var.set('Select')
    phone_entry.delete(0, tk.END)

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
app.geometry('800x800') #ขนาดหน้าจอแสดงผลของโปรแกรม

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

# สร้างช่องเลือกแผนก
department_label = tk.Label(app, text='Department:')
department_var = tk.StringVar()
department_dropdown = ttk.Combobox(app, textvariable=department_var, values=['Select', 'IT', 'HR', 'Finance'])
department_dropdown.current(0)
department_label.pack()
department_dropdown.pack()

# สร้างช่องเลือกสถานที่
location_label = tk.Label(app, text='Location:')
location_var = tk.StringVar()
location_dropdown = ttk.Combobox(app, textvariable=location_var, values=['Select', 'Bangkok', 'Chonburi', 'Samut Prakran', 'Samut Sakhon', 'Pathum Thani', 'Nonthaburi'])
location_dropdown.current(0)
location_label.pack()
location_dropdown.pack()

# สร้างช่องกรอกเบอร์โทรศัพท์
phone_label = tk.Label(app, text='Phone:')
phone_var = tk.StringVar()
phone_entry = tk.Entry(app, textvariable=phone_var, validate='key', validatecommand=(app.register(validate_phone_number), '%S'))
phone_label.pack()
phone_entry.pack()

# สร้างปุ่มบันทึกข้อมูล
save_button = tk.Button(app, text='Save', command=save_data)
save_button.pack()

app.mainloop()