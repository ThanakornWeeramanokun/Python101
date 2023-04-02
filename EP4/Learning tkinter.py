import tkinter as tk


def print_something(text):
    print(text)

app = tk.Tk() #หน้าจอหลักของโปรแกรม
app.title('Learning tkinter') #ชื่อโปรแกรม
app.geometry('900x600') #ขนาดหน้าจอแสดงผลของโปรแกรม

button = tk.Button(text='click me!', command=lambda: print_something('print this'))
button.place(x=50, y=50)

pack_frame = tk.Frame(app)
pack_frame.pack()
tk.Label(pack_frame, text='Pack!', bg="blue").pack(side=tk.LEFT)
tk.Label(pack_frame, text='Pack!', bg="blue").pack(side=tk.LEFT)
tk.Label(pack_frame, text='Pack!', bg="blue").pack(side=tk.LEFT)

grid_frame = tk.Frame(app)
grid_frame.pack()
tk.Button(grid_frame,text='A', bg = "yellow").grid(row=0, column=0, sticky='NSEW')
tk.Button(grid_frame,text='B', bg = "yellow").grid(row=0, column=1, sticky='NSEW')
tk.Button(grid_frame,text='C', bg = "yellow").grid(row=0, column=2, sticky='NSEW')




app.mainloop()


