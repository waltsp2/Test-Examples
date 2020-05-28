from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "C:\\Users\\Walter Spears\\Downloads\\RE__Operational_Metrics",title = "Select file",filetypes = (("all files","*.*"),("CSV files","*.csv"),("Excell Files",".xlsx"),("Excell Files",".xls")))
print (root.filename)