from tkinter import *
import sqlite3


root = Tk()
root.title("Address Book With SQLITE")
root.iconbitmap(r'C:\Users\brian\Desktop\CCR\FULLSTACK_DEVELOPMENT\BACKEND\PYTHON\Projects\Address_book\assets\address_64.ico')
root.geometry("500x500")

#Databases
conn = sqlite3.connect("address_book.db")
c = conn.cursor()

#Addresses Table
# c.execute("""CREATE TABLE addresses(
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
# )
# """)

#submit function
def submit():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    #Insert Into Table
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city':city.get(),
                'state':state.get(),
                'zipcode':zipcode.get()
            })

    conn.commit()
    conn.close()
    #Clear the text Boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

#query function
def query():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    #Query the database
    c. execute("SELECT oid, * FROM addresses")
    records = c.fetchall()

    #Loop through records
    print_records = ''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + '\n' 

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()
    conn.close()

#Delete function
def delete():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    
    #Delete a record
    c.execute("DELETE FROM addresses WHERE rowid= " + select_box.get())
    select_box.delete(0,END)

    conn.commit()
    conn.close()

def save():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    record_id = select_box.get()
    c.execute("""UPDATE addresses SET
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode

            WHERE rowid = :rowid""",
            {
                'first':f_name_update.get(),
                'last':l_name_update.get(),
                'address': address_update.get(),
                'city':city_update.get(),
                'state':state_update.get(),
                'zipcode':zipcode_update.get(),
                'rowid':record_id
            })

    conn.commit()
    conn.close()
    
    #Clear the Boxes
    f_name_update.delete(0,END)
    l_name_update.delete(0,END)
    address_update.delete(0,END)
    city_update.delete(0,END)
    state_update.delete(0,END)
    zipcode_update.delete(0,END)

    update.destroy()


    

def edit():
    global update
    update = Tk()
    update.title("Update A Record")
    update.iconbitmap(r'C:\Users\brian\Desktop\CCR\FULLSTACK DEVELOPMENT\FRONTEND\FAVICONS\address_64.ico')
    update.geometry("400x400")
    
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    #Create global variables for entry boxes
    global f_name_update
    global l_name_update
    global address_update
    global city_update
    global state_update
    global zipcode_update

    #Entry Boxes
    f_name_update = Entry(update, width=30)
    f_name_update.grid(row=0, column=1, padx=20, pady=(10,0))
    l_name_update = Entry(update, width=30)
    l_name_update.grid(row=1, column=1)
    address_update = Entry(update, width=30)
    address_update.grid(row=2, column=1)
    city_update = Entry(update, width=30)
    city_update.grid(row=3, column=1)
    state_update = Entry(update, width=30)
    state_update.grid(row=4, column=1)
    zipcode_update = Entry(update, width=30)
    zipcode_update.grid(row=5, column=1)

    #Entry Box Labels
    f_name_label = Label(update, text="First Name")
    f_name_label.grid(row=0, column=0,pady=(10,0))
    l_name_label = Label(update, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(update, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(update, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(update, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(update, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    #Update Button
    update_btn= Button(update, text="Save New Record", command=save)
    update_btn.grid(row=11,column=0, columnspan=2,padx=10, pady=10, ipadx=136)

    record_id = select_box.get()
    c.execute("SELECT * FROM addresses WHERE rowid = " + record_id)
    records = c.fetchall()
    for record in records:
        f_name_update.insert(0, record[0])
        l_name_update.insert(0, record[1])
        address_update.insert(0, record[2])
        city_update.insert(0, record[3])
        state_update.insert(0, record[4])
        zipcode_update.insert(0, record[5])
    conn.commit()
    conn.close()


#Entry Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
select_box = Entry(root,width=30)
select_box.grid(row=9,column=1)

#Entry Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0,pady=(10,0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
select_box_label = Label(root,text="Select ID")
select_box_label.grid(row=9, column=0)

#Submit Button
submit_btn= Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6,column=0, columnspan=2,padx=10, pady=10, ipadx=100)

#Query Button
query_btn= Button(root, text="Show Records", command=query)
query_btn.grid(row=7,column=0, columnspan=2,padx=10, pady=10, ipadx=137)

#Delete Button
delete_btn= Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10,column=0, columnspan=2,padx=10, pady=10, ipadx=136)

#Update Button
update_btn= Button(root, text="Edit Record", command=edit)
update_btn.grid(row=11,column=0, columnspan=2,padx=10, pady=10, ipadx=144)


conn.commit()
conn.close()
root.mainloop()