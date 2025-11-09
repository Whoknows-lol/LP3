# --------------------------------------------
# Program: Fibonacci Numbers (Recursive & Non-Recursive)
# Objective:
#   1. Understand Fibonacci Number Generation
#   2. Compare Time & Space Complexity of Recursive vs Iterative methods
# --------------------------------------------

# Recursive function to calculate Fibonacci number
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# Non-recursive (iterative) function to generate Fibonacci series
def fib_iterative(n):
    a, b = 0, 1
    series = []
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Main code
if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))

    # Iterative approach
    print("\nFibonacci Series using Iterative (Non-Recursive) Method:")
    iterative_series = fib_iterative(n)
    print(iterative_series)

    # Recursive approach
    print("\nFibonacci Series using Recursive Method:")
    recursive_series = [fib_recursive(i) for i in range(n)]
    print(recursive_series)

    # Analysis Summary
    print("\n----- Time and Space Complexity Analysis -----")
    print("Recursive Method:")
    print("  ➤ Time Complexity: O(2^n)  (Exponential)")
    print("  ➤ Space Complexity: O(n)   (Due to recursion stack)")
    print("\nIterative (Non-Recursive) Method:")
    print("  ➤ Time Complexity: O(n)    (Single loop runs n times)")
    print("  ➤ Space Complexity: O(1)   (Only a few variables used, ignoring list storage)")
