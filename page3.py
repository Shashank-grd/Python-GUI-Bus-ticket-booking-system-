from tkinter import *
import pymysql
from tkinter.messagebox import *

def home(e=0):
    root.destroy()
    import page2 

row_number = 5
price=None
bus_choose=None

def conn():
    con = pymysql.connect(host="localhost", database="python_busbooking", user="root", password="2236", port=3306)
    return con
   

def show_ticket(a):
    def home1():
       root1.destroy()
       import page2 
    root1 = Tk()
    root1.title("PYTHON PROJECT")
    root1.geometry("800x800")
    def ticket():
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
    img_label = Label(root1, image=img)
    img_label.pack(side=TOP,anchor="n",padx=34) 
    Label(root1, text="ONLINE BUS BOOKING SYSTEM",font=("comicsansms",15,"bold"), relief='ridge',bg='yellow').pack(pady=20)
    Label(root1, text="BUS TICKET ",font=("comicsansms",15,"bold"), relief='ridge',bg='darkorange1',fg='white').pack(pady=20)
    f1 = Frame(root1,border=5,bg="gray87",relief="ridge")
    f1.pack()
    homeimg = PhotoImage(file="C:\\Users\\SHASHANK\\Documents\\Visual studio\\.vscode\\python\\Project\\2.png")
    Button(root1, image=homeimg, relief='ridge',command=home1).pack(pady=10)
    ticket()


    root1.mainloop()


def set_selected_values(selected_price, bus_id):
    global price,bus_choose
    price=selected_price
    bus_choose = bus_id
    print(price)
    print(bus_id)

def show(bus):
    row_number = 5
    v1 = IntVar()
    v = 1
    for i in bus:
        try: 
            con = conn()
            cursor = con.cursor()
            args = i
            query1 = "SELECT a.name, b.capacity, b.bus_type, b.fare_rs FROM bus_operator a INNER JOIN busdetail b ON a.bus_id = b.bus_id WHERE b.bus_id = %s"
            cursor.execute(query1, args)
            results = cursor.fetchall()
            if results:
                for bus_detail in results:
                    print("Bus Details:", bus_detail)
                    r = Radiobutton(f1, variable=v1, value=v)
                    r.grid(row=row_number, column=1)
                    Label(f1, text=bus_detail[0], font=30, fg="blue").grid(row=row_number, column=2)
                    Label(f1, text=bus_detail[2], font=30, fg="blue").grid(row=row_number, column=3)
                    Label(f1, text=bus_detail[1], font=30, fg="blue").grid(row=row_number, column=4)
                    Label(f1, text=bus_detail[3], font=30, fg="blue").grid(row=row_number, column=5)
                    row_number += 1
                    v += 1  
                    r.config(command=lambda price=bus_detail[3], bus_id=i: set_selected_values(price, bus_id))

            con.commit()
            con.close()

        except Exception as err:
            print("Exception:", err)

def proceed():
      def booking_detail():
              a1=vare1.get()
              a2=vare2.get()
              a3=vare3.get()
              a4=vare4.get()
              a5=vare5.get()
              
              if a1=="" or a2=="" or a3=="" or a4=="" or a5=="" :
                  showerror("error","Kuch likh le bhai:")

              else:
                  con = conn()
                  cursor = con.cursor()
                  ar=(a3,bus_choose)
                  que="UPDATE busdetail SET capacity = capacity - %s WHERE bus_id = %s"
                  cursor.execute(que, ar)
                  args = (bus_choose, a1, a2, a3, a4, a5,price*int(a3),var2.get(),var3.get())
                  query1 = "INSERT INTO bus_booking(bus_id, passenger_name, gender, no_of_seats, mobile_no, age,amount,boarding_station,boarding_date, booking_date) VALUES(%s, %s, %s, %s, %s, %s,%s,%s,%s,CURDATE())"
                  cursor.execute(query1, args)
                  con.commit()
                  con.close()
                  message = f"Total amount to be paid: RS {price*int(a3)}"
                  showinfo("Fare Confirm",message)
                  root.destroy()
                  show_ticket(a4)

      Label(f2, text="FILL PASSENGER DETAILS TO BOOK TICKET",font=("comicsansms",15,"bold"), relief='ridge',bg='light sky blue',fg='red').grid(row=0,column=4,columnspan=3,pady=15)
      
      Label(f2,text='Name',font=15).grid(row=3,column=1,padx=10)
      vare1=Entry(f2)
      vare1.grid(row=3,column=2,padx=10,pady=10)

      Label(f2,text='Gender',font=15).grid(row=3,column=3,)
      vare2=StringVar()
      vare2.set("Select")
      option=["Male","Female","Third"]
      OptionMenu(f2,vare2,*option).grid(row=3,column=4,padx=10)

      Label(f2,text='No. of Seats',font=15).grid(row=3,column=5)
      vare3=Entry(f2)
      vare3.grid(row=3,column=6,padx=10,pady=10)

      Label(f2,text='Mobile No',font=15).grid(row=3,column=7)
      vare4=Entry(f2)
      vare4.grid(row=3,column=8,padx=10,pady=10)

      Label(f2,text='Age',font=15).grid(row=3,column=9)
      vare5=Entry(f2)
      vare5.grid(row=3,column=10,padx=10,pady=10)

      Button(f2,text="Book Seat",command=booking_detail,relief='ridge', bg='red',font="bold").grid(row=4,column=5,padx=10,pady=10)

