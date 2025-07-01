class SalesPerson:
    def __init__(self, name, sales_amount):
        self.name = name
        self.sales_amount = sales_amount
        self.commission = 0
        self.bonus = 0

    def __str__(self):
        return f"{self.name}: Sales = KES {self.sales_amount}, Commission = KES {self.commission}, Bonus = KES {self.bonus}"
