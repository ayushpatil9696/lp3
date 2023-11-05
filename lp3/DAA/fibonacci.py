def fibonacci_iterative(n):
    a, b = 0, 1
    sequence = [a]
    for _ in range(n-1):
        a, b = b, a + b
        sequence.append(a)
    return sequence

n = 10
print(f"The Fibonacci sequence up to {n} terms (iterative) is: {fibonacci_iterative(n)}")

# TIME COMPLEXITY FOR ITERATIVE = O(n)
# SPACE COMPLEXITY FOR ITERATIVE = O(1)

def fibonacci_recursive(n, a=0, b=1, sequence=None):
    if sequence == None:
        sequence = []
    if n == 0:
        return sequence
    sequence.append(a)
    return fibonacci_recursive(n-1, b, a+b, sequence)

print(f"The Fibonacci sequence up to {n} terms (recursive) is: {fibonacci_recursive(n)}")

# TIME COMPLEXITY FOR ITERATIVE = O(2^n)
# SPACE COMPLEXITY FOR RECURSIVE = O(n) (due to the recursion stack)