class Main():
    def __init__(self,greeting):
        self.greeting = greeting

    def output(self):
        return self.greeting

instance = Main('Hi')
print(instance.output())
