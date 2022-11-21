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


# creo un dizionario  
d = {}

for index, elem in enumerate(sol):
        zeros = np.zeros([len(distinct_places), len(distinct_places)])
        d[index] = pd.DataFrame(zeros, index=distinct_places, columns=distinct_places)
        
for index, stringa in enumerate(soll):
    
    # si prende la stringa i-esima e la si mette in una variabile temporanea quindi temp diventerà percorso 1, percorso 2, ecc
    
    temp = stringa
    print(temp)
    
    # si splitta la variabile temp secondo il carattere spazio, inserendola in una variabile chiamata split (che sarà una lista), 
    # in modo da avere ad esempio split[0] = D0, split[1] = C21, ecc 
    
    split = temp.split(" ")                         
    
    # si prendono i singoli luoghi che servono a costruire la matrice di ogni percorso all'interno del vettore precedente,
    # quindi avrò unique = ["C21", "C26", "D0"] (ordinata con sort)
    
    split = np.array(split)
    
    for i in range(len(split)-1):
            d[index].loc[split[i], split[i+1]] = 1
    print(d)