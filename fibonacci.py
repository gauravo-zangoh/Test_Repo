def fibonacci(n):
    """
    Generate Fibonacci series up to the nth term.
    
    Args:
        n: Number of terms in the series
        
    Returns:
        A list containing the Fibonacci series
    """
    # Initialize the series with the first two numbers
    fib_series = [0, 1]
    
    # Generate the series up to n terms
    for i in range(2, n):
        # Next number is the sum of the previous two
        next_num = fib_series[i-1] + fib_series[i-2]
        fib_series.append(next_num)
    
    return fib_series[:n]  # Return only n terms

def main():
    # Get user input for the number of terms
    try:
        n = int(input("Enter the number of terms for Fibonacci series: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
            
        # Generate and display the series
        series = fibonacci(n)
        print(f"Fibonacci series with {n} terms:")
        print(series)
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
