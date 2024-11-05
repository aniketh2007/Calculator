from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiple(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiple,
    "/" : divide
}
def calculator():
    should_accumulate  = True
    num1 = float(input("Enter the first number : "))
    while should_accumulate:

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick a operation : ")
        num2= float(input("Enter the second number : "))

        answer = f"{operations[operation_symbol](num1,num2)}"
        print(f"{num1} {operation_symbol}{num2} = {answer}")

        choice = input(f"Type 'y' if the user wants to continue with the existing calculation {answer}, type 'n' if the user wants to exit")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 40)
            calculator()

calculator()







