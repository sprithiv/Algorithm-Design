
list_a = [2,8,-9,20,25,-127,90,50,-89,-2,125,64,8,-15,-8,10,11,-30,22]

def find_max(list_val): 
	
	#Variable declaration
    length = len(list_val)
    max_val = max(list_val)
	
	#Start index
    idx1 = list_val.index(max_val) + 1
	#End index
    idx2 = list_val.index(max_val) + 1
	
	#Iterative algorithm to find the max sub array
    k=1
	#To iterate till end of the given list
    for x in range(0,length-2):
        l = x + 2
		#To iterate till length-k elements in the list
        for y in range(0,length-k):
            sum = 0
            for z in range(y,l):
                sum = sum + list_val[z]
			#Compare the sum with max_val
            if (sum > max_val):
                max_val = sum
                idx1 = y+1
                idx2 = l
            l=l+1
        k = k+1
	#Return the sum,index 1 and index 2
    return(max_val,idx1,idx2)

def main():
	
	#variable declarations
	#Find the length of the given list
	length = len(list_a)
	#Split the list into two halves
	l = length/2
	left_list = list_a[0:l]
	right_list = list_a[l-1:length]

	#Procedure call to find the max sum of divided array
	left_sum,left_i,left_j = find_max(left_list)
	right_sum,right_i,right_j = find_max(right_list)
	right_i = right_i+l-1
	right_j = right_j+l-1
	
	#variables to compute the max sum crossing the mid element
	max_val = left_sum
	mid_i = left_i
	mid_j = left_j
	sum = left_sum
	#calculating the max sum
	for i in range(left_j,length):
		sum = sum + list_a[i]
		if sum > max_val:
			max_val = sum
			mid_j = left_j + 1
		left_j = left_j + 1
		
	#Finding the maximum of three sum obtained
	max_subarray_sum = max(left_sum,right_sum,max_val)
	
	if max_subarray_sum == left_sum:
		print("The max sub array sum is", left_sum,"\n","Index i is", left_i,"\n","Index j is", left_j)
	elif max_subarray_sum == right_sum:
		print("The max sub array sum is", right_sum,"\n","Index i is", right_i,"\n","Index j is", right_j)
	else:
		print("The max sub array sum is", max_val,"\n","Index i is", mid_i,"\n","Index j is", mid_j)

if __name__ == "__main__":
    main()
