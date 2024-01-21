class calculator():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

obj = calculator(a,b)


choice = 1
while choice != 0:
    print('0 : Exit')
    print('1 : Addition')
    print('2 : subtraction')
    print('3 : multiplication')
    print('4 : division')
    print('---------------------------------')
    print('---------------------------------')

    choice = int(input('Enter choice: '))

    if choice == 1:
        print('Addition: ',obj.addition())
        print('---------------------------------')
        print('---------------------------------')
    elif choice == 2:
        print('Subtraction: ',obj.subtraction())
        print('---------------------------------')
        print('---------------------------------')
    elif choice == 3:
        print('Multiplication: ',obj.multiplication())
        print('---------------------------------')
        print('---------------------------------')
    elif choice == 4:
        print('Division: ',obj.division())
        print('---------------------------------')
        print('---------------------------------')
    elif choice == 0:
        print('Exiting')
        print('---------------------------------')
        print('---------------------------------')
    else:
        print('Invalid choice !!')

print()







