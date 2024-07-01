import os,json, logging
import datetime, time
from tkinter import messagebox
import tkinter
# import ctypes, asyncio

logging.basicConfig(filename="log.log",format="[%(asctime)s] %(filename)s %(levelname)s %(message)s",level=logging.INFO)
logging.info("Main started")
time.sleep(30)
need_files = False
try:
    with open("data.json","r") as f:
        data = json.load(f)
except FileNotFoundError:
    logging.warning("No data.json!")
    need_files= True


try:
    if not need_files:
        if all([datetime.datetime.fromisoformat(i[1])+datetime.timedelta(hours=1)<datetime.datetime.now() for i in data]):
            logging.info("Need new files")
            need_files =True        
except:
    if not need_files:logging.warning("something fishy! at loading past data.json")
    need_files = True
if need_files:

    # check if today is sunday
    if datetime.datetime.today().weekday() == 6:
        logging.warn("exiting, as today is Sunday")
        exit()

    os.system("python gets_html.py")
    logging.info("got html")
    os.system("python get_links.py")
    logging.info("loaded links, hopefully...")
    with open("data.json","r") as f:
        data = json.load(f)

del need_files, json

def popup(msg:str):
    print("popup start")
    root = tkinter.Tk()
    root.withdraw()
    root.after(600_000,root.destroy)
    messagebox.showinfo("Next Class!",msg)

# async def popup(msg:str):             
#     # HWND, lpText:msg, lpCaption:title, uType
#     await ctypes.windll.user32.MessageBoxW(0, msg, 'Next Class!', 0x1000)


for i in data:
    wait=datetime.datetime.now()-datetime.datetime.fromisoformat(i[1])
    if wait>datetime.timedelta(hours=1):
        print(i[0]+" "+i[1]+" is outdated")
        continue
    else:
        # following code executes when need to sleep

        logging.info("loading "+i[0]+" at "+i[1])
        # wait <0
        # popup only if class is in >15 min in future
        # -------wait------(-15)------0----------------
        # like that, wait < -15
        # (popup(f"Next class{ i[0]} at {datetime.datetime.fromisoformat(i[1])}")) if wait<-datetime.timedelta(minutes=15) else None
        # print("popup succeesfull")
        wait=datetime.datetime.now()-datetime.datetime.fromisoformat(i[1])
        logging.info("sleeping for "+ str(-1*min(-1,wait.total_seconds()+90)))
        time.sleep(-1*min(-1,wait.total_seconds()+90))  
    while "No tasks are running" not in os.popen('tasklist /fi "imagename eq CptHost.exe"').read():
        time.sleep(30)
        #logging.info("waiting to over")   
    os.system( f'start zoommtg:"//zoom.us/join?confno={str(i[2]).replace(" ","")}&pwd={i[3]}&uname=Sai%20Srinivas%20F22"')
    logging.info(f'start zoommtg:"//zoom.us/join?confno={str(i[2]).replace(" ","")}&pwd={i[3]}&uname=Sai%20Srinivas%20F22"')

    # code to make no_escape.py
        # skip = False
        # while "No tasks are running" in os.popen('tasklist /fi "imagename eq CptHost.exe"').read():
        #     time.sleep(30)
        #     print("waiting to start")
        #     if datetime.datetime.now()-datetime.datetime.fromisoformat(i[1])>datetime.timedelta(minutes=20):
        #         skip = True
        #         break
        # if not skip: os.system("python no_escape.py")

logging.info("Bye Bye")