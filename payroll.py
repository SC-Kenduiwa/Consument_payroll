class SalesPerson:
    def __init__(self, name, sales_amount):
        self.name = name
        self.sales_amount = sales_amount
        self.commission = 0
        self.bonus = 0

    def __str__(self):
        return f"{self.name}: Sales = KES {self.sales_amount}, Commission = KES {self.commission}, Bonus = KES {self.bonus}"
    def calculate_pay(self):
        if self.sales_amount >= 500000:
            self.commission = self.sales_amount * 0.30
            self.bonus = 25000
        elif 350000 <= self.sales_amount < 500000:
            self.commission = self.sales_amount * 0.20
        elif 200000 <= self.sales_amount < 350000:
            self.commission = self.sales_amount * 0.10
        elif 50000 <= self.sales_amount < 200000:
            self.commission = self.sales_amount * 0.05
        # sales below 50k => no commission or bonus
class PayrollSystem:
    def __init__(self):
        self.salespeople = []

    def add_salesperson(self, person):
        self.salespeople.append(person)

    def process_payroll(self):
        for person in self.salespeople:
            person.calculate_pay()

    def print_report(self):
        total_commission = 0
        print("----- Payroll Report -----")
        for person in self.salespeople:
            print(person)
            total_commission += person.commission
        print(f"\nTotal Commission Paid Out: KES {total_commission}")
def main():
    payroll = PayrollSystem()

    test_data = [
        ("Alice", 510000),
        ("Bob", 475000),
        ("Carol", 330000),
        ("Dan", 60000),
        ("Eve", 45000),
        ("Faith", 200000),
        ("George", 150000),
        ("Hannah", 300000),
        ("Ian", 550000),
        ("Jane", 490000),
        ("Kevin", 349999),
        ("Liam", 55000),
        ("Mona", 51000),
        ("Nora", 345000),
        ("Oscar", 180000),
        ("Paul", 90000),
        ("Queen", 250000),
        ("Ron", 499999),
        ("Sarah", 198000),
        ("Tom", 10000)
    ]

    for name, sales in test_data:
        person = SalesPerson(name, sales)
        payroll.add_salesperson(person)

    payroll.process_payroll()
    payroll.print_report()

if __name__ == "__main__":
    main()
