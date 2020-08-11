import tkinter as tk

window = tk.Tk()
frame = tk.Frame()

# Function to handle what happens when an item is selected in the list box
# NOTE: first argument 'evt' stands for 'event' and it has to be always passed
def onselect(evt):
    # getting widget from the event
    w = evt.widget
    # from the widget we get cursor selection
    # I doubt it will ever need anything but [0], unless you're allowing to select multiple items at once.
    index = int(w.curselection()[0])
    print("index:" + str(index))
    # from the widget we acquired in the previous line
    # we get the value (or text) of the listbox item
    # and printing it out to the terminal to confirm that the selection happened. Voila!
    entry_text = w.get(index)
    print(entry_text)
    # once you have the selection, you can perform checks like
    # if w.get(index) == "Saturn V":
    #     show saturn V photo!

lb = tk.Listbox(frame, name='lb')

# this is a way to bind events to a listbox.
# this time we are binding the ListboxSelect event.
lb.bind('<<ListboxSelect>>', onselect)

frame.pack()
lb.pack()
# inserting items to a listbox
lb.insert(tk.END, "One Mississippi")
lb.insert(tk.END, "Two Mississippi")

window.mainloop()