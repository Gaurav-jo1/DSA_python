# Q - Split Array Largest Sum

# Ans - 

nums = [10,20,11,23,12]
m =2

def splitArray():
    start = 0
    end = 0
    for i in range(nums) :
        start = nums[0] 
        end += nums[i]
    
    while start < end:
        mid = start + (end - start) // 2
        sum = 0
        piceces = 1
        for num in nums:
            if sum + num > mid:
                sum = num
                pieces += 1 
            else:
                start += num
        
        if piceces > m:
            start = mid + 1
        else:
            end = mid

    return end
