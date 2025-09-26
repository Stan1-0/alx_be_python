def perform_operation(num1, num2, operation):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    
    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 > 0:
                result = num1 / num2
            else:
                result = f"You cannot divide by 0. {ZeroDivisionError}"
        case "_":
            print("No operation selected")
            
    print(f"Result: {result}")
            
