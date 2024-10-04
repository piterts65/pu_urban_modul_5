class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for floor in range(1, new_floor + 1):
            if 1 <= new_floor <= self.number_of_floors:
                print(floor)
            else:
                print('"Такого этажа не существует"')
                break

    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    print(h1)
    print(h2)

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.

    def __add__(self, value):
        return self.number_of_floors ==self.number_of_floors + value


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
#h1.go_to(5)
#h2.go_to(10)

# __str__
#print(h1)
#print(h2)

# __len__
#print(len(h1))
#print(len(h2))

print(h1)
print(h2)

print(h1 == h2) # __eq__


def __add__(self, value):
    return self.number_of_floors == self.number_of_floors + value