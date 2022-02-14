def util_func():
    print("Using the util_func")


class UsefulClass():

    def __init__(self, message):
        self.message = message

    def report(self):
        print(self.message)


class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print('helo')

    def report(self):
        print(f'I am {self.first_name} {self.last_name}')


class Agent(Person):

    def __init__(self, first_name, last_name, code_name):
        Person.__init__(self, first_name, last_name)
        self.code_name = code_name

    def report(self):
        print(f'I Am Here. My code is {self.code_name} (override method)')

    def reveal(self, passcode):

        if passcode == 123:
            print("I am a secret agent!")
        else:
            self.report()
