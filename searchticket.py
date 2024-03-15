from tkinter import *
import pymysql
from tkinter.messagebox import *

def conn():
    con = pymysql.connect(host="localhost", database="python_busbooking", user="root", password="2236", port=3306)
    return con

def home():
    root.destroy()
    import page2 

root = Tk()
root.title("PYTHON PROJECT")

def show():
  if var1.get()=="":
    showerror("Error", "Kuch likh le bhai:")
  else:
   try:
    con = conn()
    cursor = con.cursor()
    arg=var1.get()
    query = "SELECT * FROM bus_booking where mobile_no=%s"
    cursor.execute(query,arg)
    results = cursor.fetchall()
    if results:
      for i in results:
         Label(f2, text="Booking id :", font=30, fg="blue",bg="gray87").grid(row=0, column=1,padx=20)
         Label(f2, text=i[0], font=30, fg="blue",bg="gray87").grid(row=0, column=2)
         Label(f2, text="Name :", font=30, fg="blue",bg="gray87").grid(row=1, column=1,padx=20)
         Label(f2, text=i[2], font=30, fg="blue",bg="gray87").grid(row=1, column=2)
         Label(f2, text="Gender :", font=30, fg="blue",bg="gray87").grid(row=2, column=1,padx=20)
         Label(f2, text=i[3], font=30, fg="blue",bg="gray87").grid(row=2, column=2)
         Label(f2, text="No of Seats :", font=30, fg="blue",bg="gray87").grid(row=3, column=1,padx=20)
         Label(f2, text=i[4], font=30, fg="blue",bg="gray87").grid(row=3, column=2)
         Label(f2, text="Mobile No :", font=30, fg="blue",bg="gray87").grid(row=4, column=1,padx=20)
         Label(f2, text=i[5], font=30, fg="blue",bg="gray87").grid(row=4, column=2)
         Label(f2, text="Age :", font=30, fg="blue",bg="gray87").grid(row=5, column=1,padx=20)
         Label(f2, text=i[6], font=30, fg="blue",bg="gray87").grid(row=5, column=2)
         Label(f2, text="Amount :", font=30, fg="blue",bg="gray87").grid(row=0, column=3,padx=20)
         Label(f2, text=i[7], font=30, fg="blue",bg="gray87").grid(row=0, column=4)
         Label(f2, text="Bus Id :", font=30, fg="blue",bg="gray87").grid(row=1, column=3,padx=20)
         Label(f2, text=i[1], font=30, fg="blue",bg="gray87").grid(row=1, column=4)
         Label(f2, text="Boarding Station :", font=30, fg="blue",bg="gray87").grid(row=2, column=3,padx=20)
         Label(f2, text=i[8], font=30, fg="blue",bg="gray87").grid(row=2, column=4)
         Label(f2, text="Boarding Date :", font=30, fg="blue",bg="gray87").grid(row=3, column=3,padx=20)
         Label(f2, text=i[9], font=30, fg="blue",bg="gray87").grid(row=3, column=4)
         Label(f2, text="Booking Date :", font=30, fg="blue",bg="gray87").grid(row=4, column=3,padx=20)
         Label(f2, text=i[10], font=30, fg="blue",bg="gray87").grid(row=4, column=4)
    else: 
      showinfo("TICKET","NO TICKET FOUND GO TO TICKET BOOKING")
      root.destroy()
      import page3     
    con.close() 
   except Exception as e:
      showerror("Error", f"An error occurred: {e}")
   

img = PhotoImage(file="C:\\Users\\SHASHANK\\Documents\\Visual studio\\.vscode\\python\\Project\\starbus.png")
img_label = Label(root, image=img)
img_label.pack(side=TOP,anchor="n",padx=34) 
Label(root, text="ONLINE BUS BOOKING SYSTEM",font=("comicsansms",15,"bold"), relief='ridge',bg='darkorange1').pack(pady=20)
Label(root, text="Check Your Booking ",font=("comicsansms",15,"bold"), relief='ridge',bg='green4',fg="deep sky blue").pack(pady=20)
f1 = Frame(root)
f1.pack(pady=30)
f2 = Frame(root,border=5,bg="gray87",relief="ridge")
f2.pack(pady=30)
Label(f1, text="Enter Mobile NO. :",font="bold").pack(side=LEFT,padx=34)
var1=Entry(f1,font=10)
var1.pack(side=LEFT,padx=34)
Button(f1, text="Check Booking",command=show,relief='ridge', bg='pink',font="bold").pack(side=LEFT,padx=34)
homeimg = PhotoImage(file="C:\\Users\\SHASHANK\\Documents\\Visual studio\\.vscode\\python\\Project\\2.png")
Button(f1, image=homeimg, relief='ridge',command=home).pack(side=LEFT,padx=34)
root.mainloop()
