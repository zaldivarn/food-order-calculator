#Made by Nick for Geeky Squeaky Food Times
#2023 TM
#Copyright n shit
class Person:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getname(self):
        return self.name

    def getprice(self):
        return self.price

    def calculate(self, tax, tip):
        self.result = (self.getprice() + (self.getprice() * tax) + (self.getprice() * tip))
        return round(self.result, 2)

# main---------
people = []
tax = 0.07
tip = 0.20
print("~~Official Geek Squad Food Order Calculator v1.0~~")
while True:
    print()
    print("1. New Person")
    print("2. Print Result")
    print("3. Change Tax (Current %: " + str(tax) + ")")
    print("4. Change Tip (Current %: " + str(tip) + ")")
    print("5. Exit")

    matchinput = input("Enter Option: ")
    match matchinput:
        case "1":
            tempinput = input("Enter Name: ")
            p = Person(tempinput, 0.00)
            while True:
                    userinput = float(input("Enter Price (0 to end): "))
                    p.price += userinput
                    if userinput == 0:
                        break
            people.append(p)
        case "2":
            for person in people:
                print("1. ", end=" ")
                print(person.getname(), end=" ")
                print("  ", end="$")
                print(person.calculate(tax, tip))
                print()
            tempinput = input("Exit Program? y/n: ")
            if tempinput == "y":
                break
            else:
                print()
        case "3":
            tax = input("Enter new tax in Decimal format: ")
        case "4":
            tip = input("Enter new tip in Decimal format: ")
        case _:
            break
