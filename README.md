python
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import sqlite3
```
- These lines import the necessary modules for creating a GUI application using Tkinter and SQLite for database operations.

```python
window=Tk()
window.title("TECH")
window.geometry('500x450')
window.iconbitmap(r'hotel.ico')
window.config(bg='#B3E8E5')
```
- Here, a Tkinter window is created with a title "TECH", specific dimensions, an icon, and a background color.

```python
Var=StringVar()
Var1=StringVar()
```
- Two StringVar variables are created. These are Tkinter variables used to link the values of Tkinter widgets (like Entry, Radiobutton, etc.) to Python variables.

```python
def database():
    # Retrieving user input data
    name=name_entry.get()
    age=age_entry.get()
    address=address_entry.get()
    phone=phone_entry.get()
    email=email_entry.get()
    proof=proof_option.get()
    gender=Var.get()
    payment=Var1.get()
    
    # Connecting to SQLite database
    conn=sqlite3.connect('data.db')
    with conn:
        # Creating a table if it doesn't exist
        conn.execute('CREATE TABLE IF NOT EXISTS mini(name text,age int(2),gender,address varchar,phone int(10),email varchar,proof,payment)')
        # Inserting data into the table
        conn.execute("INSERT INTO mini (name,age,gender,address,phone,email,proof,payment)VALUES(?,?,?,?,?,?,?,?)",(name,age,gender,address,phone,email,proof,payment))
        conn.commit()
        # Showing message boxes based on conditions
        if(name=="" or phone=="" or age=="" and address==""):
            messagebox.showerror('error',"please enter your details")
        else:
            messagebox.showinfo('thank you','your room has been booked\nsuccesfully')
```
- This function `database()` is triggered when the user clicks the "Book a room" button. It retrieves the user input data from various entry fields and dropdown menus. Then, it connects to the SQLite database (or creates one if it doesn't exist), creates a table if it doesn't exist, inserts the data into the table, and commits the changes. It also displays appropriate message boxes based on certain conditions.

```python
# GUI elements (labels, entry fields, radio buttons, etc.) are created and placed in the window using grid layout.
```

```python
def show():
    # Function to display booking details from the database
    conn=sqlite3.connect('data.db')
    r=conn.execute('select * from mini')
    for row in r:
        # Printing booking details to the console
        print('name=',row[0])
        print('age=',row[1])
        print('gender=',row[2])
        print('address=',row[3])
        print('phone=',row[4])
        print('email=',row[5])
        print('proof=',row[6])
        print('payment=',row[7])
```
- This function `show()` retrieves booking details from the SQLite database and prints them to the console. It's linked to the "Show Detail" option in the File menu.

```python
# Menubar setup with various options like new, update, delete, show detail, and exit.
```

```python
# Button to trigger the database function for booking a room.
```

```python
window.mainloop()
```
- Finally, this statement runs the Tkinter event loop, which listens for events (like button clicks, mouse movements, etc.) and responds accordingly. This loop keeps the GUI application running until the user closes the window.


![upload 1](https://github.com/sreeramsr/Tkinter--sqlite3-Tech-launch/assets/135236418/f1c88182-8b9a-46da-8255-7e29c5a4ca3e)
![upload 3](https://github.com/sreeramsr/Tkinter--sqlite3-Tech-launch/assets/135236418/90ccaa90-36c6-4ba7-bf7f-b68d4005c583)

