from tkinter import *

def home():
    root.destroy()
    import page2 

def bus_operator():
    root.destroy()
    import addbusoperatordetailsp2

def new_bus():
    root.destroy()
    import busdetail

def new_route():
    root.destroy()
    import busroutedetail

def new_run():
    root.destroy()
    import runningdetail

root = Tk()
root.title("PYTHON PROJECT")
root.geometry("900x600")


img = PhotoImage(file="C:\\Users\\SHASHANK\\Documents\\Visual studio\\.vscode\\python\\Project\\starbus.png")
img_label = Label(root, image=img)
img_label.pack(side=TOP,anchor="n",padx=34) 
Label(root, text="ONLINE BUS BOOKING SYSTEM",font=("comicsansms",15,"bold"), relief='ridge',bg='yellow').pack(pady=20)
Label(root, text="ADD NEW DETAILS TO THE DATABASE ",font=("comicsansms",15,"bold"), relief='ridge',bg='darkorange1',fg='white').pack(pady=20)
f1 = Frame(root)
f1.pack(pady=30)
Button(f1, text="New Operator",relief='ridge', bg='red',font="bold",command=bus_operator).pack(side=LEFT,padx=34)
Button(f1, text="New Bus",relief='ridge', bg='blue',font="bold",command=new_bus).pack(side=LEFT,padx=34)
Button(f1, text="New Route",relief='ridge', bg='pink',font="bold",command=new_route).pack(side=LEFT,padx=34)
Button(f1, text="New Run",relief='ridge', bg='dodgerblue3',font="bold",command=new_run).pack(side=LEFT,padx=34)
homeimg = PhotoImage(file="C:\\Users\\SHASHANK\\Documents\\Visual studio\\.vscode\\python\\Project\\2.png")
Button(f1, image=homeimg, relief='ridge',command=home).pack(side=LEFT,padx=34)
root.mainloop()
