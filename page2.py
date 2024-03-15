from tkinter import *

def book_ticket(e=0):
    root.destroy()
    import page3 

def check_ticket(e=0):
    root.destroy()
    import searchticket

def book_detail(e=0):
    root.destroy()
    import addbusoperatordetails


root = Tk()
root.title("PYTHON PROJECT")
root.geometry("800x500")

img = PhotoImage(file="C:\\Users\\SHASHANK\\Documents\\Visual studio\\.vscode\\python\\Project\\starbus.png")
img_label = Label(root, image=img)
img_label.pack(side=TOP,anchor="n",padx=34) 
Label(root, text="ONLINE BUS BOOKING SYSTEM",font=("comicsansms",15,"bold"), relief='ridge',bg='darkorange1').pack(pady=20)
f1 = Frame(root, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f1.pack(pady=30)
Button(f1, text="Seat Booking",relief='ridge', bg='red',font="bold",command=book_ticket).pack(side=LEFT,padx=34)
Button(f1, text="Cheaked Booked Seat",relief='ridge', bg='blue',font="bold",command=check_ticket).pack(side=LEFT,padx=34)
Button(f1, text="Add Bus Detail",relief='ridge', bg='pink',font="bold",command=book_detail).pack(side=LEFT,padx=34)
Label(root, text="For Admin Only", fg='red',bg="black").pack(side=RIGHT,anchor="se")
root.mainloop()
