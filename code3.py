
import random
import operator
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
op = random.choice(list(ops.keys()))
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
print(f"{num1} {op} {num2}")
ans = float(input("Enter your answer: "))
if ans == ops[op](num1, num2):
    print("Correct Answer")
else:
    print("Incorrect Answer")
    
# Output:
# 9 * 3
# Enter your answer: 27
# Correct Answer

# Output:
# 6 + 4
# Enter your answer: 10
# Correct Answer
