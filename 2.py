def withdraw(money1, bankBalance):
    bankBalance -= money1
    return bankBalance

def deposit(money2, bankBalance):
    bankBalance += money2
    return bankBalance
    

deposited = int(input("for deposite press 1 for withdraw press 0 = "))
bankBalance = 0
match deposited:
    case 1: 
        depositt = int(input("enter the deposited amount = "))
        bankBalance = deposit(depositt,bankBalance)
    case 0:
        withd = int(input("enter the withdraw amount = "))
        bankBalance = withdraw(withd,bankBalance)
        
print(f"the balance is = {bankBalance}")