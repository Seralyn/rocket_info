from tkinter import *

window = Tk()
frame = Frame(window)
canvas = Canvas(frame)
scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

def configure_scrollable_area(evt):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", configure_scrollable_area)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
for i in range(50):
    mytext = "Test Text which is really boring and no one is reading it \n" * 50
    Label(scrollable_frame, text=mytext).pack()

frame.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

window.mainloop()
