import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=True)
        self.master.geometry('{}x{}'.format(500,210))
        self.master.title('Check files')
        self.master.config(bg='lightgray')  #can also you #000 basically pound and three numbers for a specific color

        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()

        
        self.txtBrowse1 = Entry(self.master,text=self.varBrowse1,font=("Helvetica",16), fg='black' ,bg="white")
        self.txtBrowse1.grid(row=2,column=2,padx=(30,0), pady=(30,0),columnspan=9) # pack manager is another way to place fields anywhere

        self.txtBrowse2 = Entry(self.master,text=self.varBrowse2,font=("Helvetica",16), fg='black', bg="white")
        self.txtBrowse2.grid(row=3,column=2,padx=(30,0), pady=(10,0),columnspan=9)

        self.btnBrowse1 = Button(self.master, text="Browse...", width = 20, height = 2)
        self.btnBrowse1.grid(row=2,column=1,padx=(20,20), pady=(30,0), sticky=NE)

        self.btnBrowse2 = Button(self.master, text="Browse...", width = 20, height = 2)
        self.btnBrowse2.grid(row=3,column=1,padx=(20,20), pady=(10,0), sticky=NE)

        self.btnCheck = Button(self.master, text="Check for files...", width = 20, height = 2)
        self.btnCheck.grid(row=4,column=1,padx=(20,20), pady=(30,0), sticky=NE)

        self.btnClose = Button(self.master, text="Close Program", width = 20, height = 2)
        self.btnClose.grid(row=4,column=10,padx=(0,0), pady=(30,0), sticky=NE)






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()   #This line of code keeps the window from closing immediatly after you run the program
