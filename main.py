from tkinter import *
#from function_users import *
from tkinter import messagebox

root = Tk()
root.title('Phone book')
root.geometry('500x250')
root.iconbitmap('contacts.ico')


labelSuccessSave = Label(root,text="Great add!",font=('Arial', 10, 'bold'))
# def successSave():
#     labelSuccessSave.place(relx=.5, rely=.4, anchor="c", height=200, width=450, bordermode=OUTSIDE)

def saveUsers():
    with open('contacts.txt', 'a') as saveFile:
        saveFile.write("\n" + firstName.get() + " " + lastName.get() + ", " + phoneNum.get())
    #root.withdraw() #hide window root
    #messagebox.showinfo('Status:', firstName.get() + " " + lastName.get() + "\nadded successfully!")
    labelNewUser.place_forget()
    labelSuccessSave.place(relx=.5, rely=.4, anchor="c", height=200, width=450, bordermode=OUTSIDE)
    labelSuccessSave.after(3000, labelSuccessSave.place_forget())
    labelNewUser.place(relx=.5, rely=.4, anchor="c", height=200, width=450, bordermode=OUTSIDE)
    # firstName.delete(0, END) #clean fields
    # lastName.delete(0, END)
    # phoneNum.delete(0, END)
    #root.deiconify() #show again window root after closing messagebox



labelNewUser = LabelFrame(root,text="New contact:",font=('Arial', 10, 'bold'))
def newUserAdd():
    root.geometry('500x300')
    labelNewUser.place(relx=.5, rely=.4, anchor="c", height=200, width=450, bordermode=OUTSIDE)
    labelShowUsers.place_forget()

labelShowUsers = LabelFrame(text="All contacts:", font=('Arial', 10, 'bold'))
def showUsers():
    root.geometry('500x500')
    labelNewUser.place_forget()
    labelShowUsers.place(x=250, y=240, anchor="c", height=470, width=450, bordermode=OUTSIDE)
    with open('users.txt', 'r') as saveFile:
        for line in saveFile:
            contactList.insert(0, line)

# new contact
firstName = StringVar()
lastName = StringVar()
phoneNum = StringVar()

firstName = Entry(labelNewUser,textvariable=firstName, width=45)
firstName.grid(row=1, column=1, padx=0, pady=10, sticky="W")
labelFirstName = Label(labelNewUser,text='Name:', justify=RIGHT, padx=30)
labelFirstName.grid(row=1, column=0)

lastName = Entry(labelNewUser, textvariable=lastName, width=45)
lastName.grid(row=2, column=1, padx=0, pady=10, sticky="W")
labelLastName = Label(labelNewUser, text='Surname:', justify=RIGHT, padx=30)
labelLastName.grid(row=2, column=0)

phoneNum = Entry(labelNewUser, textvariable=phoneNum, width=45)
phoneNum.grid(row=3, column=1, padx=0, pady=10, sticky="W")
labelPhoneNum = Label(labelNewUser, text='Phone:', justify=RIGHT, padx=30)
labelPhoneNum.grid(row=3, column=0)

btnReg = Button(labelNewUser, text="Add", width=10, command=saveUsers)
btnReg.grid(row=4, column=1, padx=0, pady=20)

# удаление выделенного элемента
def delete():
    selection = contactList.curselection()
    # мы можем получить удаляемый элемент по индексу
    # selected_language = languages_listbox.get(selection[0])
    contactList.delete(selection[0])

# создаем список
contactList = Listbox(labelShowUsers, height=40, width=110)
contactList.place()

btnDelete = Button(labelShowUsers, text="Delete",width=10, command=delete)
btnDelete.place(x=190, y=410)

# menu
mainMenu = Menu()
mainMenu.add_cascade(label='New', command=newUserAdd)
mainMenu.add_cascade(label='View all', command=showUsers)
mainMenu.add_cascade(label='Edit')
mainMenu.add_cascade(label='Exit', command=root.quit, font=("Verdana", 8, 'bold'))

root.config(menu=mainMenu)

root.mainloop()