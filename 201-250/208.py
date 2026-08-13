a = int(input())
b = int(input())

total = a + b
whole = total // 2
remainder = total % 2
if remainder == 0:
    print(f"{whole}.0")
else:
    print(f"{whole}.5")