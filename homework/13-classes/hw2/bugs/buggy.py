class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            return "金額無效"
        if amount > self.balance:
            return "餘額不足"
        balance = self.balance - amount
        return f"領出 {amount} 元"


account = Account(100)
message = account.withdraw(int(input()))
print(f"{message}，餘額 {account.balance} 元")
