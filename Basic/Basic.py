import turtle
t = turtle.Turtle()

turtle.title("My Turtle Program") #ตั้งชื่อ Title
turtle.bgcolor('blue') #กำหนดสีพื้นหลัง
t.shapesize(1,10,1) #กำหนดขนาดของรูปทรงปากกา (กว้าง,ยาว,เส้นขอบ)
t.fillcolor("green") #กำหนดสีของรูปทรงปากกาด้านใน
t.pencolor("red") #กำหนดสีของปากกาที่ใช้วาด
t.pensize(2) #กำหนดขนาดของปากกา
t.speed(10) #กำหนดความเร็วในการวาด
t.begin_fill() #คำสั่งเริ่มต้นการสร้างรูปร่าง เพื่อบอกโปรแกรมว่ากำลังจะวาดรูปร่างปิด (สีตามที่กำหนดไว้ใน fillcolor)
t.rt(90) #หันขวา 90 องศา
t.fd(100) #วาดไปด้านหน้า 100 pixel
t.lt(90) #หันซ้าย 90 องศา
t.bk(100) #วาดกลับหลัง 100 pixel
t.goto(100,100) #วาดไปตำแหน่งแกน x, y ที่ 100, 100
t.circle(60) #วาดรูปวงกลม(ขนาดที่ต้องการ)
t.dot(20) #วาดจุดทึบ(ขนาดที่ต้องการ)
t.end_fill() #คำสั่งจบการสร้างรูปร่าง เพื่อให้ทราบว่าสามารถเติมสีได้ (สีตามที่กำหนดไว้ใน fillcolor)

# กำหนดรูปร่างของปากกา
# t.shape("turtle") #เต่า
# t.shape("arrow") #ลูกศร
# t.shape("circle") #วงกลม
# t.shape("Square") #สี่เหลี่ยม
# t.shape("Triangle") #สามเหลี่ยม
# t.shape("Classic") #ดั้งเดิม

# กำหนดคุณลักษณะของปากกา เช่น ปากกาสีม่วง, เติมสีส้ม, ขนาดปากกา 10, ความเร็ว 9
t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()

# การวาดแบบยกปากกาขึ้น เพื่อไปตำแหน่งที่ต้องการและวาดรูปต่อ
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.rt(90)
t.pendown()
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.pendown()

t.undo() #ยกเลิกคำสั่งล่าสุดที่เรียกใช้
t.clear() #เคลียร์รูปวาดทั้งหมดที่เคยเรียกใช้ แต่ตำแหน่งของปากกายังอยู่ที่เดิม
t.reset() #รีเซ็ตทั้งหมด กลับสู่จุดเริ่มต้น

#การทำสแตมป์ปากกา
t.stamp()
t.fd(100)
t.stamp()
t.fd(100)
t.clearstamp(8)

#การโคลนปากกา
c = t.clone()
t.color("magenta")
c.color("red")
t.circle(100)
c.circle(60)

#คำสั่ง for Loops
for i in range(4):
    t.fd(100)
    t.rt(90)

#คำสั่ง for while Loops
n=10
while n <= 40:
    t.circle(n)
    n = n+10

#คำสั่งเงื่อนไขเพื่อตรวจสอบว่าเงื่อนไขที่กำหนดเป็นจริงหรือไม่ หากเป็นเช่นนั้น คำสั่งที่เกี่ยวข้องจะถูกดำเนินการ
u = input("Would you like me to draw a shape? Type yes or no: ")
if u == "yes":
    t.circle(50)
elif u == "no":
    print("Okay")
else:
    print("Invalid Reply")

#คำสั่งเพื่อบอกโปรแกรมวาดเสร็จสิ้นทั้งหมดแล้ว และค้างหน้าต่างไว้    
turtle.done()