import tkinter as tk
import os
import random
import json
import tkinter
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle

# กำหนดขนาดรูปภาพ
IMAGE_SIZE = (450, 350)

# โหลดรายการเมนูอาหารจากไฟล์ JSON
with open('C:/Python/Python311/Python101/EP2/Homework/food_menu.json', 'r', encoding='utf-8') as f:
    food_menu = json.load(f)

# ฟังก์ชั่นสร้างรายการเมนูอาหารแบบสุ่ม
def generate_food():
    food_item = random.choice(list(food_menu.keys()))
    return food_item

# ฟังก์ชั่นแสดงรายการอาหารที่สร้างขึ้นแบบสุ่มและรูปภาพ
def display_food():
    global history_list # เพิ่มบรรทัดนี้
    food_item = generate_food()
    food_picture = os.path.join("C:/Python/Python311/Python101/EP2/Homework/images/Menu/", food_menu[food_item])

    # เปิดรูปภาพพร้อมปรับขนาดให้เท่ากันทุกรูป
    pil_image = Image.open(food_picture).resize(IMAGE_SIZE)
    food_photo = ImageTk.PhotoImage(pil_image)
    
    # อัพเดต label ด้วยเมนูอาหารและรูปภาพใหม่
    food_label.config(text=food_item)
    food_image.config(image=food_photo)
    food_image.image = food_photo

# สร้างหน้าต่างหลักและชื่อ Title
GUI = tk.Tk() #หน้าจอหลักของโปรแกรม
GUI.title("Random Food Menu") #ชื่อโปรแกรม
GUI.geometry('750x650') #ขนาดหน้าจอแสดงผลของโปรแกรม

# ตั้งค่า Theme
style = ThemedStyle(GUI)
style.set_theme("breeze")

# สร้างป้ายกำกับสำหรับชื่อโปรแกรม
title_label = tk.Label(GUI, text="สุ่มอาหารตามสั่ง", font=("Helvetica", 30), fg="white", bg="black", padx=10, pady=10)
# Set the label's position using the grid geometry manager
title_label.pack()

# สร้าง Label สำหรับรายการอาหาร
food_label = tk.Label(GUI, text="",font=('Helvetica',24))
food_label.pack(pady=(20, 0))

# สร้างรูปภาพสำหรับรายการอาหาร
food_image = tk.Label(GUI, image=None)
food_image.pack(pady=(20, 0))

# สร้างปุ่มเพื่อสุ่มรายการอาหารใหม่
generate_image = Image.open("C:/Python/Python311/Python101/EP2/Homework/images/start-button.png")
generate_image = generate_image.resize((140,60))
generate_photo = ImageTk.PhotoImage(generate_image)
generate_button = tk.Button(GUI, image=generate_photo, command=display_food)
generate_button.pack(pady=(20, 0))

# ตั้งค่าช่องว่างภายในสำหรับหน้าต่าง GUI
GUI.configure(padx=20, pady=20)

# เริ่มต้นทำงานแบบลูป เป็นการอนุญาตให้ GUI ตอบสนองต่อการโต้ตอบของผู้ใช้
GUI.mainloop()
