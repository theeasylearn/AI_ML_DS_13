#example of relational operator

a = 10
b = 20
c = 30

result = a < b or b < c 
print(f"{result} {a} < {b} or {b} < {c}")

result = a > b or b < c 
print(f"{result} {a} > {b} or {b} < {c}") # True

result = a < b or b > c 
print(f"{result} {a} < {b} or {b} > {c}") # True


result = a > b or b > c 
print(f"{result} {a} > {b} or {b} > {c}") # False


result = a < b and b < c 
print(f"{result} {a} < {b} and {b} < {c}") # True

result = a > b and b < c 
print(f"{result} {a} > {b} and {b} < {c}") # False

result = a < b and b > c 
print(f"{result} {a} < {b} and {b} > {c}") # False


result = a > b and b > c 
print(f"{result} {a} > {b} and {b} > {c}") # False


result = not (a > b and b > c)
print(f" {result} not ({a} > {b} and {b} > {c})") # True


