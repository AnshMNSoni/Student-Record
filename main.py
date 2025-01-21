from tkinter import *
from tkinter import messagebox, simpledialog

FONT1 = ('Roboto', 18, 'normal')
Students = {}

class DataBase:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Student DataBase")
        self.window.config(padx=40, pady=40)
        
        self.window.newrecord = Button(text="New Record", font=FONT1, command=self.newrecord_fn)
        self.window.newrecord.grid(row=0, column=0, padx=40, pady=40)
        
        self.window.updaterecord = Button(text="Update Record", font=FONT1, command=self.updaterecord_fn)
        self.window.updaterecord.grid(row=0, column=1, padx=40, pady=40)
        
        self.window.findrecord = Button(text="Find Record", font=FONT1, command=self.findrecord_fn)
        self.window.findrecord.grid(row=1, column=0, padx=40, pady=40)

        self.window.deleterecord = Button(text="Delete Record", font=FONT1, command=self.deleterecord_fn)
        self.window.deleterecord.grid(row=1, column=1, padx=40, pady=40)
        
        
        self.window.mainloop()
        
    # New Record:
    def newrecord_fn(self):
        self.window.destroy()
        
        self.newwindow = Tk()
        self.newwindow.title("New Record")
        
        # Student Roll Number
        self.newwindow.stu_roll_label = Label(text="Roll Number: ")
        self.newwindow.stu_roll_label.grid(row=0, column=0)
        
        get_roll = StringVar()
        self.newwindow.stu_roll = Entry(master=self.newwindow, textvariable=get_roll)
        self.newwindow.stu_roll.grid(row=0, column=1)
        self.newwindow.stu_roll.focus()
        
        # Student Name 
        self.newwindow.stu_name_label = Label(text="Name: ")
        self.newwindow.stu_name_label.grid(row=1, column=0)
        
        get_name = StringVar()
        self.newwindow.stu_name = Entry(master=self.newwindow, textvariable=get_name)
        self.newwindow.stu_name.grid(row=1, column=1)
        
        # Student Age
        self.newwindow.stu_age_label = Label(text="Age: ")
        self.newwindow.stu_age_label.grid(row=2, column=0)
        
        get_age = IntVar()
        self.newwindow.stu_age = Entry(master=self.newwindow, textvariable=get_age)
        self.newwindow.stu_age.grid(row=2, column=1)
        
        # Student Department
        self.newwindow.stu_dep_label = Label(text="Department: ")
        self.newwindow.stu_dep_label.grid(row=3, column=0)
        
        get_dep = StringVar()
        self.newwindow.stu_dep = Entry(master=self.newwindow, textvariable=get_dep)
        self.newwindow.stu_dep.grid(row=3, column=1)
        
        self.newwindow.btn = Button(text="Add", command=self.confirmrecord)
        self.newwindow.btn.grid(row=4, column=0)
        
    # Confirm Add Record:
    def confirmrecord(self):
        Students.update({self.newwindow.stu_roll.get(): [self.newwindow.stu_name.get(), int(self.newwindow.stu_age.get()), self.newwindow.stu_dep.get()]})
        
        self.newwindow.destroy()
        DataBase()    
        
    # Update Record:
    def updaterecord_fn(self):
        self.window.destroy()
        
        self.updatewindow = Tk()
        self.updatewindow.title("Update Record")
        
        self.updatewindow.find_roll_label = Label(text="Roll Number: ")
        self.updatewindow.find_roll_label.grid(row=0, column=0)
        
        global find_roll
        find_roll = StringVar()
        self.updatewindow.find_roll = Entry(master=self.updatewindow, textvariable=find_roll)
        self.updatewindow.find_roll.grid(row=0, column=1)
        
        self.updatewindow.btn = Button(text="Find", command=self.updaterollentities)
        self.updatewindow.btn.grid(row=1, column=0)
    
    def updaterollentities(self):
        self.updatewindow.destroy()
        
        Update_entities()   
    
    #Find Record:
    def findrecord_fn(self):
        print(Students)
    
    # Delete Record:
    def deleterecord_fn(self):
        self.window.destroy()
        
        self.delwindow = Tk()
        self.delwindow.title("Delete Record")
        
        self.delwindow.find_roll_label = Label(text="Roll Number: ")
        self.delwindow.find_roll_label.grid(row=0, column=0)
        
        global del_roll
        del_roll = StringVar()
        self.delwindow.find_roll = Entry(master=self.delwindow, textvariable=del_roll)
        self.delwindow.find_roll.grid(row=0, column=1)
        
        self.delwindow.btn = Button(text="Find", command=self.deleteitem)
        self.delwindow.btn.grid(row=1, column=0)
        
    def deleteitem(self):
        Students.pop(del_roll.get())
        self.delwindow.destroy()
        
        DataBase()

class Update_entities:
    def __init__(self):
        self.update_item = Tk()
        self.update_item.title("Update Record")
        
        self.update_item.namebtn = Button(text="Name", command=self.updatename)
        self.update_item.namebtn.grid(row=0, column=0)
        
        self.update_item.agebtn = Button(text="Age", command=self.updateage)
        self.update_item.agebtn.grid(row=1, column=0)
        
        self.update_item.depbtn = Button(text="Department", command=self.updatedep)
        self.update_item.depbtn.grid(row=2, column=0)
        
        self.update_item.mainloop()
        
    def updatename(self):
        self.update_item.destroy()
        
        self.updateitem = Tk()
        self.updateitem.title("Update Record")
        
        self.updateitem.update_name_lbl = Label(text="Name: ")
        self.updateitem.update_name_lbl.grid(row=0, column=0)
        
        self.updateitem.update_name = Entry(master=self.updateitem, textvariable=StringVar())
        self.updateitem.update_name.grid(row=0, column=1)
        
        
        self.updateitem.update_btn = Button(text="Update", command=self.confirmname)
        self.updateitem.update_btn.grid(row=1, column=0)
        
    def confirmname(self):
        Students[find_roll.get()][0] = self.updateitem.update_name.get()
        self.updateitem.destroy()
        
        DataBase()
        
    def updateage(self):
        self.update_item.destroy()
        
        self.updateitem = Tk()
        self.updateitem.title("Update Record")
        
        self.updateitem.update_age_lbl = Label(text="Age: ")
        self.updateitem.update_age_lbl.grid(row=0, column=0)
        
        self.updateitem.update_age = Entry(master=self.updateitem, textvariable=StringVar())
        self.updateitem.update_age.grid(row=0, column=1)
        
        self.updateitem.update_btn = Button(text="Update", command=self.confirmnage)
        self.updateitem.update_btn.grid(row=1, column=0)
        
    def confirmnage(self):
        Students[find_roll.get()][1] = int(self.updateitem.update_age.get())
        self.updateitem.destroy()
        DataBase()
        
    def updatedep(self):
        self.update_item.destroy()
        
        self.updateitem = Tk()
        self.updateitem.title("Update Record")
        
        self.updateitem.update_dep_lbl = Label(text="Department: ")
        self.updateitem.update_dep_lbl.grid(row=0, column=0)
        
        self.updateitem.update_dep = Entry(master=self.updateitem, textvariable=StringVar())
        self.updateitem.update_dep.grid(row=0, column=1)
        
        self.updateitem.update_btn = Button(text="Update", command=self.confirmndep)
        self.updateitem.update_btn.grid(row=1, column=0)
        
    def confirmndep(self):
        Students[find_roll.get()][2] = self.updateitem.update_dep.get()
        self.updateitem.destroy()
        DataBase()

DataBase()