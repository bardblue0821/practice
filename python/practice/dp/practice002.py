N, K = map(int, input().split())
h = list(map(int, input().split()))


def chmin(a, b):
    if a > b:
        return b
    else:
        return a

cost = []
for i in range(10010):
    cost.append(999999999999)

cost[0] = 0

for i in range(1, N):
    cost[i] = chmin(cost[i], cost[i-1] + abs(h[i] - h[i-1]))
    for j in range(1, K):
        if i < j:
            cost[i] = chmin(cost[i], cost[i-j] + abs(h[i] - h[i-j]))

print(cost[N-1])