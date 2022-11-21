import pandas as pd
import numpy as np

path = "DB-Output_original.csv"

data = pd.read_csv(path)
data = data[:9000] # posso ridurre da 35mila a 9mila senza perdere i luoghi, velocizzando l'esecuzione
data = data.loc[:, :'Moves']

init_sol = data['Initial Solution']

sol = []
for row in init_sol:
    for elem in row.split("'], "):
        sol.append(elem)
        
for i in range(len(sol)):
    sol[i] = sol[i].replace("[['","")
    sol[i] = sol[i].replace("']]","")
    sol[i] = sol[i].replace("'","")
    sol[i] = sol[i].replace(",","")
    sol[i] = sol[i].replace("[","")
    
data["Initial Solution"] = data["Initial Solution"].str.replace("[","")
data["Initial Solution"] = data["Initial Solution"].str.replace("]","")
data["Initial Solution"] = data["Initial Solution"].str.replace(",","")
data["Initial Solution"] = data["Initial Solution"].str.replace("'","")

init_sol = data["Initial Solution"]

places = []
for row in init_sol:
    for elem in row.split():
        places.append(elem)
        
places = np.array(places)
distinct_places = np.unique(places)

d = {}

for index, elem in enumerate(sol):
        zeros = np.zeros([len(distinct_places), len(distinct_places)])
        d[index] = pd.DataFrame(zeros, index=distinct_places, columns=distinct_places)
        
for index, stringa in enumerate(sol):
 
    temp = stringa
    
    split = temp.split(" ")                         
    split = np.array(split)
    
    for i in range(len(split)-1):
            d[index].loc[split[i], split[i+1]] = 1
    
    
for i in range(len(dict)):
    dict[i] = dict[i].to_numpy()