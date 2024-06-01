def basic_calculator():
    title = 'BASIC CALCULATOR'
    divider = '--**************--'
    
    # Center and print the title and divider
    print(title.center(80))
    print(divider.center(85))
    
    # Get user input for the numbers
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    
    # Calculate the results
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2!= 0 else "Error! Division by zero."
    
    # Display operation options with a more structured format
    print("\nPlease enter:")
    print("  1 for addition")
    print("  2 for subtraction")
    print("  3 for multiplication")
    print("  4 for division\n")
    
    # Get user choice
    ch = int(input("Enter your choice: "))
    
    # Create a dictionary for operation names
    operations = {
        1: "addition",
        2: "subtraction",
        3: "multiplication",
        4: "division"
    }
    
    # Perform the chosen operation and print the result with formatting
    if ch in operations:
        result = {
            1: addition,
            2: subtraction,
            3: multiplication,
            4: division
        }[ch]
        operation_name = operations[ch]
        print(f"\nThe result of {operation_name} is: {result}")
    else:
        print("Please enter a valid number")

def main():
    while True:
        basic_calculator()
        response = input("\nDo you want to perform another calculation? (y/n): ").lower()
        if response in ['n', 'no']:
            break
        elif response in ['y', 'yes']:
            continue
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
