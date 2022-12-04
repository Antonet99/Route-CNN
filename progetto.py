import pandas as pd
import numpy as np

path = "DB-Output_original.csv"
data = pd.read_csv(path)
data = data.loc[:, ['Initial Solution', 'Moves']]

mv = data["Moves"]
moves = []
for row in mv:
    for elem in row.split("', '"):
        moves.append(elem)

for i in range(len(moves)):
    moves[i] = moves[i].replace("['","")
    moves[i] = moves[i].replace("']","")

to_remove = "null"
moves = list(filter(lambda x: x != to_remove, moves))

moves=list(set(moves))
print("Lista delle", len(moves), "possibili e diverse mosse: \n", moves)

data["Moves"] = data["Moves"].str.replace("[","")
data["Moves"] = data["Moves"].str.replace("]","")
data["Moves"] = data["Moves"].str.replace("'","")

user_input = input("Inserisci una stringa: ")
data = data.loc[data['Moves'].str.contains(user_input)]

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

dict = {}
for index, elem in enumerate(sol):
        zeros = np.zeros([len(distinct_places), len(distinct_places)])
        dict[index] = pd.DataFrame(zeros, index=distinct_places, columns=distinct_places)

for index, stringa in enumerate(sol):
    
    temp = stringa
    
    split = temp.split(" ")                         
    split = np.array(split)
    
    for i in range(len(split)-1):
            dict[index].loc[split[i], split[i+1]] = 1

# inizializzo il risultato come il primo dataframe del dizionario
df_sum = dict[0]

# itero su tutti gli altri dataframe del dizionario
for i in range(1, len(dict)):
    # sommo il dataframe corrente al risultato
    df_sum = df_sum.add(dict[i])
    
df_sum.to_csv(user_input)

for i in range(len(dict)):
    dict[i] = dict[i].to_numpy()

# Inizializzo una variabile per memorizzare il risultato
result = None

# Creo un ciclo che iteri sulla lista di matrici
for matrix in dict.values():
    # Se è il primo ciclo, il risultato è uguale alla prima matrice
    if result is None:
        result = matrix
    # Altrimenti, sommo il risultato con la matrice corrente
    else:
        result = np.add(result, matrix)

# Stampo il risultato
print("Ho salvato la matrice risultante rispetto alla mossa scelta nel file ", user_input)