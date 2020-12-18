	def DFS( self, source ):
		for u in range( 1, self.n_vertices + 1 ):
			self.color[u] = WHITE	
			self.d[u] = INFINITY
			self.pi[u] = 0
			self.f[u] = 0

		print( "DFS Sequence:" )
		self.time = 0
		self._DFS( source )
		print() 

	def _DFS( self, u ):
		print( u, end = " " )
		self.color[u] = GRAY
		self.time += 1
		self.d[u] = self.time
		for v in range( 1, self.n_vertices + 1 ):
			if ( self.A[u][v] != 0 ):
				if ( self.color[v] == WHITE ):
					self.pi[v] = u
					self._DFS( v )
		self.color[u] = BLACK
		self.time += 1
		self.f[u] = self.time

