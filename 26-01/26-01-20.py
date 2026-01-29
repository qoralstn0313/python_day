# num = []

# for _ in range(10):
#     num.append(int(input().strip()))

# nums = {}
# for i in range(num):
#     if i % 42


# remainders = set()

# for _ in range(10):
#     n = int(input())
#     remainders.add(n % 42)

# print(len(remainders))


N, M = map(int, input().split())
baskets = [0] * N

for k in range(N):
    baskets[k] = k + 1

for _ in range(M):
    i, j = map(int, input().split())
    baskets[i - 1 : j] = baskets[i - 1 : j][::-1]


print(" ".join(map(str, baskets)))
