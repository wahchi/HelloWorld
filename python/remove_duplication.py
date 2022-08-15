"""
Arr is an array consisting of random number of positive 
The integers in the array are already sorted in ascending order.
Let the count of unique integers in the array be C, please change 
this array to following state:
- The first C integers are the unique integers sorted in ascending order;
- The integers in order position remain as they are
Notice:
- The time complexity of the function should be O(n)
- It is not allowed to create a new array
Test example:
arr = [2, 5, 5, 8, 12, 12, 12, 25, 36, 36]
Return - 
print(solution(arr)) # 6
print(arr) # [2, 5, 8, 12, 25, 36, 12, 25, 36, 36]
"""


def solution(arr):
    index = None
    for i in range(len(arr)):
        if i == 0:
            index = 0
        else:
            if arr[index] != arr[i]:
                index += 1
                arr[index] = arr[i]
                
    return index

if __name__ == "__main__":
    arr = [2, 5, 5, 8, 12, 12, 12, 25, 36, 36]
    print(solution(arr))
    print(arr)