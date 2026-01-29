N, M = map(int, input().split())
baskets = [0] * N

for k in range(N):
    baskets[k] = k + 1
# baskets = [0] * N
# for k in range(N):
#     baskets[k] = k + 1
change = [0]
for _ in range(M):
    i, j = map(int, input().split())
    change[0] = baskets[i - 1]
    baskets[i - 1] = baskets[j - 1]
    baskets[j - 1] = change[0]
# baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]


print(" ".join(map(str, baskets)))
