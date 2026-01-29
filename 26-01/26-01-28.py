T = int(input())

for _ in range(T):
    R, S = map(str, input().split())
    for i in S:
        print(i * int(R), end="")
    print("")


T = int(input())

for _ in range(T):
    R, S = input().split()
    print("".join(ch * int(R) for ch in S))
