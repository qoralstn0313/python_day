# import sys

# N = int(input().strip())

# for i in range(N):
#     A, B = map(int, sys.stdin.readline().split())
#     print(A + B)
import sys

N = int(input().strip())

for i in range(1, N + 1):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {A} + {B} = {A+B}")
