from tkinter import *

def fun():
    root.destroy()
    import page2

root = Tk()
root.title("PYTHON PROJECT")
root.geometry("800x500")

img = PhotoImage(file="C:\\Users\\SHASHANK\\Documents\\Visual studio\\.vscode\\python\\Project\\starbus.png")

img_label = Label(root, image=img)
img_label.grid(row=0, column=0, columnspan=2) 

Label(root, text="ONLINE BUS BOOKING SYSTEM",font=("comicsansms",15,"bold"),relief='ridge', bg='darkorange1').grid(row=1, column=0, columnspan=2)
Label(root, text="NAME : SHASHANK KUMAR SINHA", fg='blue').grid(row=2, column=0, columnspan=2)
Label(root, text="ENROLL : 221B345", fg='blue').grid(row=3, column=0, columnspan=2)
Label(root, text="MOBILE : 950XXXXXXX", fg='blue').grid(row=4, column=0, columnspan=2)
Label(root, text="SUBMITTED TO : DR. MAHESH KUMAR",font=("comicsansms",15,"bold"),relief='ridge', bg='darkorange1').grid(row=5, column=0, columnspan=2)
Label(root, text="For Admin Only", fg='red').grid(row=6, column=1, sticky="se")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(6, weight=1)

root.after(1000,fun)
root.mainloop()
