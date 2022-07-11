from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap(r'C:\Users\brian\Desktop\CCR\FULLSTACK DEVELOPMENT\FRONTEND\FAVICONS\school.ico')

image_1 = ImageTk.PhotoImage(Image.open(r"C:\Users\brian\Desktop\CCR\FULLSTACK DEVELOPMENT\FRONTEND\IMAGES\dreaming_child.jpg"))
image_2 = ImageTk.PhotoImage(Image.open(r"C:\Users\brian\Desktop\CCR\FULLSTACK DEVELOPMENT\FRONTEND\IMAGES\kids_in_school.jpg"))
image_3 = ImageTk.PhotoImage(Image.open(r"C:\Users\brian\Desktop\CCR\FULLSTACK DEVELOPMENT\FRONTEND\IMAGES\knapsack.jpg"))
image_4 = ImageTk.PhotoImage(Image.open(r"C:\Users\brian\Desktop\CCR\FULLSTACK DEVELOPMENT\FRONTEND\IMAGES\teacher.jpg"))
image_5 = ImageTk.PhotoImage(Image.open(r"C:\Users\brian\Desktop\CCR\FULLSTACK DEVELOPMENT\FRONTEND\IMAGES\unsplash.jpg"))

image_list = [image_1, image_2, image_3, image_4, image_5]

my_label = Label(image=image_1)

back_button = Button(root, text = "<<")
exit_button = Button(root, text="Exit", command=root.quit)
next_button = Button(root,text=">>")

my_label.grid(row=0, column=0, columnspan=3)
back_button.grid(row=1,column=0)
exit_button.grid(row=1,column=1)
next_button.grid(row=1,column=2)

root.mainloop()