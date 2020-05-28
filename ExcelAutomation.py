import win32com.client as win32


excel = win32.gencache.EnsureDispatch('Excel.Application')
excel.Visible = False
excel.DisplayAlerts = False

wb_data = excel.Workbooks.Open('C:\\Users\Walter Spears\\Downloads\RE__Operational_Metrics\\ATT Medium-Vitalsuite Raw data.csv')
wb_data.SaveAs(str('C:\\Users\Walter Spears\\Downloads\RE__Operational_Metrics\\Test.xlsx'))
