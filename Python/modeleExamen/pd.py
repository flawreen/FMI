def minCostClimbingStairs(cost) -> int:
	res = [0 for _ in range(len(cost))]
	res[-1], res[-2] = cost[-1], cost[-2]
	lung = len(cost)
	for i in range(lung - 3, -1, -1):
		res[i] = cost[i] + min(res[i + 1], res[i + 2])
	return min(res[0], res[1])


cost = [1,100]
print(minCostClimbingStairs(cost))
