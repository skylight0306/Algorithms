
import numpy as np
import random
import time
#
#	Maximum-Subarray Problem
#	Find the maximum-subarray.
#
def Find_Maximum_Subarray( A ):
	n = len( A )
	low, high, sum = _Find_Maximum_Subarray( A, 0, n - 1 )
	
	#print( "Maximum-Subarray Problem:" )
	print( "Low =", low + 1, "High =", high + 1, "Sum =", sum )


def _Find_Maximum_Subarray( A, low, high ):
	if high == low:
		return low, high, A[low]
	else:
		mid = ( low + high ) // 2 
		
		left_low, left_high, left_sum    = _Find_Maximum_Subarray( A, low, mid )
		right_low, right_high, right_sum = _Find_Maximum_Subarray( A, mid + 1, high )		
		cross_low, cross_high, cross_sum = _Find_Max_Crossing_Subarray( A, low, mid, high )
		
		if ( left_sum > right_sum and left_sum >= cross_sum ):
			return left_low, left_high, left_sum
		elif ( right_sum >= left_sum and right_sum >= cross_sum ):
			return right_low, right_high, right_sum
		else:
			return cross_low, cross_high, cross_sum


def _Find_Max_Crossing_Subarray( A, low, mid, high ):
	left_sum = -3000000
	sum = 0
	for i in range( mid, low - 1, -1 ):
		sum += A[i]
		if sum > left_sum:
			left_sum = sum		
			max_left = i
		
	right_sum = -3000000
	sum = 0
	for j in range( mid + 1, high + 1 ):
		sum += A[j]
		if sum > right_sum:
			right_sum = sum	
			max_right = j
	
	cross_low  = max_left
	cross_high = max_right
	cross_sum  = left_sum + right_sum
	
	return cross_low, cross_high, cross_sum
name = 1
while name > 0:
    name = int(input('請輸入字串個數: '))
    if name <= 0 :
        break
    str = input ( '請輸入n個整數，每個整數以空格隔開。EX: 1 2 3 4 5: ')
    num = str.split(' ')
    array = list()
    for i in range(name):
        array.append(int(num[i]))
    
    Find_Maximum_Subarray( array )
    



