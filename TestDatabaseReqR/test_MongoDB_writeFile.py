# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con = MongoClient("192.168.219.103")
print("success")

db = con.jinnieDB

menuData = db.menu2021.find()

f = open("D:/ai_data/menu2021.txt", "a", encoding="utf-8")
for m in menuData:
    f.write(m["yoil"] + " ")
    f.write(m["menu"] + "\n")

print("end")
f.close()
con.close()