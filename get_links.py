from bs4 import BeautifulSoup
import datetime, logging, re

logging.basicConfig(filename="log.log",format="[%(asctime)s] %(filename)s %(levelname)s %(message)s",level=logging.INFO)
logging.info("Getting the html")
with open("WhatsApp.html",'r',encoding='utf-8') as f:
    text = BeautifulSoup(f,'html.parser').get_text("HEADER")

def get_time(s:str):
    for format in ["%b %d, %Y %I:%M %p","%d-%b-%y, from %H:%M"]:
        try:
            return str(datetime.datetime.strptime(s,format))
        except ValueError:
            continue
    """try:
        return str(datetime.datetime.strptime(s,"%b %d, %Y %I:%M %p"))
    except ValueError:
        return datetime.datetime.strptime(s,"%d-%b-%y, from %H:%M")"""
        
patterns = [
###################
r""" is inviting you to a scheduled Zoom meeting\.

Topic: (?P<topic>.*)
Time: (?P<time>.{21})

.*
.*

Meeting ID: (?P<ID>.*)
Passcode: (?P<passcode>.{6})""",
# Passcode: (?P<passcode>(\d*))
######################
r"""[\s]+You have a class on (?P<time>.*) to
[\s]+(\d|:)+ on the Topic (?P<topic>.*)

.*

\s+Meeting Id . (?P<ID>.*)
\s+Password . \s?(?P<passcode>\d*)"""
######################
]
logging.info("Doing the new recipe")
data = []

for pattern in patterns:
    matches = re.finditer(pattern,text)
    for match in matches:
        data.append([match.group("topic"),get_time(match.group("time")),int(match.group("ID").replace(" ","")),match.group("passcode")])
        #print(match.group("time"),match.group("topic"),match.group("ID"),match.group("passcode"))


data.sort(key=lambda i:i[1])
b=[]
[b.append(i) for i in data if i not in b]
# data = []
# for n,link in enumerate(b):
#     data.append([])
#     data[n]=[]
#     for i in link:
#         data[n].append(str(i))
print(data)
logging.info("Storing the results")
import json
with open("data.json",'w+') as g:
    json.dump(b,g)

import os
os.remove("WhatsApp.html")