# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con = MongoClient("192.168.219.103")
print("success")

db = con.jinnieDB
yoil = input("요일 : ")
menu = input("뭐 먹음 : ")

db.menu2021.insert({"yoil":yoil, "menu":menu})

print("success")
con.close()