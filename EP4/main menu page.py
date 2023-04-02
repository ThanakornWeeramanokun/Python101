import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

# create main window
app = tk.Tk()
# set window size
app.geometry("400x400")
# set window title
app.title("Helpdesk app")

# create label for the main menu
label = tk.Label(app, text="Welcome to the Helpdesk app!", font=("Arial", 16))
label.pack(pady=20)

# create a button to go to the next page
def open_form_page():
    # app.destroy()  # close the current window

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
        
    form_page = tk.Tk() #หน้าจอหลักของโปรแกรม
    form_page.title('Helpdesk app') #ชื่อโปรแกรม
    form_page.geometry('400x400') #ขนาดหน้าจอแสดงผลของโปรแกรม

    # สร้าง fields แบบฟอร์ม
    # สร้างช่องกรอกเรื่องปัญหา
    title_label = tk.Label(form_page, text='Title:')
    title_entry = tk.Entry(form_page)
    title_label.pack()
    title_entry.pack()

    # สร้างช่องกรอกรายละเอียดปัญหา
    description_label = tk.Label(form_page, text='Description:')
    description_entry = tk.Entry(form_page)
    description_label.pack()
    description_entry.pack()

    # สร้างช่องกรอกชื่อผู้แจ้ง
    user_label = tk.Label(form_page, text='User name:')
    user_var = tk.StringVar()
    user_entry = tk.Entry(form_page, textvariable=user_var, validate='key', validatecommand=(form_page.register(validate_user), '%S'))
    user_label.pack()
    user_entry.pack()

    # สร้าง departments dropdown
    departments = ['Sales', 'Marketing', 'IT', 'Finance']
    department_label = tk.Label(form_page, text='Department:')
    department_var = tk.StringVar(value='Select')
    department_dropdown = tk.OptionMenu(form_page, department_var, *departments)
    department_dropdown.configure(text='Select department')
    department_label.pack()
    department_dropdown.pack()

    # สร้าง locations dropdown
    locations = ['Bangkok', 'Chonburi', 'Samut Prakran', 'Samut Sakhon', 'Pathum Thani', 'Nonthaburi']
    location_label = tk.Label(form_page, text='Location:')
    location_var = tk.StringVar(value='Select')
    location_dropdown = tk.OptionMenu(form_page, location_var, *locations)
    location_dropdown.configure(text='Select location')
    location_label.pack()
    location_dropdown.pack()

    # สร้างช่องกรอกหมายเลขโทรศัพท์
    phone_validation = (form_page.register(validate_phone_number), '%P')
    phone_label = tk.Label(form_page, text='Phone:')
    phone_entry = tk.Entry(form_page, validate='key', validatecommand=phone_validation)
    phone_label.pack()
    phone_entry.pack()

    # สร้างปุ่ม Save
    save_button = tk.Button(form_page, text='Save', command=save_data)
    save_button.pack()

    # create function to close form page
    def go_close():
        form_page.destroy()  # close the current window

    # create button to go back to main menu
    back_button = tk.Button(form_page, text='Close', command=go_close)
    back_button.pack()

button = tk.Button(app, text="New ticket", command=open_form_page)
button.pack(pady=20)

app.mainloop()