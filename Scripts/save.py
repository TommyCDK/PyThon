import random
import os

a = "so "
b = 0

TileList = []
for c in range(10):
    TileList.insert(c,dict(name=str(a+str(c)), num=c))
for d in TileList:
    print(d["num"])
    print(type(len(TileList)))