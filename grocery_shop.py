from tkinter import *
from tkinter import messagebox
import tkinter as tk
from datetime import datetime
krish=Tk()

w=1000
h=500
sw=krish.winfo_screenwidth()
sh=krish.winfo_screenheight()

x=(sw/2)-(w/2)
y=(sh/2)-(h/2)
krish.geometry("%dx%d+%d+%d"   % (w,h,x,y))
krish.title("Grocer Billing System")




customer=Frame(krish)
customer.grid(row=0,column=0)
rate=Frame(krish)
rate.grid(row=1,column=0,sticky="nw",padx=10)

lafrm=tk.LabelFrame(customer,text="Customer detail")
lafrm.grid(row=1,column=0,padx=10)

laname=Label(lafrm,text="name",font=("times",10,"bold"))
laname.grid(row=1,column=0)
ename=Entry(lafrm,font=("times",10,"bold"))
ename.grid(row=1,column=1)
laphon=Label(lafrm,text="Phone",font=("times",10,"bold"))
laphon.grid(row=1,column=2)
ephone=Entry(lafrm,font=("times",10,"bold"))
ephone.grid(row=1,column=3)
labill=Label(lafrm,text="Bill No",font=("times",10,"bold"))
labill.grid(row=1,column=4)
ebill=Entry(lafrm,font=("times",10,"bold"))
ebill.grid(row=1,column=5,pady=30)

itementery=tk.LabelFrame(rate,text="Items(Entery Quality)")
itementery.grid(row=2,column=0,pady=20)
erice=Entry(itementery,font=("times",10,"bold"))
erice.grid(row=0,column=1)

larice=Label(itementery,text="Rice(₹50/kg)",font=("times",10,"bold"))
larice.grid(row=0,column=0)

erice=Entry(itementery,font=("times",10,"bold"))
erice.grid(row=0,column=1)



laoil=Label(itementery,text="Oil(₹100/kg)",font=("times",10,"bold"))
laoil.grid(row=1,column=0)
eoil=Entry(itementery,font=("times",10,"bold"))
eoil.grid(row=1,column=1,pady=10,padx=30)

lasugar=Label(itementery,text="Sugar(₹40/kg)",font=("times",10,"bold"))
lasugar.grid(row=2,column=0,pady=10)
esugar=Entry(itementery,font=("times",10,"bold"))
esugar.grid(row=2,column=1,pady=10,padx=30)
latea=Label(itementery,text="Tea(₹80/kg)",font=("times",10,"bold"))
latea.grid(row=3,column=0,pady=10,padx=30)
etea=Entry(itementery,font=("times",10,"bold"))
etea.grid(row=3,column=1,pady=10,padx=30)
lst=Frame(krish)
lst.grid(row=1,column=2)

rice=50
oil=100
sugar=40
tea=80
def add():
    lstbox.insert(END,f"Name  {ename.get()}",f"Phone  {ephone.get()}",f"bill{ebill.get()}")
    lstbox.insert(END,f"Rice:,{int(erice.get())*rice}")
    lstbox.insert(END,f"oil:{int(eoil.get())*oil}")
    lstbox.insert(END,f"sugar:{int(esugar.get())*sugar}")
    lstbox.insert(END,f"Tea:{int(etea.get())*tea}")
def total():
    lstbox.insert(END,f"total:{int(erice.get())*rice + int(eoil.get())*oil + int(esugar.get())*sugar + int(etea.get())*tea}")
        
 
 

lstbox=Listbox(lst,width=60,height=20)
lstbox.grid(row=0,column=0)

btngenratebill=Button(krish,text="Generate Bill",font=("times",10,"bold"),command=add)
btngenratebill.grid(row=2,column=0,sticky="nw",padx=30)

btngenratebill=Button(krish,text="Clear",font=("times",10,"bold"))
btngenratebill.grid(row=2,column=0,sticky="nw",padx=150)

btngenratebill=Button(krish,text="Exit",font=("times",10,"bold"))
btngenratebill.grid(row=2,column=0,sticky="nw",padx=200)

btntotal=Button(krish,text="Total",font=("times",10,"bold"),command=total)
btntotal.grid(row=2,column=0,sticky="nw",padx=300)

today=datetime.now().strftime("%d-%m-%y")
now=datetime.now()
time=now.strftime("%I:%M: %S %p")
msg="-----Wellcome to our shop--------"
lswidth=lstbox.cget("width")
msgbox=len(msg)
space=(lswidth-msgbox)//2
center_msg="   "*space+msg
lstbox.insert(END,center_msg,f"today({today})",f"Time{time}")
krish.mainloop()
