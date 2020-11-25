def k_Subsets( A, k ):
	n = len( A )
	S = [0] * n

	for i in range( k ):
		S[i] = i + 1

	print( "{", end = " " )
	print( A[S[0] - 1], end = " " )
	for j in range( 1, k ):
		print( A[S[j] - 1], end = " " )
	print( "}" )	

	position = k - 1
	while ( 1 ):
		if ( S[k - 1] == n ):
			position -= 1
		else:
			position = k - 1
		S[position] += 1
		for i in range( position + 1, k ):
			S[i] = S[i - 1] + 1

		print( "{", A[S[0] - 1], end = " " )
		for j in range( 1, k ):
			print( A[S[j] - 1 ], end = " " )
		print( "}" )

		if ( S[0] >= n - k + 1 ):
			break