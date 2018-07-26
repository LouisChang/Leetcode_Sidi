class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total_sum = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                curr = left + 1
                while  height[curr] <= height[left] and curr < right:
                    total_sum += height[left] - height[curr]
                    curr += 1
                left = curr
                pass
            else:
                curr = right - 1
                while  height[curr] <= height[right] and curr > left:
                    print curr, right
                    total_sum += height[right] - height[curr]
                    curr -= 1
                right = curr
                pass
        
        return total_sum
