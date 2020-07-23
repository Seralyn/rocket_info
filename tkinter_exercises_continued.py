from tkinter import *
import tkinter.messagebox
#from PIL import ImageTk,Image
#import sys
#import os
import datetime

root = Tk()
root.geometry("1200x800")
root.title("Seralyn's Rocket Program")

# *** Adds Icon to window ***
root.iconbitmap("rocket_icon 32.ico")

def doNothing():
    print("Nothing happened, of course.")

def quit():
    root.quit()


pop_up_answer = tkinter.messagebox.askquestion("Important Question:", "Do you want to learn more about rockets?")
if pop_up_answer == "yes":
    tkinter.messagebox.showinfo("Message", "I'm so happy to hear that!")
elif pop_up_answer == "no":
    tkinter.messagebox.showinfo("Message", "I see that you would love to learn more about rockets. That's wonderful.")

# ***The Main Menu ***

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu, tearoff=FALSE)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_command(label="Open...", command=doNothing)
subMenu.add_command(label="Save...", command=doNothing)
subMenu.add_command(label="Save As...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Settings...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit...", command=quit)

editMenu = Menu(menu, tearoff=FALSE)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=doNothing())
editMenu.add_command(label="Redo", command=doNothing())
editMenu.add_separator()
editMenu.add_command(label="Preferences...", command=doNothing)

# ***The Tool Bar ***

toolbar = Frame(root, bg="orange")

insertButton = Button(toolbar, text="Insert Image", command=doNothing)
insertButton.pack(side=LEFT, padx=3, pady=4)
printButton = Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=LEFT, padx=3, pady=4)

toolbar.pack(side=TOP, fill=X)

# *** Buttons to pull data on rockets ***

sortRocketsLabel = Label(root, text="Sort Rockets by:")
sortRocketsLabel.pack(anchor=W)
alphabeticalButton = Button(root, text="Alphabetical Order")
alphabeticalButton.pack(anchor=W)
agencyButton = Button(root, text="Agency/Company")
agencyButton.pack(anchor=W)
countryButton = Button(root, text="Country")
countryButton.pack(anchor=W)
classButton = Button(root, text="Class: Heavy, Medium, Light")
classButton.pack(anchor=W)
operationalButton = Button(root, text="Operational Status: Operational, Retired, Under Development, Concept Only")
operationalButton.pack(anchor=W)
payloadHLButton = Button(root, text="Payload Capacity to LEO: Highest to Lowest")
payloadHLButton.pack(anchor=W)
payloadLHButton = Button(root, text="Payload Capacity to LEO: Lowest to Highest")
payloadLHButton.pack(anchor=W)
massHLButton = Button(root, text="Mass: Highest to Lowest")
massHLButton.pack(anchor=W)
massLHButton = Button(root, text="Mass: Lowest to Highest")
massLHButton.pack(anchor=W)
diameterHLButton = Button(root, text="Diameter: Highest to Lowest")
diameterHLButton.pack(anchor=W)
massLHButton = Button(root, text="Diameter: Lowest to Highest")
massLHButton.pack(anchor=W)
heightHLButton = Button(root, text="Height: Highest to Lowest")
heightHLButton.pack(anchor=W)
heightLHButton = Button(root, text="Height: Lowest to Highest")
heightLHButton.pack(anchor=W)

# *** Add Image ***
satvphoto = PhotoImage(file="SaturnV.png")
satvlabel = Label(root, image=satvphoto)
satvlabel.pack(anchor=E)   #find out why this can't anchor to the right of the sorting options

# **To remind usage of .grid() system instead of .pack() system
#entry_1.grid(row=0, column=1)
#entry_2.grid(row=1, column=1)

'''If you want to handle jpg as well as png, import Image and ImageTk from PIL then do:
image = Image.open("Image Name")
photo = ImageTk.PhotoImage(image)'''

# *** The Status Bar [bottom] ***
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
status = Label(root, text=date, bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()
