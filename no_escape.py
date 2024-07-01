import win32gui, win32com.client
from time import sleep

k=win32gui.FindWindow("ZPContentViewWndClass","Zoom Meeting")
shell = win32com.client.Dispatch("WScript.Shell")
while True:

    # print(k)
    shell.SendKeys('')
    try:
        win32gui.SetForegroundWindow(k)
    except:
        k=win32gui.FindWindow("ZPContentViewWndClass","Zoom Meeting")
        if k==0: exit()
        else: continue
    sleep(60)