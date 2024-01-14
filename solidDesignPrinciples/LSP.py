
# If a class is a subclass of another class, it should be usable in place of its superclass without the client code needing to know the specific subclass.

# Violation of LSP

class Bird:
    def fly(self):
        pass

class Penguin(Bird): # this is voliation of LSP caz Peguin should hv been able to replace Bird class without changing the behaviour of code 
    def fly(self):
        # Penguins can't fly, so this violates LSP
        raise NotImplementedError("Penguins can't fly")

# Adhering to LSP

class Bird:
    def move(self):
        pass

class FlyingBird(Bird): # here both Peguin and FlyingBird can replace Bird class without throwing any error 
    def fly(self):
        pass

class Penguin(Bird):
    def move(self):
        # Penguins move by swimming
        pass
