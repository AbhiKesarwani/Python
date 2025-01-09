#operations to perform
def add(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def exponent(n1,n2):
    return n1**n2

operations ={
    "+":add,
    "-":subtraction,
    "*":multiplication,
    "/":divide,
    "**":exponent
}

def calculator():
    calculator_is_on = True
    while calculator_is_on:    #Loop will help to off the calculator
        print("""
            _____________________
        |  _________________  |
        | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
        | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
        |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
        | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
        | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
        | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
        | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
        | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
        | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
        | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
        | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
        |_____________________|
        """
        )
        num1 = int(input("What's the first number? ")) 
        calculation_is_on =True
        while calculation_is_on:     #Loop will help to start a fresh calculation
            for key in operations:    #printing operands
                print(key)    
            operator = input("Choose an operator from above: ")
            if operator not in operations:
                print("Invalid Opeator Choosen")
                calculator_is_on = False   #doing calculator off
                break
            num2 = int(input("What's the next number? "))
            function=operations[operator]
            output=function(num1,num2)   #performing operation and calling function
            print(f"{num1} {operator} {num2} = {output}")
            further = input(f"Type 'y' to continue calculatong with answer {output}, or type 'n' to start a new calculation, or type 'off' to off the calculator: ")
            if further == "y":
                calculation_is_on = True
                num1 = output
            elif further == "n":
                calculation_is_on = False
                calculator()
            elif further == "off":
                print("Thank you")
                calculation_is_on = False
                calculator_is_on = False
            else :
                print("Invalid Input")
                calculation_is_on = False
                calculator_is_on = False

calculator()