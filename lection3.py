def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        print("left")
        print(left)
        print("right")
        print(right)
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                print(f" первый  k= {k}  num  {nums[k]}    i {i}   j   {j}  left  {left}  right   {right}  num {nums}")          
                i += 1
            else:
                nums[k] = right[j]
                print(f" первый else  k= {k}  num  {nums[k]}    i {i}   j   {j}  left  {left}  right   {right} num {nums}")            
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            print(f" второй лефт  k= {k}  num  {nums[k]}    i {i}   j   {j}  left  {left}  right   {right} num {nums}")     
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            print(f"третий райт  k= {k}  num  {nums[k]}    i {i}   j   {j}  left  {left}  right   {right} num {nums}"  )     
            j += 1
            k += 1

nums = [38, 27, 82, 10,800,905,5]
print(nums)
merge_sort(nums)
print(nums)