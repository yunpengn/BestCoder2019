import numpy as np
import pandas as pd
import sklearn
import matplotlib

df = pd.read_csv("./undrg-rd1-listings/train.csv")

hashmap = {}
with open ("./undrg-rd1-listings/train.csv", "r") as f:
    f.readline()
    for line in f:
        split = list(line.split(","))
        id = int(split[0])
        for i in range(1,len(split)):
            name = split[i].replace("\"", "").strip()
            hashmap[name] = id


print(hashmap)