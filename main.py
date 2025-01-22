from tkinter import *
from tkinter import messagebox, simpledialog
import json

FONT1 = ('Roboto', 18, 'normal')
WINBG = "Light Yellow"
Students = {}

class DataBase:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Student DataBase")
        self.window.config(padx=40, pady=40, bg=WINBG)
        
        self.window.newrecord = Button(text="New Record", font=FONT1, command=self.newrecord_fn, bd=5, bg="Light Green")
        self.window.newrecord.grid(row=0, column=0, padx=40, pady=40)
        
        self.window.updaterecord = Button(text="Update Record", font=FONT1, command=self.updaterecord_fn, bd=5, bg="Light Blue")
        self.window.updaterecord.grid(row=0, column=1, padx=40, pady=40)
        
        self.window.findrecord = Button(text="All Records", font=FONT1, command=self.findrecord_fn, bd=5, bg="Light Blue")
        self.window.findrecord.grid(row=1, column=0, padx=40, pady=40)

        self.window.deleterecord = Button(text="Delete Record", font=FONT1, command=self.deleterecord_fn, bd=5, bg="Light Green")
        self.window.deleterecord.grid(row=1, column=1, padx=40, pady=40)
        
        
        self.window.mainloop()
        
    # New Record:
    def newrecord_fn(self):
        self.window.destroy()
        
        self.newwindow = Tk()
        self.newwindow.title("New Record")
        self.newwindow.config(padx=50, pady=50, bg=WINBG)
        
        # Student Roll Number
        self.newwindow.stu_roll_label = Label(text="Roll Number: ", font=FONT1, bg=WINBG, highlightthickness=0)
        self.newwindow.stu_roll_label.grid(row=0, column=0, pady=10)
        
        get_roll = StringVar()
        self.newwindow.stu_roll = Entry(master=self.newwindow, textvariable=get_roll, font=FONT1)
        self.newwindow.stu_roll.grid(row=0, column=1, pady=10)
        self.newwindow.stu_roll.focus()
        
        # Student Name 
        self.newwindow.stu_name_label = Label(text="Name: ", font=FONT1, bg=WINBG, highlightthickness=0)
        self.newwindow.stu_name_label.grid(row=1, column=0, pady=10)
        
        get_name = StringVar()
        self.newwindow.stu_name = Entry(master=self.newwindow, textvariable=get_name, font=FONT1)
        self.newwindow.stu_name.grid(row=1, column=1, pady=10)
        
        # Student Age
        self.newwindow.stu_age_label = Label(text="Age: ", font=FONT1, bg=WINBG, highlightthickness=0)
        self.newwindow.stu_age_label.grid(row=2, column=0, pady=10)
        
        get_age = IntVar()
        self.newwindow.stu_age = Entry(master=self.newwindow, textvariable=get_age, font=FONT1)
        self.newwindow.stu_age.grid(row=2, column=1, pady=10)
        
        # Student Department
        self.newwindow.stu_dep_label = Label(text="Department: ",font=FONT1, bg=WINBG, highlightthickness=0)
        self.newwindow.stu_dep_label.grid(row=3, column=0, pady=10)
        
        get_dep = StringVar()
        self.newwindow.stu_dep = Entry(master=self.newwindow, textvariable=get_dep, font=FONT1)
        self.newwindow.stu_dep.grid(row=3, column=1, pady=10)
        
        self.newwindow.btn = Button(text="Add", command=self.confirmrecord, font=FONT1, width=18, bg="Light Green", bd=5)
        self.newwindow.btn.grid(row=4, column=1, pady=30)
        
    # Confirm Add Record:
    def confirmrecord(self):
        Students.update({self.newwindow.stu_roll.get(): [self.newwindow.stu_name.get(), int(self.newwindow.stu_age.get()), self.newwindow.stu_dep.get()]})
        
        global new_data
        new_data = {
            self.newwindow.stu_roll.get(): [
                self.newwindow.stu_name.get(), 
                int(self.newwindow.stu_age.get()), 
                self.newwindow.stu_dep.get()
            ]
        }
        
        # Date Storing
        try:
            with open('records.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
        
        except FileNotFoundError:
            with open('records.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
            
        else:
            data.update(new_data)
            
            with open('records.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        
        self.newwindow.destroy()
        DataBase()    
        
    # Update Record:
    def updaterecord_fn(self):
        self.window.destroy()
        
        self.updatewindow = Tk()
        self.updatewindow.title("Update Record")
        self.updatewindow.config(padx=40, pady=40, bg=WINBG)
        
        self.updatewindow.find_roll_label = Label(text="Roll Number: ", font=FONT1, bg=WINBG, highlightthickness=0)
        self.updatewindow.find_roll_label.grid(row=0, column=0, pady=10)
        
        global find_roll
        find_roll = StringVar()
        self.updatewindow.find_roll = Entry(master=self.updatewindow, textvariable=find_roll, font=FONT1)
        self.updatewindow.find_roll.grid(row=0, column=1, pady=10)
        
        self.updatewindow.btn = Button(text="Find", command=self.updaterollentities, font=FONT1, width=18, bg="Light Green", bd=5)
        self.updatewindow.btn.grid(row=1, column=1, pady=30)
    
    def updaterollentities(self):
        self.updatewindow.destroy()
        
        Update_entities()   
    
    #Find Record:
    def findrecord_fn(self):
        self.window.destroy()
        
        self.findwindow = Tk()
        self.findwindow.title("Student Records")
        self.findwindow.config(padx=20, pady=20, bg="Light Blue")
        
        # Create a Canvas to hold the table
        canvas = Canvas(self.findwindow, bg="Light Yellow", width=730, height=350)
        canvas.pack(side="left", fill="both", expand=True)
    
        # Add a vertical scrollbar
        scrollbar = Scrollbar(self.findwindow, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
    
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
        # Create a frame inside the canvas
        frame = Frame(canvas, bg="Light Yellow")
        canvas.create_window((0, 0), window=frame, anchor="nw")
    
        # Create the header row
        Label(frame, text="ROLL NO", borderwidth=1, relief="solid", width=14, height=2, bg="Light Green", font=("Roboto", 15, 'bold')).grid(row=0, column=0, padx=5, pady=5)
        for col, header in enumerate(["NAME", "AGE", "DEPARTMENT"], start=1):
            Label(frame, text=header, borderwidth=1, relief="solid", width=14, height=2, bg="Light Green", font=("Roboto", 15, 'bold')).grid(row=0, column=col, padx=5, pady=5)
    
        # Display the dictionary in the grid
        for row, (key, values) in enumerate(Students.items(), start=1):
            # Add the row header (key)
            Label(frame, text=key, borderwidth=1, relief="solid", width=14, height=2, font=("Roboto", 13, 'normal')).grid(row=row, column=0, padx=5, pady=5)
            
            # Add the list values as columns
            for col, value in enumerate(values, start=1):
                Label(frame, text=str(value), borderwidth=1, relief="solid", width=14, height=2, font=("Roboto", 13, 'normal')).grid(row=row, column=col, padx=5, pady=5)
    
        # Add mousewheel for scrolling
        def on_mouse_wheel(event):
            canvas.yview_scroll(-1 * int(event.delta / 120), "units")
    
        canvas.bind_all("<MouseWheel>", on_mouse_wheel)
        
        self.findwindow.mainloop()
        DataBase()
        
    # Delete Record:
    def deleterecord_fn(self):
        self.window.destroy()
        
        self.delwindow = Tk()
        self.delwindow.title("Delete Record")
        self.delwindow.config(padx=40, pady=40, bg=WINBG)
        
        self.delwindow.find_roll_label = Label(text="Roll Number: ", font=FONT1, bg=WINBG, highlightthickness=0)
        self.delwindow.find_roll_label.grid(row=0, column=0, pady=10)
        
        global del_roll
        del_roll = StringVar()
        self.delwindow.find_roll = Entry(master=self.delwindow, textvariable=del_roll, font=FONT1)
        self.delwindow.find_roll.grid(row=0, column=1, pady=10)
        
        self.delwindow.btn = Button(text="Delete", command=self.deleteitem, font=FONT1, width=18, bg="Light Green", bd=5)
        self.delwindow.btn.grid(row=1, column=1, pady=30)
        
    def deleteitem(self):
        roll = del_roll.get()

        # Remove from the Students dictionary.
        if roll in Students:
            Students.pop(roll)
        else:
            messagebox.showinfo(title="Warning", message="Roll Not Found!")

        # Update the JSON records.
        try:
            with open('records.json', 'r') as data_file:
                data = json.load(data_file)

            if roll in data:
                data.pop(roll)
                # Save the updated data back to the file.
                with open('records.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            else:
                pass

        except FileNotFoundError:
            messagebox.showerror(title= "Warning", message="File Not Found!")

        self.delwindow.destroy()
        DataBase() 
        

class Update_entities:
    def __init__(self):
        self.update_item = Tk()
        self.update_item.title("Update Record")
        self.update_item.config(padx=60, pady=30, bg=WINBG)
        
        self.update_item.namebtn = Button(text="Name", command=self.updatename, font=FONT1, bg="Light Green", bd=5)
        self.update_item.namebtn.grid(row=0, column=0, pady=25)
        
        self.update_item.agebtn = Button(text="Age", command=self.updateage, font=FONT1, bg="Light Blue", bd=5)
        self.update_item.agebtn.grid(row=1, column=0, pady=25)
        
        self.update_item.depbtn = Button(text="Department", command=self.updatedep, font=FONT1, bg="Light Green", bd=5)
        self.update_item.depbtn.grid(row=2, column=0, pady=25)
        
        self.update_item.mainloop()
        
    def updatename(self):
        self.update_item.destroy()
        
        self.updateitem = Tk()
        self.updateitem.title("Update Record")
        self.updateitem.config(padx=30, pady=30, bg=WINBG)
        
        self.updateitem.update_name_lbl = Label(text="Name: ", font=FONT1, bg=WINBG, highlightthickness=0)
        self.updateitem.update_name_lbl.grid(row=0, column=0, pady=10)
        
        self.updateitem.update_name = Entry(master=self.updateitem, textvariable=StringVar(), font=FONT1)
        self.updateitem.update_name.grid(row=0, column=1, pady=10)
        
        
        self.updateitem.update_btn = Button(text="Update", command=self.confirmname, font=FONT1, width=18, bg="Light Green", bd=5)
        self.updateitem.update_btn.grid(row=1, column=1, pady=30)
        
    def confirmname(self):
        Students[find_roll.get()][0] = self.updateitem.update_name.get()
        self.updateitem.destroy()
        
        DataBase()
        
    def updateage(self):
        self.update_item.destroy()
        
        self.updateitem = Tk()
        self.updateitem.title("Update Record")
        self.updateitem.config(padx=30, pady=30, bg=WINBG)
        
        self.updateitem.update_age_lbl = Label(text="Age: ", font=FONT1, bg=WINBG, highlightthickness=0)
        self.updateitem.update_age_lbl.grid(row=0, column=0, pady=10)
        
        self.updateitem.update_age = Entry(master=self.updateitem, textvariable=StringVar(), font=FONT1)
        self.updateitem.update_age.grid(row=0, column=1, pady=10)
        
        self.updateitem.update_btn = Button(text="Update", command=self.confirmnage, font=FONT1, width=18, bg="Light Green", bd=5)
        self.updateitem.update_btn.grid(row=1, column=1, pady=30)
        
    def confirmnage(self):
        Students[find_roll.get()][1] = int(self.updateitem.update_age.get())
        self.updateitem.destroy()
        DataBase()
        
    def updatedep(self):
        self.update_item.destroy()
        
        self.updateitem = Tk()
        self.updateitem.title("Update Record")
        self.updateitem.config(padx=30, pady=30, bg=WINBG)
        
        self.updateitem.update_dep_lbl = Label(text="Department: ", font=FONT1, bg=WINBG, highlightthickness=0)
        self.updateitem.update_dep_lbl.grid(row=0, column=0, pady=10)
        
        self.updateitem.update_dep = Entry(master=self.updateitem, textvariable=StringVar(), font=FONT1)
        self.updateitem.update_dep.grid(row=0, column=1, pady=10)
        
        self.updateitem.update_btn = Button(text="Update", command=self.confirmndep, font=FONT1, width=18, bg="Light Green", bd=5)
        self.updateitem.update_btn.grid(row=1, column=1, pady=30)
        
    def confirmndep(self):
        Students[find_roll.get()][2] = self.updateitem.update_dep.get()
        self.updateitem.destroy()
        DataBase()

DataBase()