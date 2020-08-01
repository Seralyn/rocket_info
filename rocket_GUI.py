# import sys
# import os
import datetime
from tkinter import *
import tkinter.messagebox
from rocket_dictionary import rocketDictionary

root = Tk()
root.configure()
root.geometry("1350x800")
root.title("Working Title: SRP")

# *** Adds Icon to window ***
# works in windows, but not on Mac...why?
root.iconbitmap("rocket_icon 512.ico")


# *** Class for Button Push ***

def pushDataToLabelTitle(data):
    return data["Name"]  


def pushDataToLabel(data):
    return "\n" + "\n" + "Country: " + data["Country"] + "\n" + "Agency/Company: " + "\n" + data[
        "Agency"] + "\n" + "\n" + "Payload Capacity to LEO: " + data["Payload Capacity to LEO"] + "\n" + "Height: " \
           + data["Height"] + "\n" + "Diameter: " + data["Diameter"] + "\n" + "Mass: " + data["Mass"] + "\n" \
           + "Years in Operation: " + data["Years in Operation"] + "\n" + "\n" + "Additional Information: " + data[
               "Additional Information"]


# labelCreate = Label (mainWindowCenterFrame, text="poop", font="-weight bold")  **to create bold text**

# *** Button Functionality/Functions Definitions ***
def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    entry_text = w.get(index)
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary[entry_text]))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary[entry_text]))
    img = PhotoImage(file=rocketDictionary[entry_text]["Image"])
    imgLabel.configure(image=img)
    imgLabel.image = img


def doNothing():
    print("Nothing happened, of course.")


def helpMenuVersionPushed():
    tkinter.messagebox.showinfo("Version", "0.1 Alpha")


# def helpAboutPopUp():
#   aboutPopUp = Toplevel(height=600, width=800)

def helpMenuAboutPushed():
    tkinter.messagebox.showinfo("About",
                                '''
    Developer: Seralyn Campbell

    Email: seralyncampbell@gmail.com

    Written in: Python 3.8.5

    Open Source Software: 
    https://github.com/Seralyn/rocket_info
                                ''')


def update_time():
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label['text'] = currentTime
    root.after(1, update_time)


def quit():
    root.quit()




# *** Create all Frames/Containers ***
toolbarFrame = Frame(root, bg="gray40", width=1200, height=20)
mainWindowFrame = Frame(root, bg="gray63", width=1200, height=650)
mainWindowLeftFrame = Frame(mainWindowFrame, bg="gray63", width=400, height=650, padx=10)
mainWindowCenterFrame = Frame(mainWindowFrame, bg="gray63", width=600, height=650)
mainWindowRightFrame = Frame(mainWindowFrame, bg="gray63", width=400, height=650)
statusBarFrame = Frame(root, bg="gray76", width=1350, height=20)

# layout parameters of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# *** Layout of all Frames/Containers ***
toolbarFrame.grid(row=0, sticky="ew")
mainWindowFrame.grid(row=1, sticky="nsew")
mainWindowLeftFrame.grid(row=0, column=0)
mainWindowCenterFrame.grid(row=0, column=1)
mainWindowCenterFrame.grid_propagate(FALSE)
mainWindowRightFrame.grid(row=0, column=2)

# *** Image definitions ***


#*** Create Listbox ***
lb = Listbox(mainWindowLeftFrame, name='lb', height=40)

# *** Populate List Box ***
lb.insert(0, "Saturn V")
lb.insert(1, "Soyuz")
lb.insert(2, "Delta III")
lb.insert(3, "Ariane 62")
lb.insert(4, "Tronador II")
lb.insert(5, "VLS-1")
lb.insert(6, "VLM")
lb.insert(7, "Feng Bao 1")
lb.insert(8, "Kaituozhe-1")
lb.insert(9, "Kuaizhou")
lb.insert(10, "Long March 1")
lb.insert(11, "Long March 1D")
lb.insert(12, "Falcon 9")
lb.insert(13, "Falcon Heavy")
lb.insert(14, "Atlas V")
lb.insert(15, "SLS")
lb.insert(16, "New Glenn")
lb.insert(17, "H-IIA")
lb.insert(18, "Diamant")
lb.insert(19, "OTRAG")
lb.insert(20, "L-4S")
lb.insert(21, "M-4S")


