class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = self.findUpperClosest(arr, x)
        left = right - 1
    
        results = []
        for _ in range(k):
            if self.isLeftCloser(arr, x, left, right):
                results.append(arr[left])
                left -= 1
            else:
                results.append(arr[right])
                right += 1
        
        return sorted(results)
    
    def findUpperClosest(self, arr, x):
        # find the first number >= x in arr
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] >= x:
                end = mid
            else:
                start = mid
        
        if arr[start] >= x:
            return start
        
        if arr[end] >= x:            
            return end
        
        # 找不到的情况
        return len(arr)
        
    def isLeftCloser(self, arr, x, left, right):
        if left < 0:
            return False
        if right >= len(arr):
            return True
        return x - arr[left] <= arr[right] - x