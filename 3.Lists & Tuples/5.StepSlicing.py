# Step Slicing of the lists.

nums = [10,20,30,40,50,60,70,80,90,100]

nums1 = nums[::2] # Every second item will be printed [10,30,50,70]
nums2 = nums[::-1] # Reverse the list [100,90,80,70,60,50,....]
nums3 = nums[1::3] # Start at index 1, jump 3 [20,50]

print(nums1)
print(nums2)
print(nums3)