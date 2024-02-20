from datetime import datetime

class Student():
    def __init__(self, name, grades) -> None:
        self.name = name
        self.grades = grades
    
    def average_grade(self):
        if len(self.grades) > 5:
            return
        else:
            result = sum(self.grades) // len(self.grades)
            return result
    

bodyan = Student('Bogdan', [4, 5, 4, 4, 3])

print(bodyan.average_grade())

class Book():
    
    def __init__(self, title, author, public_year) -> None:
        self.title = title
        self.author = author
        self.public_year = public_year
    
    def get_age(self):
        today =  datetime.now().year
        res = today - self.public_year
        return res

book = Book('На Западном Фронте без перемен', 'Ремарк', 1954)
print(book.get_age())


class BankAccount():
    def __init__(self, account_number, balance) -> None:
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Ваш банковский счет пополнен на {amount}.')
        
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f'C вашего банковского счета сняли {amount}.')
    
    def get_balance(self):
        print(f'Текущий баланс вашего банковского счета "{self.account_number}" составляет {self.balance}')
    
my_account = BankAccount(43545445, 2100)
my_account.deposit(200)
my_account.withdraw(300)
my_account.get_balance()

        