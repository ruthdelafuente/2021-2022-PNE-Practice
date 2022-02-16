class Dog:
    def __init__(self, the_name, the_age):
        self.name = the_name
        self.age = the_age

    def say_your_name(self):
        print("I'm {}, and I'm sitting down here".format(self.name))

    def show_age(self):
        print("I'm {} years old".format(self.age))

    def say_anything(self):
        print("I like arithmetic")

    def multipli(self, first_op, second_op):
        print(f'Easy!, the result is {first_op * second_op}')

ares = Dog('ares', 10)
ares.say_your_name()
ares.show_age()
ares.say_anything()
ares.multipli(3, 5)