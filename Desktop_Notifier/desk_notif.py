from tkinter import *
from plyer import notification
from tkinter import messagebox
import time

t = Tk()
t.title("DESKTOP NOTIFIER")
t.iconbitmap(r'C:\Users\brian\Desktop\CCR\FULLSTACK_DEVELOPMENT\BACKEND\PYTHON\Projects\Desktop_Notifier\alert_icon.ico')
t.geometry('400x400')

def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set", "Set notification")
        t.destroy()
        time.sleep(min_to_sec)
        notification.notify(title=get_title,
                            message=get_msg,
                            app_name = "notifier",
                            app_icon = r"C:\Users\brian\Desktop\CCR\FULLSTACK_DEVELOPMENT\BACKEND\PYTHON\Projects\Desktop_Notifier\alert_icon.ico",
                            timeout= 5)

# Label - Title
t_label = Label(t, text="Title to Notify",font=("poppins", 10))
t_label.place(x=12, y=70)

# ENTRY - Title
title = Entry(t, width="40",font=("poppins", 10))
title.place(x=140, y=70)

# Label - Message
m_label = Label(t, text="Display Message", font=("poppins", 10))
m_label.place(x=12, y=120)

# ENTRY - Message
msg = Entry(t, width="40", font=("poppins", 10))
msg.place(x=140,height=30, y=120)

# Label - Time
time_label = Label(t, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y=175)

# ENTRY - Time
time1 = Entry(t, width="5", font=("poppins", 10))
time1.place(x=140, y=175)

# Label - min
time_min_label = Label(t, text="min", font=("poppins", 10))
time_min_label.place(x=205, y=180)

# Button
but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",
             command=get_details)
but.place(x=170, y=230)

t.mainloop()