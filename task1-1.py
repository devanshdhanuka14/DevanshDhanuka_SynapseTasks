##Forming the best possible pokemon team
import itertools

Pokedex = {
    "Pikachu": ("Electric",),
    "Charizard": ("Fire", "Flying"),
    "Lapras": ("Water", "Ice"),
    "Machamp": ("Fighting",),
    "Mewtwo": ("Psychic", "Fighting"),
    "Hoopa": ("Psychic", "Ghost", "Dark"),
    "Lugia": ("Psychic", "Flying", "Water"),
    "Squirtle": ("Water",),
    "Gengar": ("Ghost", "Poison"),
    "Onix": ("Rock", "Ground")
}

k=int(input("Enter the value of k: "))
items=list(['Pikachu', 'Charizard', 'Lapras', 'Machamp', 'Mewtwo', 'Hoopa', 'Lugia', 'Squirtle', 'Gengar', 'Onix'])
combinations = list(itertools.combinations(items, k))

mlen = 0
bteam = None
mtypes  = None

for i in combinations:
    types=set() #we are using set here and no other datatype because it does not allow duplicates, and we dont want duplicates in the types of pokemons
    for j in i:
        types.update(Pokedex[j]) #this will update and add the types for the specific pokemon in the specific combination (group) in the types set

        if len(types)>mlen:
            mlen=len(types)
            bteam=i
            mtypes=types

print(f"Strongest team of size {k}: {bteam}")
print(f"no. of types covered: {mlen}")
print(f"the types covered: {mtypes}")

