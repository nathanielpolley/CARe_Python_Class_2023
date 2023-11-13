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
print('We have collected more than 15 '+ str(greater_than_15))

#Create a function
def add_species ():
    new_species
    if microbial_species.get(new_species):
        nombre_champi=microbial_species.get(new_species)+1
        return microbial_species.update({new_species:nombre_champi})
    else:
        return microbial_species.update({new_species:1})

#While loop to continuously prompt the user for new species names

new_species=input('Enter a new species name: ')
while len(new_species)>0:
    add_species()
    new_species=input('Enter a new species name: ')

print('The new dictonnary is now '+str(microbial_species))



