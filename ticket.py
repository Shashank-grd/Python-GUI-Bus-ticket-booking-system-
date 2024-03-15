from tkinter import *
import pymysql
from tkinter.messagebox import *

root = Tk()
root.title("PYTHON PROJECT")
root.geometry("800x600")

def conn():
    con = pymysql.connect(host="localhost", database="python_busbooking", user="root", password="2236", port=3306)
    return con

def show_ticket(a):
  try:
    con = conn()
    cursor = con.cursor()
    arg=a
    query = "SELECT * FROM bus_booking where mobile_no=%s"
    cursor.execute(query,arg)
    results = cursor.fetchall()
    for i in results:
         Label(f1, text="Booking id :", font=30, fg="blue",bg="gray87").grid(row=0, column=1,padx=20)
         Label(f1, text=i[0], font=30, fg="blue",bg="gray87").grid(row=0, column=2)
         Label(f1, text="Name :", font=30, fg="blue",bg="gray87").grid(row=1, column=1,padx=20)
         Label(f1, text=i[2], font=30, fg="blue",bg="gray87").grid(row=1, column=2)
         Label(f1, text="Gender :", font=30, fg="blue",bg="gray87").grid(row=2, column=1,padx=20)
         Label(f1, text=i[3], font=30, fg="blue",bg="gray87").grid(row=2, column=2)
         Label(f1, text="No of Seats :", font=30, fg="blue",bg="gray87").grid(row=3, column=1,padx=20)
         Label(f1, text=i[4], font=30, fg="blue",bg="gray87").grid(row=3, column=2)
         Label(f1, text="Mobile No :", font=30, fg="blue",bg="gray87").grid(row=4, column=1,padx=20)
         Label(f1, text=i[5], font=30, fg="blue",bg="gray87").grid(row=4, column=2)
         Label(f1, text="Age :", font=30, fg="blue",bg="gray87").grid(row=5, column=1,padx=20)
         Label(f1, text=i[6], font=30, fg="blue",bg="gray87").grid(row=5, column=2)
         Label(f1, text="Amount :", font=30, fg="blue",bg="gray87").grid(row=0, column=3,padx=20)
         Label(f1, text=i[7], font=30, fg="blue",bg="gray87").grid(row=0, column=4)
         Label(f1, text="Bus Id :", font=30, fg="blue",bg="gray87").grid(row=1, column=3,padx=20)
         Label(f1, text=i[1], font=30, fg="blue",bg="gray87").grid(row=1, column=4)
         Label(f1, text="Boarding Station :", font=30, fg="blue",bg="gray87").grid(row=2, column=3,padx=20)
         Label(f1, text=i[8], font=30, fg="blue",bg="gray87").grid(row=2, column=4)
         Label(f1, text="Boarding Date :", font=30, fg="blue",bg="gray87").grid(row=3, column=3,padx=20)
         Label(f1, text=i[9], font=30, fg="blue",bg="gray87").grid(row=3, column=4)
         Label(f1, text="Booking Date :", font=30, fg="blue",bg="gray87").grid(row=4, column=3,padx=20)
         Label(f1, text=i[10], font=30, fg="blue",bg="gray87").grid(row=4, column=4)
         
    con.close()
  except Exception as e:
    showerror("Error", f"An error occurred: {e}")

img = PhotoImage(file="C:\\Users\\SHASHANK\\Documents\\Visual studio\\.vscode\\python\\Project\\starbus.png")
img_label = Label(root, image=img)
img_label.pack(side=TOP,anchor="n",padx=34) 
Label(root, text="ONLINE BUS BOOKING SYSTEM",font=("comicsansms",15,"bold"), relief='ridge',bg='yellow').pack(pady=20)
Label(root, text="BUS TICKET ",font=("comicsansms",15,"bold"), relief='ridge',bg='darkorange1',fg='white').pack(pady=20)
f1 = Frame(root,border=5,bg="gray87",relief="ridge")
f1.pack()

root.mainloop()