import win32api
import win32com.client
import pythoncom
win32api.MessageBox(0, 'hello', 'title')

result = win32api.MessageBox(None,"Do you want to open a file?", "title",1)

if result == 1:
 print ('Ok')
elif result == 2:
 print ('cancel')

win32api.MessageBox(0,"msgbox", "title")
win32api.MessageBox(0,"ok cancel?", "title",1)
win32api.MessageBox(0,"abort retry ignore?", "title",2)
win32api.MessageBox(0,"yes no cancel?", "title",3)
