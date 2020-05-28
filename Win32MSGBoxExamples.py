##pip install pywin32
import win32api, win32con

## OKOK message box
win32api.MessageBox(0, "This is a test reminder OK message box", "Reminder", win32con.MB_OK)

##
win32api.MessageBox(0, "This is a test if the message box", "Reminder", win32con.MB_YESNO)

##
win32api.MessageBox(0, "This is a test description message box", "Reminder", win32con.MB_HELP)

####Warning message box
win32api.MessageBox(0, "This is a test warning message box", "Reminder", win32con.MB_ICONWARNING)

##
win32api.MessageBox(0, "This is a test question message box", "Reminder", win32con.MB_ICONQUESTION)

##
win32api.MessageBox(0, "This is a test prompt message box", "Reminder", win32con.MB_ICONASTERISK)

##Confirm message box
win32api.MessageBox(0, "This is a test confirmation message box", "Reminder", win32con.MB_OKCANCEL)

##Retry message box
win32api.MessageBox(0, "This is a test retry message box", "Reminder", win32con.MB_RETRYCANCEL)

##Do you want to cancel the message box?
win32api.MessageBox(0, "This is a test whether to cancel the message box", "Reminder", win32con.MB_YESNOCANCEL)