class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        if other.currency == self.currency:
            result = other.amount + self.amount
            return Money(other.amount + self.amount, self.currency)
        else:
            raise ValueError("Mismatched currencies!")
    def __sub__(self, other):
        if other.currency == self.currency:
            result = self.amount - other.amount
            return Money(self.amount - other.amount, self.currency)
        else:
            raise ValueError("Mismatched currencies!")

    def __mul__(self, value):
            result = self.amount * value
            return Money(self.amount * value, self.currency)

Money1 = Money(30, "EUR")
Money2 = Money(10, "EUR")
Money3 = Money(20, "USD")

moneyss = Money1 * 5
print(moneyss)