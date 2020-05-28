import win32ui
import os



open = win32ui.CreateFileDialog( 1, ".xlsx", None, 0, "Excel Files (*.xlsx)|*.xlsx|CSV Files (*.csv)|*.csv|All Files (*.*)|*.*|")
open.SetOFNTitle("Open Source Metric .CSV")
open.DoModal()
wb1=(open.GetFileName())
wb2=(open.GetPathName())
wb2a = (os.path.split(wb2))
wb2b = (os.path.splitext(wb2))
wb2c = (os.path.splitdrive(wb2))
wb2d = (os.path.normpath(wb2).lstrip(os.path.sep).split(os.path.sep))

print (wb2a)
print (len(os.path.split(wb2)))
print (wb2b)
print (len(os.path.splitext(wb2)))
print (wb2c)
print (len(os.path.splitdrive(wb2)))
print (wb2d)
print (len(os.path.normpath(wb2).lstrip(os.path.sep).split(os.path.sep)))