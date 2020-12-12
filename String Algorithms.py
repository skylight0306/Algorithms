LOW     = 1
MIDDLE  = 2
HIGH    = 3
HIGHEST = 4

def priority_op( op ):
	if ( op == '^' ):
		return HIGHEST
	elif ( op == '*' or op == '/' ):
		return HIGH
	elif ( op == '+' or op == '-' ):
		return MIDDLE	
	else:
		return LOW

def infix_to_postfix( in_str ):
	k = len( in_str )
	S = Stack()
	out_str = ""

	for i in range( k ):
		ch = in_str[i]

		if ( ch in '+-*/^' ):
			done = False
			while ( ( S.isEmpty() == False ) and ( done == False ) ):
				top = S.Pop()
				if ( ( top != '(' ) and ( priority_op( top ) >= priority_op( ch ) ) ):
					out_str += top
				else:
					S.Push( top )
					done = True
			S.Push( ch )

		elif ( ch == '(' ):  
			S.Push( ch )

		elif ( ch == ')' ):  
			top = S.Pop()
			while ( top != '(' ):
				out_str += top
				top = S.Pop()

		else:  # Operands
			out_str += ch

	while( S.isEmpty() == False ):
		out_str = out_str + S.Pop()

	return ( out_str )
