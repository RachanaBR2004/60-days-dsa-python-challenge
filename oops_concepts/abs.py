# For learning Python abstraction, practise this problem first:

# Create an abstract class Payment with an abstract method pay().

# Create three child classes:
# - CreditCard
# - UPI
# - Cash
# Each class should implement pay() differently.


from abs import ABC, abstractmethod

class payment(abs):
    @abstractmethod
    def pay():
        pass

class creditedcard(payment):
    def 