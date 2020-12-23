from enum import Enum

class Airport(object):
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return self.name + " (" + self.country.name + ")"


Countries = Enum('Countries', 'Deutschland Australien')

airport_list = [
    Airport("Berlin Tegel", Countries.Deutschland),
    Airport("Stuttgart", Countries.Deutschland),
    Airport("Melbourne", Countries.Australien)
]

# Gut lesbar
for airport in airport_list:
    print(airport)

print("")

# Schlecht lesbar
for i in range(len(airport_list)):
    print(airport_list[i])