class Zenith:

    def __init__(self, name):
        self.name = name

    def unique_services(self):
        print("Retirement and Education Accounts")
        print("Loans and Mortgages")
        print("Checking and Saving")

        print("Multi-currency management services and products")
        print("Foreign currency accounts")
        print("Foreign currency credit cards")
        print("Transborder advisory services")
        print("Liquidity management")

        print("Advisory Services")

    def mutual_services(self):
        print("Lines of Credit")
        print("Investment Management and Accounts")
        print("Insurance")

class RetailBanking(Zenith):
    def unique_services(self):
        print("Lines of Credit")
        print("Investment Management and Accounts")
        print("Insurance")
        print("Retirement and Education Accounts")
        print("Loans and Mortgages")
        print("Checking and Saving")

class GlobalBanking(Zenith):
    def unique_services(self):
        print("Multi-currency management services and products")
        print("Foreign currency accounts")
        print("Foreign currency credit cards")
        print("Transborder advisory services")
        print("Liquidity management")

class CommercialBanking(Zenith):
    def unique_services(self):
        print("Lines of Credit")
        print("Investment Management and Accounts")
        print("Insurance")
        print("Advisory Services")


employee_name = input("Enter your name: ")


if employee_name == "Mary":
    service = RetailBanking(employee_name)
elif employee_name == "Agatha":
    service = GlobalBanking(employee_name)
elif employee_name == "Noel":
    service = CommercialBanking(employee_name)
else:
    service = Zenith(employee_name)

print(f"\nServices for {service.name}:")
service.unique_services()