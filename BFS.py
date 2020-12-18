	def BFS( self, source ):
		for u in range( 1, self.n_vertices + 1 ):
			if ( u != source ):
				self.color[u] = WHITE
				self.d[u] = INFINITY
		
		self.color[source] = GRAY
		self.d[source] = 0
		self.pi[source] = 0

		print( "BFS Sequence:" )
		Q = Queue()
		Q.Enqueue( source )
