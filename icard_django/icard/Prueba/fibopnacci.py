def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_term = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_term)
        return fib_sequence

# Solicita el número de términos
num_terms = int(input("¿Cuántos términos de la sucesión de Fibonacci deseas? "))
fibonacci_sequence = fibonacci(num_terms)

print("Sucesión de Fibonacci:")
for term in fibonacci_sequence:
    print(term, end=" ")
print()
