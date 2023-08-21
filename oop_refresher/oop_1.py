class Greeting:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")


class BetterGreeting(Greeting):
    def say_hello(self):
        super().say_hello()
        print(f"This is better greeting for you, {self.name}!")


greeting = BetterGreeting("John")
greeting.say_hello()
