

import numpy as np
import random
import time

class BSTNode:

	def __init__( self ):
		self.key   = None
		self.left  = None
		self.right = None


class BinarySearchTree:

	def __init__( self ):
		self.root = None
		self.n = 0

	def Insert( self, key ):
		ptr = BSTNode()
		ptr.key = key
		ptr.left = None
		ptr.right = None

		if ( self.root == None ):
			self.root = ptr
		else:
			parent = None
			current = self.root
			while ( current != None ):
				parent = current
				if ( key < current.key ):
					current = current.left
				else:
					current = current.right
			if ( key < parent.key ):
				parent.left = ptr
			else:
				parent.right = ptr
		self.n += 1

	def Delete( self, key ):
		parent = None
		current = self.root	
		while ( current != None ):			
			if ( key == current.key ):
				break
			parent = current
			if ( key < current.key ):
				current = current.left
			else:
				current = current.right

		if ( current == None ):
			print( "Deleted node is not found." )
		else:
			if ( current.left == None and current.right == None ):  # Leaf node
				if ( current == self.root ):
					self.root = None
				else:
					if ( current.key < parent.key ):
						parent.left = None
					else:
						parent.right = None
			elif ( current.left != None and current.right == None ):  # Left subtree is not empty
				if ( current == self.root ):
					self.root = current.left
				else:
					if ( current.key < parent.key ):
						parent.left = current.left
					else:
						parent.right = current.left
			elif ( current.left == None and current.right != None ):  # Right subtree is not empty
				if ( current == self.root ):
					self.root = current.right
				else:
					if ( current.key < parent.key ):
						parent.left = current.right
					else:
						parent.right = current.right
			else:                                        # Both left & right subtrees are not empty
				prev = current
				ptr = current.right
				while ( ptr.left != None ):
					prev = ptr
					ptr = ptr.left

				if ( ptr.key < prev.key ):
					prev.left = ptr.right
				else:
					prev.right = ptr.right

				current.key = ptr.key

			self.n -= 1				

	def Preorder( self ):
		if ( self.root == None ):
			print( "No keys in the binary search tree." )
		else:
			print( "Binary Search Tree (Preoder):" )
			self._Preorder( self.root )
			print()

	def _Preorder( self, ptr ):
		if ( ptr != None ):
			print( ptr.key, end = " " )
			self._Preorder( ptr.left )	
			self._Preorder( ptr.right )

	def Inorder( self ):
		if ( self.root == None ):
			print( "No keys in the binary search tree." )
		else:
			print( "Binary Search Tree (Inorder):" )
			self._Inorder( self.root )
			print()

	def _Inorder( self, ptr ):
		if ( ptr != None ):
			self._Inorder( ptr.left )
			print( ptr.key, end = " " )
			self._Inorder( ptr.right )
	
	def Postorder( self ):
		if ( self.root == None ):
			print( "No keys in the binary search tree." )
		else:
			print( "Binary Search Tree (Postorder):" )
			self._Postorder( self.root )
			print()

	def _Postorder( self, ptr ):
		if ( ptr != None ):
			self._Postorder( ptr.left )
			self._Postorder( ptr.right )
			print( ptr.key, end = " " )
str = 1
while str != 0:
    str = input ( '請輸入n個整數，每個整數以空格隔開。EX: 1 2 3 4 5: ')
    if str == '0': break
    num = str.split(' ')
    array = list()
    for i in range(len(num)):
        array.append(num[i])         
        #print(array)
    
    Tree = BinarySearchTree()
    BinarySearchTree.__init__( Tree )
    for i in range(len(array)):
        if array[i].isdigit():
            BinarySearchTree.Insert( Tree, int(array[i]) )
        else: BinarySearchTree.Insert( Tree, array[i] )
    BinarySearchTree.Postorder( Tree )


# In[ ]:





# In[ ]:




