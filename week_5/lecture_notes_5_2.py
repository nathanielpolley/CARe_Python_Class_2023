'''Review of Objects in Python
Modeling a bacteria cell as an object with more elaborate methods
'''

class BacteriaCell:
    def __init__(self, name, shape, size, growth_rate):
        self.name = name
        self.shape = shape
        self.size = size
        self.growth_rate = growth_rate
        self.population = 1  # Start with one cell in the population

    def replicate(self):
        new_cells = self.population * 2
        self.population += new_cells
        print(f"{self.name} is replicating. Population: {self.population}")

    def infect_host(self, host):
        if self.population > 0:
            self.population -= 1
            print(f"{self.name} is infecting {host}. Population reduced to {self.population}.")
        else:
            print(f"{self.name} population is exhausted. Cannot infect {host}.")

    def describe(self):
        print(f"Details of {self.name}:")
        print(f"Shape: {self.shape}")
        print(f"Size: {self.size}")
        print(f"Growth Rate: {self.growth_rate}")
        print(f"Current Population: {self.population}")


# Creating a BacteriaCell object
e_coli = BacteriaCell("E. coli", "Rod-shaped", "1-2 μm", "20 minutes")

# Elaborate methods usage
e_coli.describe()  # Describe the cell
e_coli.replicate()  # Replicate the cell
e_coli.replicate()  # Replicate again
e_coli.infect_host("human intestine")  # Infect a host
e_coli.replicate()  # Replicate once more
e_coli.infect_host("human lung")  # Infect another host
e_coli.describe()  # Describe the cell after actions

