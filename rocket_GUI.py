

import datetime
from rocket_dictionary import rocketDictionary
from PyQt_GUI import *

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())


# *** Adds Icon to window ***
# works in windows, but not on Mac...why?
#root.iconbitmap("images/rocket_icon 512.ico")


#alphabetical_rocket_choices = sorted(rocketDictionary.keys())



# *** PyQt-related Functions ***
# def insertItemToListWidget(self):
#     for rocket in alphabetical_rocket_choices:
#         self.listWidget.addItem(rocket)
#         self.listWidget.repaint()

# insertItemToListWidget()
# *** Dictionary Info Pull Functions ***

#def pushDataToLabelTitle(data):
    #return data["Name"]  


# def pushDataToLabel(data):
#     return "\n" + "\n" + "Country: " + data["Country"] + "\n" + "Agency/Company: " + "\n" + data[
#         "Agency"] + "\n" + "\n" + "Payload Capacity to LEO: " + data["Payload Capacity to LEO"] + "\n" + "Height: " \
#            + data["Height"] + "\n" + "Diameter: " + data["Diameter"] + "\n" + "Mass: " + data["Mass"] + "\n" \
#            + "Years in Operation: " + data["Years in Operation"] + "\n" + "\n" + "Additional Information: " + data[
#                "Additional Information"]


# *** Button Functionality/Functions Definitions ***
# def onselect(evt):
#     w = evt.widget
#     index = int(w.curselection()[0])
#     entry_text = w.get(index)
#     rocketName.configure(text=pushDataToLabelTitle(rocketDictionary[entry_text]))
#     infoLabel.configure(text=pushDataToLabel(rocketDictionary[entry_text]))
#     img = PhotoImage(file="images/" + rocketDictionary[entry_text]["Image"])
#     imgLabel.configure(image=img)
#     imgLabel.image = img


# def doNothing():   #for now
#     print("Nothing happened, of course.")


# def helpMenuVersionPushed():
#     tkinter.messagebox.showinfo("Version", "0.2 Alpha")


# def helpAboutPopUp():
#   aboutPopUp = Toplevel(height=600, width=800)

# def helpMenuAboutPushed():
#     tkinter.messagebox.showinfo("About",
#                                 '''
#     Developer: Seralyn Campbell

#     Email: seralyncampbell@gmail.com

#     Written in: Python 3.8.5

#     Open Source Software: 
#     https://github.com/Seralyn/rocket_info

      #Printer Icon: https://p.yusukekamiyamane.com/
      #compare Icon: Freepik from "https://www.flaticon.com/" 
      #Flag Icons: Freepik from www.flaticon.com
#                                 ''')



# def update_time():
#     currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     label['text'] = currentTime
#     root.after(1, update_time)


# def quit():
#     root.quit()


# *** Create all Frames/Containers/Canvas ***


# *** Place Canvas ***


# Layout parameters of the main containers



# *** Layout of all Frames/Containers ***

#frame_inside_canvas.grid_propagate(FALSE)

# *** Populate List Box ***



#*** Create Listbox ***



# *** Create & Place Scrollbars ***


# *** Populate List Box ***

# *** Bind List Box ***


# *** Bind Canvas ***


# *** Create all buttons/Labels ***


# *** Placement & Layout of all Buttons ***

#statusBarFrame.grid_propagate(FALSE)  #when commented out, results in the timebar placed in center of frame as opposed to leftmost side

# *** Popup Menus ***

# ***The Main Menu ***


# sticky EW seems to do nothing here. How can I stretch the status bar out to the size of the whole frame?

# *** Add Image ***
# satvphoto = PhotoImage(file="SaturnV.png")
# satvlabel = Label(root, image=satvphoto)
# satvlabel.grid(anchor=E)   #find out why this can't anchor to the right of the sorting options




#update_time()
#root.mainloop()
