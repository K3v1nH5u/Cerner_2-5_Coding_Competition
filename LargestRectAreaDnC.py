def calculateAreaDnC(heights, start, end):
	if start > end:
		return 0

	mid = start

	for i in range(start,end + 1):
		if (heights[mid] > heights[i]):
			mid = i

	return max((heights[mid]*(end - start + 1)), 
		max(calculateAreaDnC(heights,start,mid - 1),calculateAreaDnC(heights,mid + 1,end)))

#cerner_2^5_2019
def main():
	heights = [[1,4,1,3,4,5],[2,1,5,6,2,4],[4,2],
			[6,7,5,2,4,5,9,3],[1,2,3,4,5,6,7,8],[3,1,2,5,8,7]]
	for height in heights:
		print('Largest Rectangle Area is:{}'
			.format(calculateAreaDnC(height,0,len(height)-1)))

main()