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
       v4=var4.get()
       v5=var5.get()
       v6=var6.get()

       if v1=="" or v2=="" or v3=="" or v4=="" or v5=="" or v6=="":
            showerror("error","pehele select to kr le")  
       else:
            try:
                con = conn()
                cursor = con.cursor()
                args=(v1,v3,v5,v2,v4,v6)
                query= "insert into busdetail value(%s,%s,%s,%s,%s,%s)"
                cursor.execute(query,args)
                con.commit()
                showinfo("Good","Shabaash")
                
                display_entered_data = f"{v1},{v2},{v3},{v4},{v5},{v6}"
                Label(f1, text=display_entered_data,font=20).grid(row=5, column=5, columnspan=5, pady=10)
                con.close()

            except Exception as err:
                 print("exception :",err)

def update_data():
       v1=var1.get()
       v2=var2.get()
       v3=var3.get()
       v4=var4.get()
       v5=var5.get()
       v6=var6.get()

       if v1=="" or v2=="" or v3=="" or v4=="" or v5=="" or v6=="":
            showerror("error","Kuch likh le bhai:")  
       else:
            try:
                con = conn()
                cursor = con.cursor()
                args=(v1,v3,v2,v4,v6,v5)
                query= "update busdetail set bus_id=%s,capacity=%s,bus_type=%s,fare_rs=%s,route_id=%s where operator_id=%s"
                cursor.execute(query,args)
                con.commit()
                showinfo("Good","Shabaash")
                
                display_entered_data = f"{v1},{v2},{v3},{v4},{v5},{v6}"
                Label(f1, text=display_entered_data).grid(row=5, column=5, columnspan=5, pady=10)
                con.close()

            except Exception as err:
                 print("exception :",err)

img = PhotoImage(file="C:\\Users\\SHASHANK\\Documents\\Visual studio\\.vscode\\python\\Project\\starbus.png")
img_label = Label(f1, image=img)
img_label.grid(row=0,column=6,columnspan=3) 

Label(f1, text="ONLINE BUS BOOKING SYSTEM",font=("comicsansms",15,"bold"), relief='ridge',bg='yellow').grid(row=1,column=6,columnspan=3,pady=15)
Label(f1, text="Add Bus Operator details",font=("comicsansms",15,"bold"), relief='ridge',bg='sea green').grid(row=2,column=6,columnspan=3,pady=15)

Label(f1,text='Bus id',font=15).grid(row=3,column=1)
var1=Entry(f1)
var1.grid(row=3,column=2,padx=10,pady=10)

Label(f1,text='Bus Type',font=15).grid(row=3,column=3,)
var2=StringVar()
var2.set("Bus Type")
option=["AC 2x2","AC 3x2","Non AC 2x2","Non AC 3x2","AC Sleeper 2x1","Non AC Sleeper 2x1"]
OptionMenu(f1,var2,*option).grid(row=3,column=4)

Label(f1,text='Capacity',font=15).grid(row=3,column=5)
var3=Entry(f1)
var3.grid(row=3,column=6,padx=10,pady=10)

Label(f1,text='Fare Rs',font=15).grid(row=3,column=7)
var4=Entry(f1)
var4.grid(row=3,column=8,padx=10,pady=10)

Label(f1,text='Operator id',font=15).grid(row=3,column=9)
var5=Entry(f1)
var5.grid(row=3,column=10,padx=10,pady=10)

Label(f1,text='Route Id',font=15).grid(row=3,column=11)
var6=Entry(f1)
var6.grid(row=3,column=12,padx=10,pady=10)

Button(f1,text="Add",command=insertdata,relief='ridge', bg='red',font="bold").grid(row=4,column=6,padx=10,pady=10)
Button(f1,text="Edit",command=update_data,relief='ridge', bg='red',font="bold").grid(row=4,column=7,padx=10,pady=10)
homeimg = PhotoImage(file="C:\\Users\\SHASHANK\\Documents\\Visual studio\\.vscode\\python\\Project\\2.png")
Button(f1, image=homeimg, relief='ridge',command=home).grid(row=4, column=8, padx=10, pady=10)

root.mainloop()
