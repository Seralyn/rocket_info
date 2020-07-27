# import sys
# import os
import datetime
from tkinter import *
import tkinter.messagebox


root = Tk()
root.geometry("1200x700")
root.title("Working Title: Seralyn's Rocket Program")

date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# *** Rocket Info Dictionary ***
rocketDictionary = {
    'Saturn V': {
        "Name": "Saturn V",
        "Agency": "NASA - National Aeronautics & Space Administration",
        "Payload Capacity to LEO": "140,000kg (310,000 lbs)",
        "Height": "110.6m (363ft)",
        "Diameter": "10.1m (33ft)",
        "Mass": "2,970,000 kg",
        "Years in Operation": "1967-1972",
        "Country": "USA"
    },
    'Soyuz': {
        "Name": "Soyuz",
        "Agency": "Roscosmos",
        "Payload Capacity to LEO": "6,450 kilograms (14,220 lbs)",
        "Height": "45.6m (150 ft)",
        "Diameter": "10.3m (34ft)",
        "Mass": "308,000 kg",
        "Years in Operation": "1967-present",
        "Country": "Russia"
    },

    "Delta III": {
        "Name": "Delta III",
        "Agency": "ULA - United Launch Alliance",
        "Payload Capacity to LEO": "8,290 kg (18,280 lbs)",
        "Height": "35m (115ft)",
        "Diameter": "4m (13ft)",
        "Mass": "301,450 kg",
        "Years in Operation": "1993-current",
        "Country": "USA"
    },

    "Ariane 62": {
        "Name": "Ariane 62",
        "Agency": "ESA - European Space Agency",
        "Payload Capacity to LEO": "10,350 kg (22,817 lbs)",
        "Height": "63m (207ft)",
        "Diameter": "5.4m (18ft)",
        "Mass": "530,000–860,000 kg",
        "Years in Operation": "2007-2019",
        "Country": "France(EU)"
    },
    "ORBIT II": {
        "Name": "ORBIT II",
        "Agency": "CNAE - Comisión Nacional de Actividades Espaciales",
        "Payload Capacity to LEO": "250 kg to Polar",
        "Height": "28 m (92 ft)",
        "Diameter": "2.5 m (8 ft 2 in)",
        "Mass": "67,000 kg (148,000 lb) (including propellant)",
        "Years in Operation": "2020(slated)~",
        "Country": "Argentina"
    }
}


# *** Class for Button Push ***

def pushDataToLabel(data):
    return data["Name"] + "\n" + "\n" + "Country: " + data["Country"] + "\n" + "Agency/Company: " + "\n" + data[
        "Agency"] \
           + "\n" + "\n" + "Payload Capacity to LEO: " + data["Payload Capacity to LEO"] + "\n" + "Height: " \
           + data["Height"] + "\n" + "Diameter: " + data["Diameter"] + "\n" + "Mass: " + data["Mass"] + "\n" \
           + "Years in Operation: " + data["Years in Operation"]


# *** Adds Icon to window ***
# works in windows, but not on Mac...why?
root.iconbitmap("rocket_icon 512.ico")

# *** Loose Variables ***

# labelCreate = Label (mainWindowCenterFrame, text="poop", font="-weight bold")  **to create bold text**

# *** Button Functionality/Functions Definitions ***
def satVPushed():
    satVLabelCreate = Label(mainWindowCenterFrame, text="")
    satVLabelCreate.grid(row=0, column=0, padx=25)
    satVLabelCreate.configure(text=pushDataToLabel(rocketDictionary["Saturn V"]))
    # satvphoto = PhotoImage(file="SaturnV.png")
    # satvImgLabel = Label(mainWindowRightFrame, image=satvphoto)
    # satvImgLabel.grid(row=0, column=0, sticky=E)


def soyuzPushed():
    soyuzLabelCreate = Label(mainWindowCenterFrame, text="")
    soyuzLabelCreate.grid(row=0, column=0)
    # img placement here
    soyuzLabelCreate.configure(text=pushDataToLabel(rocketDictionary["Soyuz"]))


