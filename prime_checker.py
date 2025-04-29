def is_prime(number):
    """
    Check if a number is prime.
    
    Args:
        number: The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    # Handle special cases
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    # Check using 6k +/- 1 optimization
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    
    return True

def main():
    try:
        # Get user input
        num = int(input("Enter a number to check if it's prime: "))
        
        # Check if the number is prime
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
