"""
Author: Bianca Magyar
Date: 9/4/2020
Version 1.0
Description: Gallery programmed in Python to display series of photos.
References: Codemy
"""

from tkinter import *
from PIL import ImageTk, Image


#create forward function for forward button
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    #display image
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])

    #adjust buttons
    button_forward = Button(root, text=">>", padx=30, command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", padx=30, command=lambda: back(image_number-1))
    
    if image_number == len(image_list):
        button_forward = Button(root, text=">>", padx=30, state=DISABLED)

    #grid for buttons
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    #update status bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

#create back function for back button
def back(image_number):
    global my_label
    global button_forward
    global button_back

    #display image
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])

    #adjust buttons
    button_forward = Button(root, text=">>", padx=30, command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", padx=30, command=lambda: back(image_number-1))
    
    if image_number == 1:
        button_back = Button(root, text="<<", padx=30, state=DISABLED)

    #grid for buttons
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    #update status bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


if __name__ == "__main__":
    root = Tk()
    root.title("Gallery")
    root.iconbitmap("C:/Users/Bianca/Documents/Eclipse/Workspace/Tkinter/images/gallery-icon.ico")

    #open and store images for gallery
    my_img1 = ImageTk.PhotoImage(Image.open("flower1.jpg"))
    my_img2 = ImageTk.PhotoImage(Image.open("flower2.jpg"))
    my_img3 = ImageTk.PhotoImage(Image.open("flower3.jpg"))
    my_img4 = ImageTk.PhotoImage(Image.open("flower4.jpg"))
    my_img5 = ImageTk.PhotoImage(Image.open("flower5.jpg"))
    my_img6 = ImageTk.PhotoImage(Image.open("flower6.jpg"))
    my_img7 = ImageTk.PhotoImage(Image.open("flower7.jpg"))
    my_img8 = ImageTk.PhotoImage(Image.open("flower8.jpg"))
    my_img9 = ImageTk.PhotoImage(Image.open("flower9.jpg"))

    #store images in list
    image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9] 
    
    status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

    #display image
    my_label = Label(image=my_img1)
    my_label.grid(row=0, column=0, columnspan=3)

    #set up buttons
    button_back = Button(root, text="<<", padx=30, command=back, state=DISABLED)
    button_exit = Button(root, text="Exit Program", padx=30, command=root.destroy)
    button_forward = Button(root, text=">>", padx=30, command=lambda: forward(2))

    #grid for buttons
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2, pady=10)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
    root.mainloop()
