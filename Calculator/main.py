import art
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-": subtract,
    "*" :multiply,
    "/": divide,
}
# print(operations["*"](4,8))
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("type the first number: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operator = input("pick an operation: ")
        num2 = float(input("type the second number: "))
        answer = operations[operator](num1,num2)
        print(f"{num1} {operator} {num2} = {answer}")
        choice = input(f"type 'y' to continue calculating with {answer} or type 'n' to calculate with new value: ").lower()
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" *20)
            calculator()

calculator()

