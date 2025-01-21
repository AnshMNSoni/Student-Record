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
        self.newwindow.config(padx=50, pady=50)
        
        # Student Roll Number
        self.newwindow.stu_roll_label = Label(text="Roll Number: ", font=FONT1)
        self.newwindow.stu_roll_label.grid(row=0, column=0, pady=10)
        
        get_roll = StringVar()
        self.newwindow.stu_roll = Entry(master=self.newwindow, textvariable=get_roll, font=FONT1)
        self.newwindow.stu_roll.grid(row=0, column=1, pady=10)
        self.newwindow.stu_roll.focus()
        
        # Student Name 
        self.newwindow.stu_name_label = Label(text="Name: ", font=FONT1)
        self.newwindow.stu_name_label.grid(row=1, column=0, pady=10)
        
        get_name = StringVar()
        self.newwindow.stu_name = Entry(master=self.newwindow, textvariable=get_name, font=FONT1)
        self.newwindow.stu_name.grid(row=1, column=1, pady=10)
        
        # Student Age
        self.newwindow.stu_age_label = Label(text="Age: ", font=FONT1)
        self.newwindow.stu_age_label.grid(row=2, column=0, pady=10)
        
        get_age = IntVar()
        self.newwindow.stu_age = Entry(master=self.newwindow, textvariable=get_age, font=FONT1)
        self.newwindow.stu_age.grid(row=2, column=1, pady=10)
        
        # Student Department
        self.newwindow.stu_dep_label = Label(text="Department: ",font=FONT1)
        self.newwindow.stu_dep_label.grid(row=3, column=0, pady=10)
        
        get_dep = StringVar()
        self.newwindow.stu_dep = Entry(master=self.newwindow, textvariable=get_dep, font=FONT1)
        self.newwindow.stu_dep.grid(row=3, column=1, pady=10)
        
        self.newwindow.btn = Button(text="Add", command=self.confirmrecord, font=FONT1, width=18)
        self.newwindow.btn.grid(row=4, column=1, pady=30)
        
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
        self.updatewindow.config(padx=40, pady=40)
        
        self.updatewindow.find_roll_label = Label(text="Roll Number: ", font=FONT1)
        self.updatewindow.find_roll_label.grid(row=0, column=0, pady=10)
        
        global find_roll
        find_roll = StringVar()
        self.updatewindow.find_roll = Entry(master=self.updatewindow, textvariable=find_roll, font=FONT1)
        self.updatewindow.find_roll.grid(row=0, column=1, pady=10)
        
        self.updatewindow.btn = Button(text="Find", command=self.updaterollentities, font=FONT1, width=18)
        self.updatewindow.btn.grid(row=1, column=1, pady=30)
    
    def updaterollentities(self):
        self.updatewindow.destroy()
        
        Update_entities()   
    
    #Find Record:
    def findrecord_fn(self):
        self.window.destroy()
        
        self.findwindow = Tk()
        self.findwindow.title("Student Records")
        self.findwindow.config(padx=20, pady=20)
        
        
        # Create the header row
        self.findwindow.lbl1 = Label(text="ROLL NO", borderwidth=1, relief="solid", width=12, height=2).grid(row=0, column=0, padx=5, pady=5)
        
        for col, header in enumerate(["NAME", "AGE", "DEPARTMENT"], start=1):
            self.findwindow.lbl2 = Label(text=header, borderwidth=1, relief="solid", width=12, height=2).grid(row=0, column=col, padx=5, pady=5)
        
        # Display the dictionary in the grid
        for row, (key, values) in enumerate(Students.items(), start=1):
            # Add the row header (key)
            self.findwindow.lbl3 = Label(text=key, borderwidth=1, relief="solid", width=12, height=2).grid(row=row, column=0, padx=5, pady=5)
            
            # Add the list values as columns
            for col, value in enumerate(values, start=1):
                self.findwindow.lbl3 = Label(text=str(value), borderwidth=1, relief="solid", width=12, height=2).grid(row=row, column=col, padx=5, pady=5)
                        
        self.findwindow.mainloop()
    
    # Delete Record:
    def deleterecord_fn(self):
        self.window.destroy()
        
        self.delwindow = Tk()
        self.delwindow.title("Delete Record")
        self.delwindow.config(padx=40, pady=40)
        
        self.delwindow.find_roll_label = Label(text="Roll Number: ", font=FONT1)
        self.delwindow.find_roll_label.grid(row=0, column=0, pady=10)
        
        global del_roll
        del_roll = StringVar()
        self.delwindow.find_roll = Entry(master=self.delwindow, textvariable=del_roll, font=FONT1)
        self.delwindow.find_roll.grid(row=0, column=1, pady=10)
        
        self.delwindow.btn = Button(text="Find", command=self.deleteitem, font=FONT1, width=18)
        self.delwindow.btn.grid(row=1, column=1, pady=30)
        
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