# *** Place List Box ***
lb.bind('<<ListboxSelect>>', onselect)
lb.grid(row=1, column=0)


# *** Create all buttons/Labels ***
insertButton = Button(toolbarFrame, text="Insert Image", command=doNothing)
printButton = Button(toolbarFrame, text="Print", command=doNothing)

rocketListLabel = Label(mainWindowLeftFrame, bg="gray63", text="Rockets:", font="-weight bold")

rocketName = Label(mainWindowCenterFrame, font="-weight bold", bg="gray63", fg="white")
rocketName.config(font=("Arial", 20))
infoLabel = Label(mainWindowCenterFrame, bg="gray63", fg="white")
infoLabel.config(font=("Arial", 11))

imgLabel = Label(mainWindowRightFrame, bg="gray63", border=0, padx=20)  # padx does nothing...why?

label = Label(statusBarFrame, text="placeholder")
label.grid(row=0, column=0)

# *** Placement & Layout of all Buttons ***
insertButton.grid(row=0, column=0, padx=3, pady=4, sticky=W)
printButton.grid(row=0, column=1, padx=3, pady=4, sticky=W)

rocketListLabel.grid(row=0, column=0, padx=60, pady=5, sticky=N)

rocketName.grid(row=0, column=0)
infoLabel.grid(row=1, column=0, padx=25)

imgLabel.grid(row=0, column=0, sticky=E)

statusBarFrame.grid(row=2)
statusBarFrame.grid_propagate(FALSE)

# *** Popup Menus ***
'''
pop_up_answer = tkinter.messagebox.askquestion("Important Question:", "Do you want to learn more about rockets?")
if pop_up_answer == "yes":
    tkinter.messagebox.showinfo("Message", "I'm so happy to hear that!")
elif pop_up_answer == "no":
    tkinter.messagebox.showinfo("Message", "I see that you would love to learn more about rockets. That's wonderful.")
'''
# ***The Main Menu ***
menu = Menu(root)
root.config(menu=menu)

showMenu = Menu(menu, bd=0, tearoff=FALSE)
menu.add_cascade(label="Show", menu=showMenu)
showMenu.add_command(label="Individual Rockets", command=doNothing)
showMenu.add_command(label="Rocket Families", command=doNothing)

sortMenu = Menu(menu, bd=0, tearoff=FALSE)
menu.add_cascade(label="Sort", menu=sortMenu)
sortMenu.add_command(label="Alphabetical", command=doNothing)
sortMenu.add_command(label="Agency/Company", command=doNothing)
sortMenu.add_command(label="Country", command=doNothing)
sortMenu.add_command(label="Lifting Class", command=doNothing)
sortMenu.add_command(label="Operational Status", command=doNothing)
sortMenu.add_command(label="Payload Capacity to LEO", command=quit)
sortMenu.add_command(label="Mass", command=quit)
sortMenu.add_command(label="Diameter", command=quit)
sortMenu.add_command(label="Height", command=quit)

editMenu = Menu(menu, tearoff=FALSE)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=doNothing)
editMenu.add_command(label="Redo", command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Preferences...", command=doNothing)

helpMenu = Menu(menu, tearoff=FALSE)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=helpMenuAboutPushed)
helpMenu.add_command(label="Version", command=helpMenuVersionPushed)
helpMenu.add_command(label="List of Acronyms", command=doNothing)

# sticky EW seems to do nothing here. How can I stretch the status bar out to the size of the whole frame?

# *** Add Image ***
# satvphoto = PhotoImage(file="SaturnV.png")
# satvlabel = Label(root, image=satvphoto)
# satvlabel.grid(anchor=E)   #find out why this can't anchor to the right of the sorting options


'''If you want to handle jpg as well as png, import Image and ImageTk from PIL then do:
image = Image.open("Image Name")
photo = ImageTk.PhotoImage(image)'''

update_time()
root.mainloop()
