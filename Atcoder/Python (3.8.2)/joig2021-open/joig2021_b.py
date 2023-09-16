N, K = (int(x) for x in input().split())
T = input()

print(T[:K-1] + T[K-1:].swapcase())