from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("DESKTOP NOTIFIER")
root.iconbitmap(r'C:\Users\brian\Desktop\CCR\FULLSTACK_DEVELOPMENT\BACKEND\PYTHON\Projects\Desktop_Notifier\alert_icon.ico')
root.geometry('400x400')

#ENTRY BOXES
title_to_notify = Entry(root,width=35).grid(row=0,column=1)
message = Entry(root,width=35).grid(row=1, column=1)
time = Entry(root,width=10).grid(row=2,column=1)

#ENTRY BOXES LABELS
title_to_notify_label = Label(root,text="title to notify")
title_to_notify_label.grid(row=0,column=0,pady=10)
message_label = Label(root,text="message")
message_label.grid(row=1,column=0)
time_label = Label(root,text="time")
time_label.grid(row=2,column=0)

root.mainloop()