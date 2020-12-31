class FlowNetwork:

	def __init__ ( self, n_vertices ):
		
		# Initialization (By default: source vertex = 1, sink vertex = n)
		self.n_vertices = n_vertices
		self.n_edges = 0
		self.source = 1			 
		self.sink = n_vertices	 

		# Capacity & Flow
		self.cap  = [ [ 0 for i in range( n_vertices + 1 )] for j in range( n_vertices + 1 ) ]
		self.flow = [ [ 0 for i in range( n_vertices + 1 )] for j in range( n_vertices + 1 ) ]
	
		# For the BFS
		self.color = [ 0 for i in range( n_vertices + 1 ) ]
		self.pi     = [ 0 for i in range( n_vertices + 1 ) ]

	def SetEdge( self, start_vertex, end_vertex, capacity ):
		if ( start_vertex >= 1 and start_vertex <= self.n_vertices and 
			 end_vertex >= 1 and end_vertex <= self.n_vertices ):
				self.cap[start_vertex][end_vertex] = capacity
				self.n_edges += 1

	def Display( self ):
		print( "Flow Network" )
		print( "Number of Vertices =", self.n_vertices )
		print( "Number of Edges =", self.n_edges )
		for i in range( 1, self.n_vertices + 1 ):
			for j in range( 1, self.n_vertices + 1 ):
				print( self.cap[i][j], end = " " )
			print()

	def BFS( self ):		
		for u in range( 1, self.n_vertices + 1 ):
			if ( u != self.source ):
				self.color[u] = WHITE
				self.pi[self.source] = 0

		self.color[self.source] = GRAY
		self.pi[self.source] = 0

		Q = Queue()
		Q.Enqueue( self.source )

		while ( Q.isEmpty() == False ):
			u = Q.Dequeue()
			for v in range( 1, self.n_vertices + 1 ):
				if ( self.color[v] == WHITE and self.cap[u][v] - self.flow[u][v] > 0 ):
					self.color[v] = GRAY
					self.pi[v] = u
					Q.Enqueue( v )
			self.color[u] = BLACK

		if ( self.color[self.sink] == BLACK ):  # If the sink is reachable, then the augmenting path exists!
			return True
		else:
			return False

	def MaxFlow( self ):
		max_flow = 0

		while ( self.BFS() ):  # Determine if the augmenting path exists

			increment = 10000000
			u = self.sink
			while( self.pi[u] >= self.source ):
				if ( increment > self.cap[self.pi[u]][u] - self.flow[self.pi[u]][u] ):
					increment = self.cap[self.pi[u]][u] - self.flow[self.pi[u]][u]
				u = self.pi[u]

			u = self.sink
			while ( self.pi[u] >= self.source ):  # Update the flow
				self.flow[self.pi[u]][u] += increment
				self.flow[u][self.pi[u]] -= increment
				u = self.pi[u]

			max_flow += increment
			if ( increment == 0 ): break	

		return max_flow

