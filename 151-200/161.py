nums = []

while True:
    try:
        nums.append(int(input()))
    except EOFError:
        break

print(sum(nums))