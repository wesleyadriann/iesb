
# -*- coding: utf-8 -*-

from Graph import Graph
from fileReader import fileReader
from distanceCalc import distanceCalc

users = fileReader()
users_ = []
count = 0
for user in users:
    user = user.split(';')
    user[1] = user[1].split(',')
    users_.append({
        "id" : count,
        "mome" : user[0],
        "latitude" : float(user[1][0]),
        "longitude" : float(user[1][1]),
        "profissao" : user[2],
        "disponibilidade" : user[3]
    })
    count += 1

users = users_[:]
del users_, count

graph = Graph(len(users))
for user in users:
    for user_ in users:
        if (user['id'] is not user_['id']):
            user_['dist'] = distanceCalc(user['latitude'], user['longitude'], user_['latitude'], user_['longitude'])
            graph.GRAPHInsert(user, user_)


print("\n********************************")
print("********** PROJETO 02 **********")
print("**********   FINDER   **********")
print("********************************")

lat = -15.836073
lng = -47.912019
print(f"\nLatitude atual {lat} \nLongitude atual {lng}")
print("Deseja mudar ?")

range = 50
print(f"{range}km é o raio maximo para encontrar profissionais.")
print("Deseja mudar ?")

# Nome, latitude, longitude, profissão, disponibilidade
print(f"\nLista de profissionais disponiveis em ate {range} km\n")
select_users = ["a", "b", "c"]
for user in users:
    print(f"({user['id']:02d}) - {user['profissao']}")


print("\nO caminho que você tera que fazer")
print(" -> ".join(select_users))

distanceCalc(lat,lng,users[0]['latitude'],users[0]['longitude'])