
# ISP-> Interface Segregation Principle suggests that a class should not be forced to implement interfaces it does not use. In other words, it encourages the use of small, specific interfaces rather than large, general ones.

# Violation of ISP

class Worker:
    def work(self):
        pass
    
    def eat(self):
        pass

# Adhering to ISP

class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Worker(Workable, Eatable):
    pass
