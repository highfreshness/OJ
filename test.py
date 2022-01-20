from itertools import permutations, combinations

numbers = "011"
nums = [x for x in numbers]
permu = []
combi = []

for i in range(1, len(nums) + 1):
    permu += list(permutations(nums, i))
    new_permu = set(["".join(x) for x in permu])
    combi += list(combinations(nums, i))
    new_combi = set(["".join(x) for x in combi])

print(new_permu)
print(new_combi)
