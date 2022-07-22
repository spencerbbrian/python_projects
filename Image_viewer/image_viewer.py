from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('SCHOOL IMAGES VIEWER')
root.iconbitmap(r'C:\Users\brian\Desktop\CCR\FULLSTACK DEVELOPMENT\FRONTEND\FAVICONS\school.ico')

image_1 = ImageTk.PhotoImage(Image.open(r"C:\Users\brian\Desktop\CCR\FULLSTACK DEVELOPMENT\FRONTEND\IMAGES\dreaming_child.jpg"))
image_2 = ImageTk.PhotoImage(Image.open(r"C:\Users\brian\Desktop\CCR\FULLSTACK DEVELOPMENT\FRONTEND\IMAGES\kids_in_school.jpg"))
image_3 = ImageTk.PhotoImage(Image.open(r"C:\Users\brian\Desktop\CCR\FULLSTACK DEVELOPMENT\FRONTEND\IMAGES\Knapsack.jpg"))
image_4 = ImageTk.PhotoImage(Image.open(r"C:\Users\brian\Desktop\CCR\FULLSTACK DEVELOPMENT\FRONTEND\IMAGES\teacher.jpg"))

image_list = [image_1, image_2, image_3, image_4]
#bd(border)
status = Label(root, text="Image 1 of " + str(len(image_list)),bd=1,relief=SUNKEN, anchor=E)

def next(image_number):
    global my_label
    global next_button
    global back_button
    #Used to get rid of something
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    next_button = Button(root,text=">>", command=lambda: next(image_number+1))
    back_button = Button(root, text="<<", command=lambda:  back(image_number-1))

    if image_number == 4:
        next_button = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1,column=0)
    next_button.grid(row=1,column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)),bd=1,relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
def back(image_number):
    global my_label
    global next_button
    global back_button
    #Used to get rid of something
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    next_button = Button(root,text=">>", command=lambda: next(image_number+1))
    back_button = Button(root, text="<<", command=lambda:  back(image_number-1))

    if image_number == 1:
        back_button = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1,column=0)
    next_button.grid(row=1,column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)),bd=1,relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

my_label = Label(image=image_1)

back_button = Button(root, text = "<<", command=back, state=DISABLED)
exit_button = Button(root, text="Exit", command=root.quit)
next_button = Button(root,text=">>", command=lambda: next(2))

my_label.grid(row=0, column=0, columnspan=3)
back_button.grid(row=1,column=0)
exit_button.grid(row=1,column=1)
next_button.grid(row=1,column=2,pady=10)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()