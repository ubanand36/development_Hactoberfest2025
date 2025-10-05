def two_sum(nums, target):
    num_map = {}  # To store number and its index
    
    for i, num in enumerate(nums):
        complement = target - num  # The number we need
        
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[num] = i  # Store index of the current number
    
    return []  # If no pair found

# Example:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
