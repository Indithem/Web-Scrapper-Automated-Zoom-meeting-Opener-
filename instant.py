import os, datetime, json
try:
    with open("data.json","r") as f:
        data = json.load(f)
    for i in data:
        if datetime.datetime.now()-datetime.datetime.fromisoformat(i[1])>datetime.timedelta(minutes=50):
            print(i[0]+" is completed")
            continue
        os.system( f'start zoommtg:"//zoom.us/join?confno={str(i[2]).replace(" ","")}&pwd={i[3]}"')
        os.system("py no_escape.py")
        exit()
except FileNotFoundError:
    os.system("py gets_html.py")
    os.system("py get_links.py")

with open("data.json","r") as f:
    data = json.load(f)

for i in data:
    if datetime.datetime.now()-datetime.datetime.fromisoformat(i[1])>datetime.timedelta(minutes = 50):
        print(i[0]+" is completed")
        continue
    os.system( f'start zoommtg:"//zoom.us/join?confno={str(i[2]).replace(" ","")}&pwd={i[3]}&uname=Sai%20Srinivas%20F22"')
    os.system("py no_escape.py")
    break