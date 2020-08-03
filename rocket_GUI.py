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
toolbarFrame = Frame(root, bg="plum4", width=1200, height=20)
mainWindowFrame = Frame(root, bg="gray63", width=1200, height=650)
mainWindowLeftFrame = Frame(mainWindowFrame, bg="gray63", width=400, height=650, padx=10)
mainWindowCenterFrame = Frame(mainWindowFrame, bg="gray63", width=500, height=650)
mainWindowRightFrame = Frame(mainWindowFrame, bg="gray63", width=400, height=650)
statusBarFrame = Frame(root, bg="gray76", width=1350, height=20)

# layout parameters of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

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

#*** Create Listbox ***
lb = Listbox(mainWindowLeftFrame, name='lb', height=40,  background="gray50", fg="white", selectbackground="MediumPurple2", highlightcolor="MediumPurple2")

# *** Create & Place Scrollbars ***
rocket_scrollbar = Scrollbar(mainWindowLeftFrame, orient=VERTICAL)
lb.configure(yscrollcommand=rocket_scrollbar.set)
rocket_scrollbar.configure(command=lb.yview)
lb.grid(row=1, column=0, sticky=N+E+S+W)
lb.columnconfigure(0, weight=1)
rocket_scrollbar.grid(row=1, column=1, rowspan=40, sticky=N+S)

info_scrollbar = Scrollbar(mainWindowCenterFrame, orient=VERTICAL)
lb.configure(yscrollcommand=info_scrollbar.set)
info_scrollbar.configure(command=lb.yview)
lb.grid(row=1, column=0, sticky=N+E+S+W)
lb.columnconfigure(0, weight=1)
info_scrollbar.grid(row=1, column=1, rowspan=40, sticky=N+S)