root = Tk()
root.title("PYTHON PROJECT")

def showbus():
   if var1.get()=="" or var2.get()=="" or var3.get()=="":
        showerror("error","Kuch likh le bhai:")
   Label(f1,text='Select Bus',font=30).grid(row=4,column=1,pady=20)
   Label(f1,text='Operator',font=30).grid(row=4,column=2,pady=20)
   Label(f1,text='Bus Type',font=30).grid(row=4,column=3,pady=20)
   Label(f1,text='Available',font=30).grid(row=4,column=4,pady=20)
   Label(f1,text='Fare',font=30).grid(row=4,column=5,pady=20)  
   find()
f1 = Frame(root)
f1.pack()

f2 = Frame(root)
f2.pack()

img = PhotoImage(file="C:\\Users\\SHASHANK\\Documents\\Visual studio\\.vscode\\python\\Project\\starbus.png")
img_label = Label(f1, image=img)
img_label.grid(row=0,column=3,columnspan=3) 

Label(f1, text="ONLINE BUS BOOKING SYSTEM",font=("comicsansms",15,"bold"), relief='ridge',bg='yellow').grid(row=1,column=3,columnspan=3,pady=15)
Label(f1, text="Enter Journey Details",font=("comicsansms",15,"bold"), relief='ridge',bg='sea green').grid(row=2,column=3,columnspan=3,pady=15)

Label(f1,text='To',font=30).grid(row=3,column=1,)
var1=Entry(f1,font=11)
var1.grid(row=3,column=2,padx=10,pady=10)

Label(f1,text='From',font=30).grid(row=3,column=3)
var2=Entry(f1,font=11)
var2.grid(row=3,column=4,padx=10,pady=10)

Label(f1,text='Journey Date(Y-M-D)',font=30).grid(row=3,column=5)
var3=Entry(f1,font=11)
var3.grid(row=3,column=6,padx=10,pady=10)

Button(f1,text="Show Bus",command=showbus,relief='ridge', bg='red',font="bold").grid(row=3,column=7,padx=10,pady=10)
homeimg = PhotoImage(file="C:\\Users\\SHASHANK\\Documents\\Visual studio\\.vscode\\python\\Project\\2.png")
Button(f1, image=homeimg, relief='ridge',command=home).grid(row=3, column=8, padx=10, pady=10)

def find():
  try:
    con = conn()
    cursor = con.cursor()
    args = (var2.get(), var1.get())
    query = "SELECT bus_id FROM bus_route WHERE station_name = %s AND destination_name = %s"
    cursor.execute(query, args)
    result = cursor.fetchall()
     
    bus = []
    if result:
      for row in result:
        bus_id = row[0]
        bus.append(bus_id)  
        print("Bus ID:", bus_id)
    print(bus)  
    show(bus)
    Button(f1,text="Proceed to Book",command=proceed,relief='ridge', bg='red',font="bold").grid(row=row_number,column=7,padx=10,pady=10)

    con.commit()
    con.close()

  except Exception as err:
    print("Exception:", err)


root.mainloop()

