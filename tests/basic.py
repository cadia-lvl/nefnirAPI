# -*- coding: utf-8 -*-
import requests
import json

LOC="/lemmatizer"
LOC="/process/service"

inp = 'Hvað fshen var sfg3eþ þetta fahen ? ? Maðurinn nkeng leit sfg3eþ upp aa frá aþ verkinu nheþg . .'
print("INP:",inp)
r = requests.post("http://localhost:8080"+LOC, json={"type":"text","content":inp})
print("OUT:",r.content.decode("utf-8"))
json.loads(r.content.decode("utf-8"))
print()


1/0
