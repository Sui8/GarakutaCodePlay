W = []
K = []

for i in range(10):
    W.append(int(input()))

for i in range(10):
    K.append(int(input()))

W.sort(reverse=True)
K.sort(reverse=True)

print(f"{W[0] + W[1] + W[2]} {K[0] + K[1] + K[2]}")