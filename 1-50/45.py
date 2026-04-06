n = int(input())
numbers = list(map(int, input().split()))

counts = [0] * 10  # 1 dan 9 gacha
results = [-1] * 9  # 9 ta natija, default -1

for i, number in enumerate(numbers):
    if 1 <= number <= 9:
        counts[number] += 1
        if counts[number] == number:  
            results[number - 1] = i + 1  # 1-based index

print(*results)