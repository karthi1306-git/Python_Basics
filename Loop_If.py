a = 5
b = 7

# Simple If Statement
if b > a:
    print("Pass1")

# If Else Statement
if a == b:
    print("Pass2")
else:
    print("Fail2")

# If Else Statement with Elif
if a > b:
    print("Pass3")
elif a ==b:
    print("Pass3")
else:
    print("Fail3")

# Short Hand If and Else
print("Pass_SH") if b < a else print("Fail_SH")

# Using AND , OR Operator and NOT
if b > a and b != a:
    print("Both are True")
if b > a or b != a:
    print("Anyone is True")
if not b == a:
    print("True")
