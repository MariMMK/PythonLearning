MAX_LINES = 3  # Write in Capital because it is CONSTANT 


def deposit():
    while True:
       amount = input("What would you like to deposit ? $") #grabing the amount from the user via input()
       if amount.isdigit(): # check to ensure the input value is a whole number
           amount = int( amount) # convert to integer 
           if amount > 0 : # cheeck to ensure taht the input is greater than 0
               break # if yes , we can continue with the amount and exit of the wile loop
           else: # for propably negetive input 
               print ("Amount must be greater than 0.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") 
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: #to check the values in between two values
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print ( balance, lines)
 
main()