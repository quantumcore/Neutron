import os

try:
    import requests
except ImportError:
    print("requests not found. Install requests and Re run.")
    exit(1)
    
from tkinter import *
from tkinter import messagebox
import webbrowser

def showError(errormessage):
    """ Show an Error MessageBox """
    messagebox.showerror("Neutron", errormessage)

def showInfo(infomessage):
    """ Show an Information MessageBox """
    messagebox.showinfo("Neutron", infomessage)

def showWarning(warning):
    """ Show an Information MessageBox """
    messagebox.showwarning("Neutron", warning)

def clear_screen():
    """ Clear the Screen """
    os.system("clear")


def check_for_update():
    """ Check for Updates """
    print("Checking for updates")
    try:
        data = requests.get("https://raw.githubusercontent.com/Fahad-M/Neutron/master/update.md")
        status = data
        if(status == "Update-Available"):
            ask = messagebox.askquestion("Neutron", "A new Version of Neutron is available. Update?")
            if(ask == "yes"):
                webbrowser.open_new("https://github.com/Fahad-M/Neutron")
            else:
                showInfo("Returning. It is recommended to update later.")
                
    except requests.Timeout:
        status = "Internet Slow or not available"
    except Exception as e:
        status =  "Unknown error occured : " + str(e)
        
    return status.content

        

