from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Address Book With SQLITE")
root.iconbitmap(r'C:\Users\brian\Desktop\CCR\FULLSTACK DEVELOPMENT\FRONTEND\FAVICONS\address_64.ico')
root.geometry("400x400")

#Databases
conn = sqlite3.connect("address_book.db")
c = conn.cursor()

#Create Table
c.execute("""CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
)
""")

conn.commit()
conn.close()
root.mainloop()