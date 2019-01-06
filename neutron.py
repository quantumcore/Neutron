import neutron_core
from neutron_core import clear_screen
from neutron_core import showInfo
try:
    import tkinter
except ImportError:
    print("Tkinter not found. Install tkinter and Re run.")
    exit(1)
    
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os, subprocess

class GUI:
    def __init__(self, master):

        def create_file(file):

            def askToRun():
                question = messagebox.askquestion("Neutron", "File is Compiled. Would you like to Run it now using Wine?")
                if(question == "yes"):
                    print("==================================")
                    print("Running your FILE")
                    print("==================================")
                    os.system("wine " + file + ".exe")
                else:
                    showInfo("Not Running.")

            os.system("i686-w64-mingw32-g++ -o " + file + ".exe " + file + " --static")

            self.output = Entry(master, bg="gray9", fg="green", bd="1", width=30)
            self.output.configure(font=("monospace", 10))
            self.output.pack()

            try:
                test = open(file+".exe")
                self.output.insert(0,"Compilation Succeded!")
                askToRun()
                
            except FileNotFoundError:
                self.output.insert(0,"Compilation Failed!")

            

        self.master = master
        self.img = tkinter.PhotoImage(file = r'neutron.png')
        self.master.tk.call('wm', 'iconphoto', self.master._w, self.img)

        self.heading = Label(master, text="Neutron", fg="cornflowerblue", bg="gray9")
        self.heading.configure(font=("fixedsys", 30))
        self.heading.pack()

        self.update = Label(master, text="Version 2", fg="light cyan", bg="gray9")
        self.update.configure(font=("fixedsys", 8))
        self.update.pack()

        self.browse = Label(master, text="Select File to Compile",  fg="purple", bg="gray9")
        self.browse.configure(font=("fixedsys", 8))
        self.browse.pack()

        self.path = Entry(master, width = 25)
        self.path.configure(font=("monospace", 8))
        self.path.pack()

        self.create = Label(master, text="Ready to Compile", fg="cornflowerblue", bg="gray9")
        self.create.configure(font=("monospace", 8))
        
        self.comButton = Button(master, text="Compile", fg="dodgerblue", bg="gray9", bd="1", command = lambda: create_file(self.file.name))
        self.comButton.configure(font=("fixedsys", 8))

        def Browse():
            self.file = filedialog.askopenfile(mode="r+")
            try:
                self.path.insert(0, self.file.name)
            except AttributeError:
                print("Attribute Error. Maybe you pressed Cancel.")
            
            self.create.pack()
            self.comButton.pack()



        self.ButtonBrowse = Button(master, text="Browse", fg="dodgerblue", bg="gray9", bd="1", command= lambda: Browse())
        self.ButtonBrowse.configure(font=("fixedsys", 8))
        self.ButtonBrowse.pack()

def main():
    clear_screen()

    root = Tk()
    root.title("Neutron")
    root.configure(background="gray9")
    root.geometry("500x300")
    root.pack_propagate(0)
    app = GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
    
