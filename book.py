from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *

mainwin = Tk()

mainwin.title("My Adress Book")
maintitle = Label(mainwin, text = "My Adress Book")
maintitle.grid(row = 0, column = 0, columnspan = 3, pady = 4)

open_button = Button(mainwin, text = "Open", command = None)
open_button.grid(row = 0, column = 3, pady = 4)

listbox = Listbox(mainwin)
listbox.grid(row = 1, rowspan = 5, column = 0, columnspan = 3)

name_label = Label(mainwin, text = "Name")
name_label.grid(row = 1, column = 3, padx = 3)

name_entry = Entry(mainwin)
name_entry.grid(row = 1, column = 4)

address_label = Label(mainwin, text = "Address")
address_label.grid(row = 2, column = 3, pady = 3)

address_entry = Entry(mainwin)
address_entry.grid(row = 2, column = 4)

mobile_label = Label(mainwin, text = "Mobile")
mobile_label.grid(row = 3, column = 3)

mobile_entry = Entry(mainwin)
mobile_entry.grid(row = 3, column = 4)

email_label = Label(mainwin, text = "Email")
email_label.grid(row = 4, column = 3)

email_entry = Entry(mainwin)
email_entry.grid(row = 4, column = 4)

edit_button = Button(mainwin, text = "Edit", command = None)
edit_button.grid(row = 6, column = 0)

delete_button = Button(mainwin, text = "Delete", command = None)
delete_button.grid(row = 6, column = 1)

update_button = Button(mainwin, text = "Update/Add", command = None)
update_button.grid(row = 6, column = 4)

save_button = Button(mainwin, text = "Save", width = 40, command = None)
save_button.grid(row = 7, column = 1, columnspan = 3)











mainwin.mainloop()


