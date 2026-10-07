def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorial(5):", factorial(5))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci(6):", fibonacci(6))


def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print("Sum of digits(1234):", sum_digits(1234))


def reverse_string_rec(s):
    if len(s) == 0:
        return s
    return reverse_string_rec(s[1:]) + s[0]

print("Reverse of 'hello':", reverse_string_rec("hello"))


def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n-1)
    print(n)

print("Print 1 to 5:")
print_1_to_n(5)


def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n-1)

print("Print 5 to 1:")
print_n_to_1(5)


def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

print("Power(2, 5):", power(2, 5))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print("GCD(48, 18):", gcd(48, 18))


def is_palindrome_rec(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_rec(s[1:-1])

print("Palindrome check 'madam':", is_palindrome_rec("madam"))
print("Palindrome check 'python':", is_palindrome_rec("python"))


def tower_of_hanoi(n, src, dest, aux):
    if n == 1:
        print("Move disk 1 from", src, "to", dest)
        return
    tower_of_hanoi(n-1, src, aux, dest)
    print("Move disk", n, "from", src, "to", dest)
    tower_of_hanoi(n-1, aux, dest, src)

print("Tower of Hanoi with 3 disks:")
tower_of_hanoi(3, 'A', 'C', 'B')
