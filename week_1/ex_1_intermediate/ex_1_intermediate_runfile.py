#create a dictionnary of species
microbial_species={'Bacteria':20,
                   'Archea':15,
                   'Fungi':10}

#Calculate the the total number of samples
count=0
for x in microbial_species.values():
    count=count+(x)
print(str(count)+' samples have been collected')

#list comprehension to create a list of microbial species with sample counts greater than 15
greater_than_15=[species for species, count in microbial_species.items() if count >15]
print(greater_than_15)

#Create a function
def add_species ():
    nom_champi=input("enter the new species name: ")
    if microbial_species.get(nom_champi):
        nombre_champi=microbial_species.get(nom_champi)+1
        return microbial_species.update({nom_champi:nombre_champi})
    else:
        return microbial_species.update({nom_champi:1})

#While loop to continuously prompt the user for new species names

new_s=input('Enter a new species name: ')
while len(new_s)>0:
    add_species()
    new_s=input('Enter a new species name: ')

print(microbial_species)



