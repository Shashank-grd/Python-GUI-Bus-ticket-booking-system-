from tkinter import *
import pymysql
from tkinter.messagebox import *

root = Tk()
root.title("PYTHON PROJECT")

def home():
    root.destroy()
    import page2

f1 = Frame(root)
f1.pack()

def conn():
        con = pymysql.connect(host="localhost", database="python_busbooking", user="root", password="2236", port=3306)
        return con

def insertdata():
       v1=var1.get()
       v2=var2.get()
       v3=var3.get()
    
       if v1=="" or v2=="" or v3=="" :
            showerror("error","pehele select to kr le")  
       else:
            try:
                con = conn()
                cursor = con.cursor()
                args=(v1,v2,v3)
                query= "insert into runningdetail value(%s,%s,%s)"
                cursor.execute(query,args)
                con.commit()
                showinfo("Good","Shabaash")
                
                display_entered_data = f"{v1},{v2},{v3}"
                Label(f1, text=display_entered_data,font=20).grid(row=5, column=3, columnspan=5, pady=10)
                con.close()

            except Exception as err:
                 print("exception :",err)

def delete_data():
       v1=var1.get()
       v2=var2.get()
       v3=var3.get()
       

       if v1=="" or v2=="" or v3=="":
            showerror("error","Kuch likh le bhai:")  
       else:
            try:
                con = conn()
                cursor = con.cursor()
                args=(v1)
                query= "delete from runningdetail where bus_id=%s"
                cursor.execute(query,args)
                con.commit()
                showinfo("Good","Shabaash")
                
                display_entered_data = f"{v1},{v2},{v3}"
                Label(f1, text=display_entered_data,font=20).grid(row=5, column=3, columnspan=5, pady=10)
                con.close()

            except Exception as err:
                 print("exception :",err)

img = PhotoImage(file="C:\\Users\\SHASHANK\\Documents\\Visual studio\\.vscode\\python\\Project\\starbus.png")
img_label = Label(f1, image=img)
img_label.grid(row=0,column=3,columnspan=3) 

Label(f1, text="ONLINE BUS BOOKING SYSTEM",font=("comicsansms",15,"bold"), relief='ridge',bg='yellow').grid(row=1,column=3,columnspan=3,pady=15)
Label(f1, text="Enter Journey Details",font=("comicsansms",15,"bold"), relief='ridge',bg='sea green').grid(row=2,column=3,columnspan=3,pady=15)

Label(f1,text='Bus Id',font=30).grid(row=3,column=1,)
var1=Entry(f1,font=11)
var1.grid(row=3,column=2,padx=10,pady=10)

Label(f1,text='Running Date',font=30).grid(row=3,column=3)
var2=Entry(f1,font=11)
var2.grid(row=3,column=4,padx=10,pady=10)

Label(f1,text='Seat Available',font=30).grid(row=3,column=5)
var3=Entry(f1,font=11)
var3.grid(row=3,column=6,padx=10,pady=10)

Button(f1,text="Add",command=insertdata,relief='ridge', bg='red',font="bold").grid(row=3,column=7,padx=10,pady=10)
Button(f1,text="Delete",command=delete_data,relief='ridge', bg='red',font="bold").grid(row=3,column=8,padx=10,pady=10)
homeimg = PhotoImage(file="C:\\Users\\SHASHANK\\Documents\\Visual studio\\.vscode\\python\\Project\\2.png")
Button(f1, image=homeimg, relief='ridge',command=home).grid(row=3, column=9, padx=10, pady=10)

root.mainloop()
