class Airport(object):
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return self.name + " (" + self.country + ")"


airport_list = [
    Airport("Berlin Tegel", "Deutschland"),
    Airport("Stuttgart", "Deutschland"),
    Airport("Melbourne", "Australien")
]

for airport in airport_list:
    print(airport)

print("")

for i in range(len(airport_list)):
    print(airport_list[i])