def deltaIIIPushed():
    deltaIIILabelCreate = Label(mainWindowCenterFrame, text="")
    deltaIIILabelCreate.grid(row=0, column=0)
    deltaIIILabelCreate.configure(text=pushDataToLabel(rocketDictionary["Delta III"]))


def ariane62Pushed():
    ariane62LabelCreate = Label(mainWindowCenterFrame, text="")
    ariane62LabelCreate.grid(row=0, column=0)
    # img placement here
    ariane62LabelCreate.configure(text=pushDataToLabel(rocketDictionary["Ariane 62"]))


def orbitIIPushed():
    orbitIILabelCreate = Label(mainWindowCenterFrame, text="")
    orbitIILabelCreate.grid(row=0, column=0)
    orbitIILabelCreate.configure(text=pushDataToLabel(rocketDictionary["ORBIT II"]))


def doNothing():
    print("Nothing happened, of course.")

def helpMenuVersionPushed():
    tkinter.messagebox.showinfo("Version", "0.1 Alpha")

#def helpAboutPopUp():
 #   aboutPopUp = Toplevel(height=600, width=800)

def helpMenuAboutPushed():
    tkinter.messagebox.showinfo("About",
                                '''
    Developer: Seralyn Campbell
                                
    Email: seralyncampbell@gmail.com
                                
    Written in: Python
                                
    Open Source Software: 
    https://github.com/Seralyn/rocket_info
                                ''')


def quit():
    root.quit()


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

sortMenu = Menu(menu, tearoff=FALSE)
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


# *** Create all Frames/Containers ***
toolbarFrame = Frame(root, bg="orange", width=1200, height=20)
mainWindowFrame = Frame(root, width=1200, height=650)
mainWindowLeftFrame = Frame(mainWindowFrame, width=400, height=650)
mainWindowCenterFrame = Frame(mainWindowFrame, width=400, height=650)
mainWindowRightFrame = Frame(mainWindowFrame, width=400, height=650, bg="green")
statusBarFrame = Frame(root, width=1200, height=20)

# layout parameters of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# *** Layout of all Framees/Containers ***
toolbarFrame.grid(row=0, sticky="ew")
mainWindowFrame.grid(row=1, sticky="nsew")
mainWindowLeftFrame.grid(row=0, column=0)
mainWindowCenterFrame.grid(row=0, column=1)
mainWindowCenterFrame.grid_propagate(FALSE)
mainWindowRightFrame.grid(row=0, column=2)
statusBarFrame.grid(row=2)
statusBarFrame.grid_propagate(FALSE)

# *** Create all buttons/Labels ***
insertButton = Button(toolbarFrame, text="Insert Image", command=doNothing)
printButton = Button(toolbarFrame, text="Print", command=doNothing)

rocketListLabel = Label(mainWindowLeftFrame, text="Rockets:")

