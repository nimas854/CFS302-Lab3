import random
import time

def grade_school(a, b):
    a = a.lstrip("0") or "0"
    b = b.lstrip("0") or "0"
    if a == "0" or b == "0":
        return "0"

    x = [int(c) for c in reversed(a)]
    y = [int(c) for c in reversed(b)]
    result = [0] * (len(x) + len(y))

    for i in range(len(x)):
        carry = 0
        for j in range(len(y)):
            total = result[i + j] + x[i] * y[j] + carry
            result[i + j] = total % 10
            carry = total // 10
        result[i + len(y)] += carry

    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return ''.join(map(str, reversed(result)))

def add_strings(a, b):
    carry = 0
    out = []
    i, j = len(a)-1, len(b)-1
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += ord(a[i]) - 48
            i -= 1
        if j >= 0:
            total += ord(b[j]) - 48
            j -= 1
        out.append(str(total % 10))
        carry = total // 10
    return ''.join(reversed(out)).lstrip("0") or "0"

def sub_strings(a, b):
    # Assumes a >= b and both are non-negative.
    out = []
    borrow = 0
    i, j = len(a)-1, len(b)-1
    while i >= 0:
        d = ord(a[i]) - 48 - borrow
        if j >= 0:
            d -= ord(b[j]) - 48
            j -= 1
        if d < 0:
            d += 10
            borrow = 1
        else:
            borrow = 0
        out.append(str(d))
        i -= 1
    return ''.join(reversed(out)).lstrip("0") or "0"

def shift_decimal(s, k):
    return "0" if s == "0" else s + "0" * k

def karatsuba(x, y):
    x = x.lstrip("0") or "0"
    y = y.lstrip("0") or "0"
    if x == "0" or y == "0":
        return "0"
    if len(x) <= 2 or len(y) <= 2:
        return str(int(x) * int(y))

    n = max(len(x), len(y))
    if n % 2:
        n += 1
    x = x.zfill(n)
    y = y.zfill(n)
    m = n // 2

    a, b = x[:-m], x[-m:]
    c, d = y[:-m], y[-m:]

    z2 = karatsuba(a, c)
    z0 = karatsuba(b, d)
    z1 = karatsuba(add_strings(a, b), add_strings(c, d))
    z1 = sub_strings(sub_strings(z1, z2), z0)

    return add_strings(
        add_strings(shift_decimal(z2, 2*m), shift_decimal(z1, m)),
        z0
    )

def random_number(digits):
    first = str(random.randint(1, 9))
    return first + ''.join(str(random.randint(0, 9)) for _ in range(digits - 1))

if __name__ == "__main__":
    print("Q2: Karatsuba vs Grade-School Multiplication")
    print("Digits | Grade-school(s) | Karatsuba(s) | Match")
    for digits in [8, 16, 32, 64, 128, 256]:
        a = random_number(digits)
        b = random_number(digits)

        t0 = time.perf_counter()
        r1 = grade_school(a, b)
        t1 = time.perf_counter()

        t2 = time.perf_counter()
        r2 = karatsuba(a, b)
        t3 = time.perf_counter()

        print(f"{digits:6} | {t1-t0:.6f}       | {t3-t2:.6f}   | {r1 == r2}")
# Analysis / Conclusion:
#In grade-school multiplication, the result of a single-digit multiplication is done in about n^2 time.
#The time complexity of this code is O(n^2), because we are making n*n multiplications.
#This is because Karatsuba requires only three recursive multiplications instead of four.
# T(n) = 3T(n/2) + O(n), giving O(n^log2(3)) ≈ O(n^1.585).
#These two methods should yield the same product.
# Karatsuba may incur additional costs for small inputs, but reduces its complexity.
#As the number of digits increases, the "asymptotic complexity" becomes useful.
