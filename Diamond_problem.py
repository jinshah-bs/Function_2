class BaseClass:
    no_of_basecalls = 0

    def print_message(self):
        print("Executed Base class")
        BaseClass.no_of_basecalls += 1


class LeftClass(BaseClass):
    no_of_leftcalls = 0

    def print_message(self):
        BaseClass.print_message(self)
        print("Executed left class")
        LeftClass.no_of_leftcalls += 1


class RightClass(BaseClass):
    no_of_rightcalls = 0

    def print_message(self):
        BaseClass.print_message(self)
        print("Executed right class")
        RightClass.no_of_rightcalls += 1


class SubClass(LeftClass, RightClass):
    no_of_subcalls = 0

    def print_message(self):
        LeftClass.print_message(self)
        RightClass.print_message(self)
        print("Executed Sub Class")
        SubClass.no_of_subcalls += 1


trial = SubClass()
trial.print_message()
print(trial.no_of_subcalls, trial.no_of_leftcalls, trial.no_of_rightcalls, trial.no_of_basecalls)