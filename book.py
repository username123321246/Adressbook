from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *

mainwin = Tk()
addressbook = {}

def clear_all():
    name_entry.delete(0,END)
    address_entry.delete(0, END)
    mobile_entry.delete(0, END)
    email_entry.delete(0, END)
    

def update():
    key = name_entry.get()
    if key == "":
        messagebox.showinfo("Error","Name can't be empty")
    else:
        if key not in addressbook.keys():
            listbox.insert(END, key)
        addressbook[key] = (address_entry.get(), mobile_entry.get(), email_entry.get())
        clear_all()
            

def saveFile():
        fout = asksaveasfile(defaultextension = ".txt")
        if fout is not None:
            print(addressbook, file = fout)
        else:
            messagebox.showinfo("Error", "Couldn't save file")


def openFile():
    global addressbook
    clear_all()
    fin = askopenfile(title = "Open File")
# If filename selected
    if fin:
        addressbook = eval(fin.read())
        for key in addressbook.keys():
            listbox.insert(END, key)
    else:
        messagebox.showinfo("Error", "Can't open file")

def edit():
     clear_all()
     index = listbox.curselection()
     if index:
        name_entry.insert(0, listbox.get(index))
        details = addressbook[name_entry.get()]         
     #get details corresponding to anem from dictioary
        address_entry.insert(0, details[0])
        mobile_entry.insert(0, details[1])
        email_entry.insert(0, details[2])
     else:
        messagebox.showinfo("Error", "Information is missing.")
def delete():
    index = listbox.curselection()
    if index:
        del addressbook[listbox.get(index)]
        listbox.delete(index)
        clear_all()
    else:
        messagebox.showinfo("Error", "Select a name.")

def display(event):
    newWindow = Toplevel(mainwin)
    index = listbox.curselection()

    contact =""
    if index:
        key = listbox.get(index)
        contact = "Name   :" + key + "\n"

        details = addressbook[key]
        contact += "Address   :" + details[0] + "\n"
        contact += "Mobile    :" + details[1] + "\n"
        contact += "Email     :" + details[2] + "\n"

    window = Label(newWindow)
    window.grid(row = 0, column = 0)
    window.configure(text = contact)
    






mainwin.title("My Adress Book")
maintitle = Label(mainwin, text = "My Adress Book")
maintitle.grid(row = 0, column = 0, columnspan = 3, pady = 4)

open_button = Button(mainwin, text = "Open", command = openFile)
open_button.grid(row = 0, column = 3, pady = 4)

listbox = Listbox(mainwin)
listbox.grid(row = 1, rowspan = 5, column = 0, columnspan = 3)
listbox.bind('<<ListboxSelect>>', display)

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

edit_button = Button(mainwin, text = "Edit", command = edit)
edit_button.grid(row = 6, column = 0)

delete_button = Button(mainwin, text = "Delete", command = delete)
delete_button.grid(row = 6, column = 1)

update_button = Button(mainwin, text = "Update/Add", command = update)
update_button.grid(row = 6, column = 4)

save_button = Button(mainwin, text = "Save", width = 30, command = saveFile)
save_button.grid(row = 7, column = 1, columnspan = 3)






mainwin.mainloop()


