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


def repository_status():
    print("Fetching Status")
    status = requests.get("https://raw.githubusercontent.com/Fahad-M/Neutron/master/status.md")
    data = status.content
    return data
