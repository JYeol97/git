# N = int(input())
# Achievement = list(map(int, input().split()))
# max_Achievement = max(Achievement) * 100

# result = [(num / (max_Achievement)) for num in Achievement]

# print(sum(result) / N)



N = int(input())
Achievement = list(map(float, input().split()))
max_Achievement = max(Achievement)

result = [(num / (max_Achievement)*100) for num in Achievement]

print(sum(result) / N)