# *** Populate List Box ***
lb.insert(END, "Ariane 1")
lb.insert(END, "Ariane 2")
lb.insert(END, "Ariane 3")
lb.insert(END, "Ariane 4")
lb.insert(END, "Ariane 5")
lb.insert(END, "Ariane 62")
lb.insert(END, "Ariane M")
lb.insert(END, "Miura 5")
lb.insert(END, "Tronador II")
lb.insert(END, "VLS-1")
lb.insert(END, "VLM")
lb.insert(END, "Diamant")
lb.insert(END, "OTRAG")
lb.insert(END, "L-4S")
lb.insert(END, "M-4S")
lb.insert(END, "M-3C")
lb.insert(END, "M-3H")
lb.insert(END, "M-3S")
lb.insert(END, "M-3SII")
lb.insert(END, "M-V")
lb.insert(END, "N-I")
lb.insert(END, "N-II")
lb.insert(END, "H-I")
lb.insert(END, "H-IIA")
lb.insert(END, "H-IIB")
lb.insert(END, "H3")
lb.insert(END, "J-I")
lb.insert(END, "GX")
lb.insert(END, "Epsilon")
lb.insert(END, "SS-520")
lb.insert(END, "ZERO")
lb.insert(END, "Electron")
lb.insert(END, "Paektusan-1")
lb.insert(END, "Unha-2")
lb.insert(END, "Unha-3")
lb.insert(END, "TSLV")
lb.insert(END, "Hapith V")
lb.insert(END, "HTTP-3a")
lb.insert(END, "Haas")
lb.insert(END, "Angara")
lb.insert(END, "CORONA (SSTO)")
lb.insert(END, "Kosmos-1")
lb.insert(END, "Kosmos-2I")
lb.insert(END, "Kosmos-3")
lb.insert(END, "Kosmos-3M")
lb.insert(END, "Buran")
lb.insert(END, "N1")
lb.insert(END, "R-7")
lb.insert(END, "Luna")
lb.insert(END, "Molniya-M")
lb.insert(END, "Molniya-L")
lb.insert(END, "Polyot")
lb.insert(END, "Soyuz")
lb.insert(END, "Soyuz-L")
lb.insert(END, "Soyuz-M")
lb.insert(END, "Soyuz-U")
lb.insert(END, "Soyuz-U2")
lb.insert(END, "Soyuz-FG")
lb.insert(END, "Soyuz-2")
lb.insert(END, "Sputnik")
lb.insert(END, "Voskhod")
lb.insert(END, "Vostok")
lb.insert(END, "Shtil'")
lb.insert(END, "Volna")
lb.insert(END, "Rus-M")
lb.insert(END, "Start-1")
lb.insert(END, "Universal Rocket")
lb.insert(END, "Rokot")
lb.insert(END, "Strela")
lb.insert(END, "Proton UR-500")
lb.insert(END, "Proton-K")
lb.insert(END, "Proton-M")
lb.insert(END, "Energia")
lb.insert(END, "RSA-3")
lb.insert(END, "CHEETAH-1")
lb.insert(END, "KSLV-1(Naro)")
lb.insert(END, "KSLV-2(Nuri)")
lb.insert(END, "KSLV-3")
lb.insert(END, "Capricornio")
lb.insert(END, "PLD Space Miura 5")
lb.insert(END, "UFS")
lb.insert(END, "Zenit")
lb.insert(END, "Zenit 2")
lb.insert(END, "Zenit 2M")
lb.insert(END, "Zenit-3SL")
lb.insert(END, "Zenit 3SLB")
lb.insert(END, "Zenit-3F")
lb.insert(END, "Dnepr")
lb.insert(END, "Tsyklon")
lb.insert(END, "Tsyklon-2")
lb.insert(END, "Tsyklon-3")
lb.insert(END, "Tsyklon-4")
lb.insert(END, "Cyclone-4M")
lb.insert(END, "Black Arrow")
lb.insert(END, "Black Prince")
lb.insert(END, "Prime")
lb.insert(END, "Skyrora XL")
lb.insert(END, "Europa")
lb.insert(END, "Hermes")
lb.insert(END, "Vega")
lb.insert(END, "Satellite Launch Vehicle")
lb.insert(END, "Augmented Satellite Launch Vehicle")
lb.insert(END, "PSLV-CA")
lb.insert(END, "PSLV-XL")
lb.insert(END, "PSLV-DL")
lb.insert(END, "PSLV-QL")
lb.insert(END, "PSLV-3S")
lb.insert(END, "GSLV Mk I (a)")
lb.insert(END, "GSLV Mk I (b)")
lb.insert(END, "GSLV Mk II)")
lb.insert(END, "Geosynchronous Satellite Launch Vehicle Mark III")
lb.insert(END, "Small Satellite Launch Vehicle")
lb.insert(END, "Reusable Launch Vehicle")
lb.insert(END, "Unified Modular Launch Vehicle")
lb.insert(END, "Feng Bao 1")
lb.insert(END, "Kaituozhe-1")
lb.insert(END, "Kuaizhou")
lb.insert(END, "Long March 1")
lb.insert(END, "Long March 1D")
lb.insert(END, "Long March 2A")
lb.insert(END, "Long March 2C")
lb.insert(END, "Long March 2D")
lb.insert(END, "Long March 2E")
lb.insert(END, "Long March 2F")
lb.insert(END, "Long March 3")
lb.insert(END, "Long March 3A")
lb.insert(END, "Long March 3B")
lb.insert(END, "Long March 3B/E")
lb.insert(END, "Long March 3C")
lb.insert(END, "Long March 4A")
lb.insert(END, "Long March 4B")
lb.insert(END, "Long March 4C")
lb.insert(END, "Long March 5")
lb.insert(END, "Long March 5B")
lb.insert(END, "Long March 6")
lb.insert(END, "Long March 7")
lb.insert(END, "Long March 8")
lb.insert(END, "Long March 9")
lb.insert(END, "Long March 11")
lb.insert(END, "Jeilong-1")
lb.insert(END, "Hyperbola-1")
lb.insert(END, "RPS-420")
lb.insert(END, "RPS-550")
lb.insert(END, "Safir")
lb.insert(END, "Simorgh")
lb.insert(END, "Qased")
lb.insert(END, "Al Abid")
lb.insert(END, "Shavid")
lb.insert(END, "Alpha")
lb.insert(END, "Antares")
lb.insert(END, "Ares I")
lb.insert(END, "Ares IV")
lb.insert(END, "Ares V")
lb.insert(END, "Athena I")
lb.insert(END, "Athena II")
lb.insert(END, "Atlas B")
lb.insert(END, "Atlas D")
lb.insert(END, "Atlas-Able")
lb.insert(END, "Atlas-Agena")
lb.insert(END, "Atlas E/F")
lb.insert(END, "Atlas H")
lb.insert(END, "Atlas LV-3B")
lb.insert(END, "Atlas SLV-3")
lb.insert(END, "Atlas-Centaur")
lb.insert(END, "Atlas G")
lb.insert(END, "Atlas I")
lb.insert(END, "Atlas II")
lb.insert(END, "Atlas III")
lb.insert(END, "Atlas V")
lb.insert(END, "Conestoga")
lb.insert(END, "Minotaur I")
lb.insert(END, "Minotaur IV")
lb.insert(END, "Minotaur V")
lb.insert(END, "Minotaur-C")
lb.insert(END, "New Glenn")
lb.insert(END, "OmegA")
lb.insert(END, "Pegasus")
lb.insert(END, "Phantom Express")
lb.insert(END, "Pilot")
lb.insert(END, "Redstone")
lb.insert(END, "Juno I")
lb.insert(END, "Sparta")
lb.insert(END, "Saturn I")
lb.insert(END, "Saturn IB")
lb.insert(END, "Saturn V")
lb.insert(END, "Saturn INT-21")
lb.insert(END, "Scout")
lb.insert(END, "Space Shuttle")
lb.insert(END, "SLS")
lb.insert(END, "Falcon 1")
lb.insert(END, "Falcon 1e")
lb.insert(END, "Falcon 5")
lb.insert(END, "Falcon 9")
#Falcon 9 Air - Canceled
#Falcon 9 v1.0 - Retired
#Falcon 9 v1.1 - Retired
#Falcon 9 Full Thrust
lb.insert(END, "Falcon Heavy")
lb.insert(END, "Starship")
lb.insert(END, "Thor")
lb.insert(END, "Thor-Able")
lb.insert(END, "Thor-Ablestar")
lb.insert(END, "Thor-Agena")
lb.insert(END, "Thorad-Agena")
lb.insert(END, "Thor-Burner")
lb.insert(END, "Thor DSV-2U")
lb.insert(END, "Thor-Delta")
lb.insert(END, "Delta A")
lb.insert(END, "Delta B")
lb.insert(END, "Delta C")
lb.insert(END, "Delta D")
lb.insert(END, "Delta E")
lb.insert(END, "Delta G")
lb.insert(END, "Delta J")
lb.insert(END, "Delta L")
lb.insert(END, "Delta M")
lb.insert(END, "Delta N")
lb.insert(END, "Delta 0100")
lb.insert(END, "Delta 1000")
lb.insert(END, "Delta 2000")
lb.insert(END, "Delta 3000")
lb.insert(END, "Delta 4000")
lb.insert(END, "Delta 5000")
lb.insert(END, "Delta II 6000")
lb.insert(END, "Delta II 7000")
lb.insert(END, "Delta III")
lb.insert(END, "Delta IV")
lb.insert(END, "Delta IV Heavy")
lb.insert(END, "LauncherOne")
lb.insert(END, "Titan")
lb.insert(END, "Titan II GLV")
lb.insert(END, "Titan 23G")
lb.insert(END, "Titan IIIB")
lb.insert(END, "Titan III")
lb.insert(END, "Titan 34D")
lb.insert(END, "Commercial Titan III")
lb.insert(END, "Titan IV")
lb.insert(END, "Vanguard")
lb.insert(END, "Vector-R")
lb.insert(END, "Vulcan")

