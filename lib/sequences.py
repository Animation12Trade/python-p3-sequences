#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print("[]")
    elif length == 1:
        print("[0]")
    else:
        fibonacci_sequence = [0, 1]
        for _ in range(2, length):
            next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_fib)
        print(f"[{', '.join(map(str, fibonacci_sequence))}]")


print_fibonacci(0)  
print_fibonacci(1)  
print_fibonacci(2)  
print_fibonacci(10)