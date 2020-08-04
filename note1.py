scrollbar = Scrollbar(master)
scrollbar.grid(xxxx)

lb = Listbox(mainFrameLeft, name='lb', yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

mainloop()

-------------------------------------
def mainframe():
    lb = Listbox(bg='red')
    scrollbar = Scrollbar(lb, orient=VERTICAL)
    .config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lb.yview)