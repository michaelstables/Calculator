is_running = True


def addition(args):
    answer = 0
    for arg in args:
        answer = answer + arg
    print(answer)


def multiplication(args):
    result = 1  # Initialize the result as 1

    for arg in args:
        result *= arg
    print(result)


def subtraction(args):
    answer = args[0]
    for i in range(1, len(args)):
        answer = answer - args[i]
    print(answer)

def division(args):
    answer = args[0]

    for i in range(1, len(args)):
        if args[i] != 0:  # Avoid division by zero
            answer /= args[i]
        else:
            return "Division by zero is not allowed."

    print(answer)
def exponent(args):
    result = args[0]  # Initialize the result as 1
    for i in range(1, len(args)):
        result = result ** args[i]
    print(result)

def calculator_interface():
    userinput = input("What type of math function would you like to perform: ")

    if userinput == "add" or userinput == "1":
        user_input_list = []
        num_item = int(input("How many items would you like to enter?"))
        for i in range(num_item):
            user_input = int(input("Enter Number"))
            user_input_list.append(user_input)
        addition(user_input_list)

    if userinput == "subtract" or userinput == "2":
        user_input_list = []
        num_item = int(input("How many items would you like to enter?"))
        for i in range(num_item):
            user_input = int(input("Enter Number"))
            user_input_list.append(user_input)
        subtraction(user_input_list)

    if userinput == "multiplecation" or userinput == "3":
        user_input_list = []
        num_item = int(input("How many items would you like to enter?"))
        for i in range(num_item):
            user_input = int(input("Enter Number"))
            user_input_list.append(user_input)
        multiplication(user_input_list)

    if userinput == "division" or userinput == "4":
        user_input_list = []
        num_item = int(input("How many items would you like to enter?"))
        for i in range(num_item):
            user_input = int(input("Enter Number"))
            user_input_list.append(user_input)
        division(user_input_list)

    if userinput == "exponet" or userinput == "5":
        user_input_list = []
        num_item = int(input("How many items would you like to enter?"))
        for i in range(num_item):
            user_input = int(input("Enter Number"))
            user_input_list.append(user_input)
        exponent(user_input_list)

    if userinput == "exit" or userinput == "6":
        global is_running
        is_running = False

def print_instructions():
    print(
      "Please select an option below\n "
      "Add or 1\n "
      "Subtract or 2\n "
      "Multiplecation or 3\n"
      "Divison or 4\n "
      "Exponent or 5\n"
      "End or 6 to close\n"
    )


print("Welcome to calculator. It is for any k-5. \n")
while is_running:
    print_instructions()
    calculator_interface()
