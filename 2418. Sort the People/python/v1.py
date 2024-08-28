from typing import List

class Solution:
	def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
		def quick_sort_recurse(low: int, high: int):
			if low >= high:
				return

			pivot = heights[high]
			final_pivot_index = low
			
			for i in range(low, high + 1):
				if heights[i] > pivot:
					heights[final_pivot_index], heights[i] = heights[i], heights[final_pivot_index]
					names[final_pivot_index], names[i] = names[i], names[final_pivot_index]
					final_pivot_index += 1
			
			heights[final_pivot_index], heights[high] = heights[high], heights[final_pivot_index]
			names[final_pivot_index], names[high] = names[high], names[final_pivot_index]
			
			quick_sort_recurse(low, final_pivot_index - 1)
			quick_sort_recurse(final_pivot_index + 1, high)
	
		quick_sort_recurse(0, len(names) - 1)
		return names

if __name__ == "__main__":
	solution = Solution()
	names = ["IEO","Sgizfdfrims","QTASHKQ","Vk","RPJOFYZUBFSIYp","EPCFFt","VOYGWWNCf","WSpmqvb"]
	heights = [17233,32521,14087,42738,46669,65662,43204,8224]
	
	res = solution.sortPeople(names, heights)
	print(res)
