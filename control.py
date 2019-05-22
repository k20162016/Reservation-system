import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dbconact import DBConnect
from ListRequest import ListTicket
Dbconnect = DBConnect()

root = Tk()
root.title('Ticket reservation')
root.config(background="#e1d8b2")
# Style
style = ttk.Style()
style.theme_use('classic')
style.configure('TLabel', background="#e1d8b2")
style.configure('TButton', background="#e1d8b2")
style.configure('TRadiobutton', background="#e1d8b2")

# FullName
ttk.Label(root, text='Full Name:').grid(row=0, column=0, padx=10, pady=10)
EntryFullName = ttk.Entry(root, width=30, font=('Arial', 16))
EntryFullName.grid(row=0, column=1, columnspan=2, pady=10)
# gender
ttk.Label(root, text='Gender:').grid(row=1, column=0)
SpanGender = StringVar()
ttk.Radiobutton(root, text='Male', variable=SpanGender, value='Male').grid(row=1, column=1)
ttk.Radiobutton(root, text='Famle', variable=SpanGender, value='Famle').grid(row=1, column=2)
# comment
ttk.Label(root, text='Comments:').grid(row=2, column=0)
txtComments = Text(root, width=30, height=15, font=('Aroal', 16))
txtComments.grid(row=2, column=1, columnspan=2)
# butoons
BuSubmit = ttk.Button(root, text='Submit :')
BuSubmit.grid(row=3, column=3)
buList = ttk.Button(root, text='List Res :')
buList.grid(row=3, column=2)


# fun
def BuSaveData():
    # print('Full Name:{}'.format(EntryFullName.get()))
     #print('Gender:{}'.format(SpanGender.get()))
     #print('Comments:{}'.format(txtComments.get(1.0,'end')))
    msg = Dbconnect.Add(EntryFullName.get(), SpanGender.get(), txtComments.get(1.0, 'end'))
    messagebox.showinfo(title='Add info', message=msg)
    EntryFullName.delete(0, 'end')
    txtComments.delete(1.0, 'end')


def BuListData():
    # TODO: show orders
    #print(' not implemented yet')
      listrequest=ListTicket()




BuSubmit.config(command=BuSaveData)
buList.config(command=BuListData)

root.mainloop()
