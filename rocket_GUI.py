# import sys
# import os
import datetime
from tkinter import *
import tkinter.messagebox
from rocket_dictionary import rocketDictionary

root = Tk()
root.configure(bg="gray50")
root.geometry("1700x900")
root.title("Working Title: SRP")

# *** Adds Icon to window ***
# works in windows, but not on Mac...why?
root.iconbitmap("rocket_icon 512.ico")


# *** Dictionary Info Pull Functions ***

def pushDataToLabelTitle(data):
    return data["Name"]  


def pushDataToLabel(data):
    return "\n" + "\n" + "Country: " + data["Country"] + "\n" + "Agency/Company: " + "\n" + data[
        "Agency"] + "\n" + "\n" + "Payload Capacity to LEO: " + data["Payload Capacity to LEO"] + "\n" + "Height: " \
           + data["Height"] + "\n" + "Diameter: " + data["Diameter"] + "\n" + "Mass: " + data["Mass"] + "\n" \
           + "Years in Operation: " + data["Years in Operation"] + "\n" + "\n" + "Additional Information: " + data[
               "Additional Information"]


# *** Button Functionality/Functions Definitions ***
def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    entry_text = w.get(index)
    rocketName.configure(text=pushDataToLabelTitle(rocketDictionary[entry_text]))
    infoLabel.configure(text=pushDataToLabel(rocketDictionary[entry_text]))
    img = PhotoImage(file="images/" + rocketDictionary[entry_text]["Image"])
    imgLabel.configure(image=img)
    imgLabel.image = img


def doNothing():   #for now
    print("Nothing happened, of course.")


def helpMenuVersionPushed():
    tkinter.messagebox.showinfo("Version", "0.2 Alpha")


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


def on_configure(evt):  #commenting out "event" changes nothing
    info_canvas.configure(scrollregion=info_canvas.bbox('all'))  #doesn't seem to do anything...

def update_time():
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label['text'] = currentTime
    root.after(1, update_time)


def quit():
    root.quit()


# *** Create all Frames/Containers/Canvas ***
toolbarFrame = Frame(root, bg="gray40", width=1200, height=20)
mainWindowFrame = Frame(root, bg="gray63", width=1200, height=650)
mainWindowLeftFrame = Frame(mainWindowFrame, bg="gray63", width=400, height=650, padx=10)
mainWindowCenterFrame = Frame(mainWindowFrame, bg="gray63", width=730, height=750, pady=80)
mainWindowRightFrame = Frame(mainWindowFrame, bg="gray63", width=400, height=650)
statusBarFrame = Frame(root, bg="gray50", width=1650, height=20)
info_canvas = Canvas(mainWindowCenterFrame, bg="gray63", bd=0, highlightthickness=0, height=700)
frame_inside_canvas = Frame(info_canvas, width=700, height=2000, bg="gray63")

# *** Place Canvas ***
info_canvas.grid(row=0, column=0, sticky=NSEW)
info_canvas.create_window((0,0), window=frame_inside_canvas, anchor='center')  #commenting this out changes nothing

# Layout parameters of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

mainWindowLeftFrame.grid_rowconfigure(1, weight=1)
mainWindowLeftFrame.grid_columnconfigure(0, weight=1)

mainWindowCenterFrame.grid_rowconfigure(1, weight=1)
mainWindowCenterFrame.grid_columnconfigure(0, weight=1)

mainWindowRightFrame.grid_rowconfigure(1, weight=1)
mainWindowRightFrame.grid_columnconfigure(0, weight=1)


# *** Layout of all Frames/Containers ***
toolbarFrame.grid(row=0, sticky="ew")
mainWindowFrame.grid(row=1, sticky="nsew")
mainWindowLeftFrame.grid(row=0, column=0)
mainWindowCenterFrame.grid(row=0, column=1)
mainWindowCenterFrame.grid_propagate(FALSE)
mainWindowRightFrame.grid(row=0, column=2)
#frame_inside_canvas.grid_propagate(FALSE)

# *** Populate List Box ***

alphabetical_rocket_choices = sorted(rocketDictionary.keys())

#*** Create Listbox ***
lb = Listbox(mainWindowLeftFrame, name='lb', height=40, background="gray50", fg="white", selectbackground="MediumPurple2", highlightcolor="MediumPurple2")
lb.insert(END, *alphabetical_rocket_choices)

# *** Create & Place Scrollbars ***
rocket_scrollbar = Scrollbar(mainWindowLeftFrame, orient=VERTICAL)
lb.configure(yscrollcommand=rocket_scrollbar.set)
lb.grid(row=2, column=0, sticky=N+E+S+W)
lb.columnconfigure(0, weight=1)
rocket_scrollbar.configure(command=lb.yview)
rocket_scrollbar.grid(row=2, column=1, rowspan=40, sticky=N+S+W)

info_scrollbar = Scrollbar(mainWindowCenterFrame, command=info_canvas.yview, orient=VERTICAL)
#info_scrollbar.configure(command=info_canvas.yview)  #added command to creation of scrollbar instead of configuring it after creation
info_scrollbar.grid(row=0, column=1, rowspan=60, sticky=N+S)  #previously row=1, looked a bit different.
info_canvas.configure(yscrollcommand = info_scrollbar.set)
info_canvas.columnconfigure(0, weight=1)


# *** Populate List Box ***

alphabetical_rocket_choices = sorted(rocketDictionary.keys())

# *** Bind List Box ***
lb.bind('<<ListboxSelect>>', onselect)

# *** Bind Canvas ***
frame_inside_canvas.bind('<Configure>', on_configure) #commenting this out changes nothing...do I need it?

# *** Create all buttons/Labels ***
compareButton = Button(toolbarFrame, text="Compare", command=doNothing)
printButton = Button(toolbarFrame, text="Print", command=doNothing)

rocketListLabel = Label(mainWindowLeftFrame, bg="gray63", text="Rockets:", font="-weight bold")
search_label = Label(mainWindowLeftFrame, fg="white", bg="gray63", text="Search: ")
search_entry = Entry(mainWindowLeftFrame)


rocketName = Label(frame_inside_canvas, font="-weight bold", bg="gray63", fg="white", pady=0)
rocketName.config(font=("Arial", 24))
infoLabel = Label(frame_inside_canvas, bg="gray63", fg="white")
infoLabel.config(font=("Arial", 13 ))

imgLabel = Label(mainWindowRightFrame, bg="gray63", border=0)

label = Label(statusBarFrame, bg="gray50", fg="white")
label.grid(row=0, column=0)

# *** Placement & Layout of all Buttons ***
compareButton.grid(row=0, column=0, padx=3, pady=4, sticky=W)
printButton.grid(row=0, column=1, padx=3, pady=4, sticky=W)

rocketListLabel.grid(row=0, column=0, padx=60, pady=5, sticky=N)
search_label.grid(row=1, column=0, padx=3, sticky=W)
search_entry.grid(row=1, column=0, padx=50, pady=5, sticky=W)

rocketName.grid(row=0, column=0)
infoLabel.grid(row=1, column=0, padx=25)

imgLabel.grid(row=0, column=0, padx=120)

statusBarFrame.grid(row=2)
#statusBarFrame.grid_propagate(FALSE)  #when commented out, results in the timebar placed in center of frame as opposed to leftmost side

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
