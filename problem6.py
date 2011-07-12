numbers = range(1,101)

diff = 0 

for num in numbers:
    for num2 in numbers:
        if num==num2:
            continue
        diff += num*num2

print diff
