
number_of_floors = 18
def go_to(new_floor):
        floor = 1
        while True:
            if floor <= new_floor:
                print(floor)
            elif new_floor > number_of_floors and new_floor<1 and new_floor is not int:
                print('"Такого этажа не существует"')
            break
        floor += 1
go_to(5)