# *** Place List Box ***
lb.bind('<<ListboxSelect>>', onselect)


# *** Create all buttons/Labels ***
insertButton = Button(toolbarFrame, text="Insert Image", command=doNothing)
printButton = Button(toolbarFrame, text="Print", command=doNothing)

rocketListLabel = Label(mainWindowLeftFrame, bg="gray63", text="Rockets:", font="-weight bold")

rocketName = Label(mainWindowCenterFrame, font="-weight bold", bg="gray63", fg="white")
rocketName.config(font=("Arial", 20))
infoLabel = Label(mainWindowCenterFrame, bg="gray63", fg="white")
infoLabel.config(font=("Arial", 11))

imgLabel = Label(mainWindowRightFrame, bg="gray63", border=0)

label = Label(statusBarFrame, text="placeholder")
label.grid(row=0, column=0)

# *** Placement & Layout of all Buttons ***
insertButton.grid(row=0, column=0, padx=3, pady=4, sticky=W)
printButton.grid(row=0, column=1, padx=3, pady=4, sticky=W)

rocketListLabel.grid(row=0, column=0, padx=60, pady=5, sticky=N)

rocketName.grid(row=0, column=0)
infoLabel.grid(row=1, column=0, padx=25)

imgLabel.grid(row=0, column=0, padx=120)

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
