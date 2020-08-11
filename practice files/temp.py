from tkinter import *


root = Tk()

mytext = StringVar(value='test \n' * 30)

myframe = Frame(root)
myentry = Text(myframe, state='readonly')
myentry.insert
myscroll = Scrollbar(myframe, orient='vertical', command=myentry.yview)
myentry.config(yscrollcommand=myscroll.set)

myframe.grid()
myentry.grid(column=1, sticky='ns')
myscroll.grid(column=2, sticky='ns')

root.mainloop()