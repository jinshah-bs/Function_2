class CheckSelf:
    Number = 10

    def increment_num(self):
        CheckSelf.Number +=1
        return CheckSelf.Number

    def print_id(self):
        print("The id of {} is {}".format(self, id(self)))
        print("The increment is {}".format(self.increment_num()))


obj1 = CheckSelf()
obj2 = CheckSelf()

obj1.print_id()
print("Id of {} is {}".format(obj1, id(obj1)))

# obj2.print_id()
# print("Id of {} is {}".format(obj2, id(obj2)))

