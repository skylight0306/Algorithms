def Permutations( A ):
	n = len( A )
	_Permutations( A, 0, n )


def _Permutations( A, i, n ):
	if i < n:
		for j in range( i, n ):
			temp = A[j]
			for k in range( j, i, -1 ):
				A[k] = A[k - 1]
			A[i] = temp
			
			_Permutations( A, i + 1, n )
			
			for k in range( i, j ):
				A[k] = A[k + 1]
			A[j] = temp
	else:
		for j in range( 0, n ):
			print( A[j], end = " " )
		print()	
	