satVButton = Button(mainWindowLeftFrame, relief=FLAT, text="Saturn V", bd=0, command=satVPushed)
soyuzButton = Button(mainWindowLeftFrame, text="Soyuz", bd=0, command=soyuzPushed)
deltaIIIButton = Button(mainWindowLeftFrame, text="Delta III", bd=0, command=deltaIIIPushed)
ariane62Button = Button(mainWindowLeftFrame, text="Ariane 62", bd=0, command=ariane62Pushed)
orbitIIButton = Button(mainWindowLeftFrame, text="ORBIT II", bd=0, command=orbitIIPushed)
tronadorButton = Button(mainWindowLeftFrame, text="TRONADOR", bd=0)
ausrockIVButton = Button(mainWindowLeftFrame, text="AUSROCK IV", bd=0)
vls1Button = Button(mainWindowLeftFrame, text="VLS-1", bd=0)
vlmButton = Button(mainWindowLeftFrame, text="VLM", bd=0)
fengBao1Button = Button(mainWindowLeftFrame, text="Feng Bao 1", bd=0)
kaituozhe1Button = Button(mainWindowLeftFrame, text="Kaituozhe-1", bd=0)
kuaizhouButton = Button(mainWindowLeftFrame, text="Kuaizhou", bd=0)
longMarch1Button = Button(mainWindowLeftFrame, text="Long March 1", bd=0)
longMarch1DButton = Button(mainWindowLeftFrame, text="Long March 1D", bd=0)
falcon9Button = Button(mainWindowLeftFrame, text="Falcon 9", bd=0)
falconHeavyButton = Button(mainWindowLeftFrame, text="Falcon Heavy", bd=0)
slsButton = Button(mainWindowLeftFrame, text="S.L.S. (Space Launch System)", bd=0)
newGlennButton = Button(mainWindowLeftFrame, text="New Glenn", bd=0)
hIIAButton = Button(mainWindowLeftFrame, text="HII-A", bd=0)
diamantButton = Button(mainWindowLeftFrame, text="Diamant", bd=0)
otragButton = Button(mainWindowLeftFrame, text="OTRAG", bd=0)
lambdaButton = Button(mainWindowLeftFrame, text="Lambda", bd=0)
l4sButton = Button(mainWindowLeftFrame, text="L-4S", bd=0)
muButton = Button(mainWindowLeftFrame, text="Mu", bd=0)
m4sButton = Button(mainWindowLeftFrame, text="M-4S", bd=0)

status = Label(statusBarFrame, text=date, bd=1, relief=SUNKEN)

# *** Placement & Layout of all Buttons ***
insertButton.grid(row=0, column=0, padx=3, pady=4, sticky=W)
printButton.grid(row=0, column=1, padx=3, pady=4, sticky=W)

rocketListLabel.grid(row=0, column=0, padx=60, pady=5, sticky=N)

satVButton.grid(row=1, column=0, padx=15)
soyuzButton.grid(row=2, column=0, padx=15)
deltaIIIButton.grid(row=3, column=0, padx=15)
ariane62Button.grid(row=4, column=0, padx=15)
orbitIIButton.grid(row=5, column=0, padx=15)
tronadorButton.grid(row=6, column=0, padx=15)
ausrockIVButton.grid(row=7, column=0, padx=15)
vls1Button.grid(row=8, column=0, padx=15)
vlmButton.grid(row=9, column=0, padx=15)
fengBao1Button.grid(row=10, column=0, padx=15)
kaituozhe1Button.grid(row=11, column=0, padx=15)
kuaizhouButton.grid(row=12, column=0, padx=15)
longMarch1Button.grid(row=13, column=0, padx=15)
longMarch1DButton.grid(row=14, column=0, padx=15)
falcon9Button.grid(row=15, column=0, padx=15)
falconHeavyButton.grid(row=16, column=0, padx=15)
slsButton.grid(row=17, column=0, padx=15)
newGlennButton.grid(row=18, column=0, padx=15)
hIIAButton.grid(row=19, column=0, padx=15)
diamantButton.grid(row=20, column=0, padx=15)
otragButton.grid(row=21, column=0, padx=15)
lambdaButton.grid(row=22, column=0, padx=15)
l4sButton.grid(row=23, column=0, padx=15)
muButton.grid(row=24, column=0, padx=15)
m4sButton.grid(row=25, column=0, padx=15)

status.grid(row=0, columnspan=5, sticky="EW")
# sticky EW seems to do nothing here. How can I stretch the status bar out to the size of the whole frame?

# *** Add Image ***
# satvphoto = PhotoImage(file="SaturnV.png")
# satvlabel = Label(root, image=satvphoto)
# satvlabel.grid(anchor=E)   #find out why this can't anchor to the right of the sorting options

# **To remind usage of .grid() system instead of .pack() system
# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)

'''If you want to handle jpg as well as png, import Image and ImageTk from PIL then do:
image = Image.open("Image Name")
photo = ImageTk.PhotoImage(image)'''

root.mainloop()
