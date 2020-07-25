from tkinter import *
import tkinter.messagebox
#from PIL import ImageTk,Image
#import sys
#import os
import datetime

root = Tk()
root.geometry("1200x700")
root.title("Seralyn's Rocket Program")

date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# *** Rocket Info Dictionary ***
dct1 = {
        'Saturn V': ["Saturn V",
                     "NASA - National Aeronautics & Space Administration",
                     "Payload Capacity to LEO: 140,000kg (310,000 lbs)",
                     "Height: 110.6m (363ft)",
                     "Diameter: 10.1m (33ft)",
                     "Mass: 2,970,000 kg"],
        "Soyuz": ["Soyuz",
                  "Roscosmos",
                  "Payload Capacity to LEO: 6,450 kilograms (14,220 lbs)",
                  "Height: 45.6m (150 ft)",
                  "Diameter: 10.3m (34ft)",
                  "Mass: 308,000 kg"],
        "Delta III": ["Delta III",
                      "ULA - United Launch Alliance",
                      "Payload Capacity to LEO: 8,290 kg (18,280 lbs)",
                      "Height: 35m (115ft)", "Diameter: 4m (13ft)", "Mass: 301,450 kg"],
        "Ariane 62": ["Ariane 62",
                      "ESA - European Space Agency",
                      "Payload Capacity to LEO: 10,350 kg (22,817 lbs)",
                      "Height: 63m (207ft)",
                      "Diameter: 5.4m (18ft)",
                      "Mass: 530,000–860,000 kg"]
    }

# *** Class for Button Push ***
#class ButtonPush:

# *** Button Functionality Functions ***
def satVPushed():
    satVLabelCreate = Label(mainWindowCenterFrame, text=dct1['Saturn V'])
    satVLabelCreate.grid(row=0, column=0)
    
# *** Adds Icon to window ***
root.iconbitmap("rocket_icon 512.ico")

# *** Functions Definitionns ***

def doNothing():
    print("Nothing happened, of course.")

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

# *** Create all Frames/Containers ***
toolbarFrame = Frame(root, bg="orange", width=1200, height=20)
mainWindowFrame = Frame(root, width=1200, height=650)
mainWindowLeftFrame = Frame(mainWindowFrame, width=400, height=650)
mainWindowCenterFrame = Frame(mainWindowFrame, width=400, height=650, bg="blue")
mainWindowRightFrame = Frame(mainWindowFrame, width=400, height=650, bg="green")
statusBarFrame = Frame(root, bg="red", width=1200, height=20)

# layout parameters of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


# *** Layout of all Framees/Containers ***
toolbarFrame.grid(row=0, sticky="ew")
mainWindowFrame.grid(row=1, sticky="nsew")
mainWindowLeftFrame.grid(row=0, column=0)
mainWindowCenterFrame.grid(row=0, column=1)
mainWindowRightFrame.grid(row=0, column=2)
statusBarFrame.grid(row=2)


# *** Create all buttons/Labels ***
insertButton = Button(toolbarFrame, text="Insert Image",command=doNothing)
printButton = Button(toolbarFrame, text="Print", command=doNothing)

rocketListLabel = Label(mainWindowLeftFrame, text= "Rockets:")

satVButton = Button(mainWindowLeftFrame, text="Saturn V", bd=0, command=satVPushed)
soyuzButton = Button(mainWindowLeftFrame, text="Soyuz", bd=0)
deltaIIIButton = Button(mainWindowLeftFrame, text="Delta III", bd=0)
ariane62Button = Button(mainWindowLeftFrame, text="Ariane 62", bd=0)
orbitIIButton = Button(mainWindowLeftFrame, text="ORBIT II", bd=0)
tronadorButton = Button(mainWindowLeftFrame, text="TRONADOR", bd=0)
ausrockIVButton = Button(mainWindowLeftFrame, text="AUSROCK IV", bd=0)
vls1Button = Button(mainWindowLeftFrame, text="VLS-1", bd=0)
vlmButton = Button(mainWindowLeftFrame, text="VLM", bd=0)
fengBao1Button = Button(mainWindowLeftFrame, text="Feng Bao 1", bd=0)
kaituozhe1Button = Button(mainWindowLeftFrame, text="Kaituozhe-1", bd=0)
kuaizhouButton = Button(mainWindowLeftFrame, text="Kuaizhou", bd=0)
longMarch1Button = Button(mainWindowLeftFrame, text="Long March 1", bd=0)
longMarch1DButton = Button(mainWindowLeftFrame, text="Long March 1D", bd=0)


status = Label(statusBarFrame, text=date, bd=1, relief=SUNKEN)


# *** Placement & Layout of all Buttons ***
insertButton.grid(row=0, column=0, padx=3, pady=4, sticky=W)
printButton.grid(row=0, column=1, padx=3, pady=4, sticky=W)

rocketListLabel.grid(row=0, column=0, padx=60, pady=5, sticky=N)

satVButton.grid(row= 1, column=0)
soyuzButton.grid(row= 2, column=0)
deltaIIIButton.grid(row= 3, column=0)
ariane62Button.grid(row= 4, column=0)
orbitIIButton.grid(row=5, column=0)
tronadorButton.grid(row=6, column=0)
ausrockIVButton.grid(row=7, column=0)
vls1Button.grid(row=8, column=0)
vlmButton.grid(row=9, column=0)
fengBao1Button.grid(row=10, column=0)
kaituozhe1Button.grid(row=11, column=0)
kuaizhouButton.grid(row=12, column=0)
longMarch1Button.grid(row=13, column=0)
longMarch1DButton.grid(row=14, column=0)


status.grid(row=0, columnspan=5)
'''
sortRocketsLabel.grid(row=1, column=0)

alphabeticalButton.grid(row=2, column=0)
agencyButton.grid(row=3, column=0)
countryButton.grid(row=4, column=0)
classButton.grid(row=5, column=0)
operationalButton.grid(row=6, column=0)
payloadHLButton.grid(row=7, column=0)
payloadLHButton.grid(row=8, column=0)
massHLButton.grid(row=9, column=0)
massLHButton.grid(row=10, column=0)
diameterHLButton.grid(row=11, column=0)
massLHButton.grid(row=12, column=0)
heightHLButton.grid(row=13, column=0)
heightLHButton.grid(row=14, column=0)
'''

# *** Add Image ***
#satvphoto = PhotoImage(file="SaturnV.png")
#satvlabel = Label(root, image=satvphoto)
#satvlabel.grid(anchor=E)   #find out why this can't anchor to the right of the sorting options

# **To remind usage of .grid() system instead of .grid() system
#entry_1.grid(row=0, column=1)
#entry_2.grid(row=1, column=1)

'''If you want to handle jpg as well as png, import Image and ImageTk from PIL then do:
image = Image.open("Image Name")
photo = ImageTk.PhotoImage(image)'''

# *** The Status Bar [bottom] ***





root.mainloop()
