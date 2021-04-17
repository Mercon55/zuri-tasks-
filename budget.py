# zuri-tasks-
#Tasks and assignments for zuri 

class Category:
    
    def _init_(self, name):
        self.name = name
        self.transactions = []  # instance variable (list)

    def deposit(self, amount, description=None):
        if description == None:
            self.transactions.append({'amount': (amount), 'description': ''})
        else:
            self.transactions.append(
                {'amount': (amount), 'description': description})

    def withdraw(self, amount, description=None):
        if self.check_funds(amount) == True:
            if description == None:
                self.transactions.append(
                    {'amount': -(amount), 'description': ''})
            else:
                self.transactions.append(
                    {'amount': -(amount), 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for items in self.transactions:
            balance += items['amount']
        return balance

    def transfer(self, amount, budget_category):
        if self.check_funds(amount) == True:
            self.transactions.append(
                {'amount': -(amount), 'description': f"Transfer to {budget_category.name}"})
            budget_category.deposit(
                amount, description=f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def _str_(self):
        name = self.name
        s = name.center(30, "*")
        for items in self.transactions:
            try:
                left = items['description'][0:23]
            except TypeError:
                left = ''
            right = str("{:.2f}".format(items['amount']))
            s += f"\n{left:<23}{right:>7}"
        s += "\nTotal: " + str(self.get_balance())
        return s


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

entertainment = Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(15, 'Starboy Concert')

print(food)
print(clothing)
print(entertainment)
