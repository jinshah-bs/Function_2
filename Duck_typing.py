class Flight:
    def __init__(self, l_w_r):
        self.len_wid_ratio = l_w_r

    def fly(self):
        if self.len_wid_ratio > 1:
            print("It can fly higher")
        elif self.len_wid_ratio == 1:
            print('It ca barely fly')
        else:
            print('It cant fly')


class Duck:
    def __init__(self):
        self._lwr = Flight(1.8)
        self. weight = 20

    def walk(self):
        print("the duck walks gracefully")

    def swim(self):
        print("The duck swim very gently")

    def quack(self):
        print("The duck quak quack quack")

    def fly(self):
        self._lwr.fly()

class Pellicans:
    def walk(self):
        print("pelican walks like a duck")

    def swim(self):
        print("Pelican swim like a duck")

    def quack(self):
        print('pelican quack quack quack')

# def duck_test(self, duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

dinesh = Duck()
# duck_test(dinesh)
#
# saravanan = Pellicans()
# duck_test(saravanan)
dinesh.fly()


