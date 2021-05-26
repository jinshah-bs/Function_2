# l1 = [10.2, 2.0, 3.5, 18.9, 15.2]
# l1.sort()
# print(l1
# a = 10
# b = 15
# print(a+b)
# print(a.__add__(b))

class CarModel:

    def __init__(self, car, what, capa, fuel_type="Diesel"):
        self.model = car
        self.type = what
        self.cc = capa
        self.fuel = fuel_type

    def set_data(self, car, what, capa):
        self.model = car
        self.type = what
        self.cc = capa

    def print_data(self):
        print(self.model, self.type, self.cc, self.fuel)


Tiago = CarModel("Tiago", "HB", 1000, "Petrol")
Tiago.print_data()
Tigor = CarModel("Tigor", "NB", 1600)
Tigor.print_data()
Tigor.Fuel = "Diesel"
Tigor.print_data()
