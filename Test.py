import os
from tkinter import filedialog
from tkinter import *
import subprocess
from tkinter import messagebox

print ("Changing Directory")
#os.chdir('C:\\Users\\Walter Spears\\Downloads\\RE__Operational_Metrics')
workbook = Tk()
workbook.filename =  filedialog.askopenfilename(initialdir = "C:/Users/Walter Spears/PycharmProjects/Metrics",title = "Select file",filetypes = (("all files","*.*"),("CSV files","*.csv"),("Excell Files",".xlsx"),("Excell Files",".xls")))
print (workbook.filename)

messagebox.showinfo("Instructions", "Opening Excel, Save the file as .XLSX")
subprocess.call(["excel.exe", workbook.filename])
messagebox.showinfo("File Conversion Completed", "Moving on to the net phase")
