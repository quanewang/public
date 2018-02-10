def count_sums(nums, sum):
    mem = {}
    return count_sums_helper(nums, sum, 0, mem)

def count_sums_helper(nums, sum, idx, mem):
    if sum is 0:
        return 1
    if sum is None or sum < 0:
        return 0
    if not nums or idx >= len(nums):
        return 0
    if hash(sum, idx) in mem:
        return mem[hash(sum, idx)]
    first = nums[idx]
    remainder = sum - first
    result = count_sums_helper(nums, remainder, idx+1, mem) + count_sums_helper(nums, sum, idx+1, mem)
    mem[hash(sum, idx)] = result
    return result

def hash(sum, idx):
    return str(sum) + '_' + str(idx)

print count_sums(None, 16)
print count_sums([], 16)
#print count_sets([-10], 16)
print count_sums([0], 16)
print count_sums([16], 16)
print count_sums([2, 4, 6, 10], 16)

