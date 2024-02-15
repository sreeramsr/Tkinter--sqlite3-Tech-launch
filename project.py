from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import sqlite3

window=Tk()
window.title("TECH")
window.geometry('500x450')
window.iconbitmap(r'hotel.ico')
window.config(bg='#B3E8E5')

Var=StringVar()
Var1=StringVar()


#connect function
def database():
    name=name_entry.get()
    age=age_entry.get()
    address=address_entry.get()
    phone=phone_entry.get()
    email=email_entry.get()
    proof=proof_option.get()
    gender=Var.get()
    payment=Var1.get()
    conn=sqlite3.connect('data.db')
    with conn:
        conn.execute('CREATE TABLE IF NOT EXISTS mini(name text,age int(2),gender,address varchar,phone int(10),email varchar,proof,payment)')
        conn.execute("INSERT INTO mini (name,age,gender,address,phone,email,proof,payment)VALUES(?,?,?,?,?,?,?,?)",(name,age,gender,address,phone,email,proof,payment))
        conn.commit()
        if(name=="" or phone=="" or age=="" and address==""):
            messagebox.showerror('error',"please enter your details")
        else:
            messagebox.showinfo('thank you','your room has been booked\nsuccesfully')




#grid
title=Label(window,text="TECH LAUNCH",font=('old stamper',25,'bold'),bg='#18978F',fg='#A0D995',borderwidth=14)
title.grid(row=1,column=2)

name=Label(window,text='name:',font=('times',15,'bold'),bg='#B3E8E5',fg='#055052')
name.grid(row=2,column=1)
name_entry=Entry(window,font=('times',12))
name_entry.grid(row=2,column=2)

age=Label(window,text='age:',font=('times',15,'bold'),bg='#B3E8E5',fg='#055052')
age.grid(row=3,column=1)
age_entry=Entry(window,font=('times',12))
age_entry.grid(row=3,column=2)

gender=Label(window,text='gender:',font=('times',15,'bold'),bg='#B3E8E5',fg='#055052')
gender.grid(row=4,column=1)
Radiobutton(window,text='male',variable=Var,value='male',bg='#B3E8E5',font=('times',14,'bold')).grid(row=4,column=2)
Radiobutton(window,text='female',variable=Var,value='female',bg='#B3E8E5',font=('times',14,'bold')).grid(row=4,column=3)

address=Label(window,text='address:',font=('times',15,'bold'),bg='#B3E8E5',fg='#055052')
address.grid(row=5,column=1)
address_entry=Entry(window,font=('times',12))
address_entry.grid(row=5,column=2)

phone=Label(window,text='phone.no:',font=('times',15,'bold'),bg='#B3E8E5',fg='#055052')
phone.grid(row=6,column=1)
phone_entry=Entry(window,font=('times',12))
phone_entry.grid(row=6,column=2)

email=Label(window,text='e-mail:',font=('times',15,'bold'),bg='#B3E8E5',fg='#055052')
email.grid(row=7,column=1)
email_entry=Entry(window,font=('times',12))
email_entry.grid(row=7,column=2)

proof=Label(window,text='proof:',font=('times',15,'bold'),bg='#B3E8E5',fg='#055052')
proof.grid(row=8,column=1)
        

proof_option=ttk.Combobox(window,width=20,state='readonly')
proof_option['values']=('aadhar','driving licence','passport','pan-card','others')
proof_option.current(4)
proof_option.bind('<<Comboboxselected>>',database)
proof_option.grid(row=8,column=2)

payment=Label(window,text='payment:',font=('times',15,'bold'),bg='#B3E8E5',fg='#055052')
payment.grid(row=9,column=1)

Radiobutton(window,text='1BHK @rs.500/day',variable=Var1,value='1BHK @rs.500/day',bg='#B3E8E5',font=('times',12,'bold')).grid(row=9,column=2)
Radiobutton(window,text='2BHK @rs.1000/day',variable=Var1,value='2BHK @rs.1000/day',bg='#B3E8E5',font=('times',12,'bold')).grid(row=10,column=2)
Radiobutton(window,text='3BHK @rs.1500/day',variable=Var1,value='3BHK @rs.1500/day',bg='#B3E8E5',font=('times',12,'bold')).grid(row=11,column=2)

#display
def show():
    conn=sqlite3.connect('data.db')
    r=conn.execute('select * from mini')
    for row in r:
        print('name=',row[0])
        print('age=',row[1])
        print('gender=',row[2])
        print('address=',row[3])
        print('phone=',row[4])
        print('email=',row[5])
        print('proof=',row[6])
        print('payment=',row[7])
    
#menubar
menubar=Menu(window)
file=Menu(menubar,tearoff=0)
file.add_command(label='new')
file.add_command(label='update')
file.add_command(label='delete')
file.add_separator()
file.add_command(label='show detail',command=show)
file.add_separator()
file.add_command(label='exit',command=window.quit)
menubar.add_cascade(label='file',menu=file)        
window.config(menu=menubar)       
    
#button
btn_1=Button(window,text='Book a room',command=database,font=('White Chocolate Mint',15,''),bg='#ff5d5d',fg='white',borderwidth=5)
btn_1.grid(row=13,column=2)

window.mainloop()

