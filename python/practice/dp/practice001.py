N = int(input())
h = list(map(int, input().split()))

def chmin(a, b):
    if a > b:
        return b
    else:
        return a

cost = []
for i in range(100010):
    cost.append(9999999)

cost[0] = 0

for i in range(1, N):
    cost[i] = chmin(cost[i], cost[i-1] + abs(h[i] - h[i-1]))
    if i > 1:
        cost[i] = chmin(cost[i], cost[i-2] + abs(h[i] - h[i-2]))

print(cost[N-1])