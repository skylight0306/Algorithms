#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Suduko( object ):

    def __init__( self, s ):                              #初始化 將題目問題放入Sudoke
        self.s = s 

    def srearch_fill( self ):                             #依序找到空格然後找最適當值填入
        i,j = self.space_point()                          #找出空格
        if i >= 8 and j >= 8 and self.s[8][8]:            #若點為(9,9)且該點的值不是0 代表全部填完
            return True
        for value in range( 1,10 ):                       #值從1~9帶入
            if self.check_all( i, j, value ):             #確認該值是否可以填入該格
                self.s[i][j] = value 
                if not self.srearch_fill():               #若找不到值帶入的話 將該格reset 
                    self.s[i][j] = 0 
                else:
                    return True
        return False                                      #若reset的話 回傳false給上一層遞迴 

    def space_point( self ):                              #依序給格子
        for i in range( 9 ):
            for j in range( 9 ):
                if not self.s[i][j]:                      #只回傳值為0的格子
                    return i,j                
        return i,j                                        
    
    def check_all( self, i, j, value ):                   #確認該值是否同值滿足三樣條件
        if self.check_row( i, j, value ) and self.check_col( i, j, value ) and self.check_small( i, j, value ):
            return True 
        else:
            return False

    def check_row( self, i, j, value ):                   #確認同行是否有相同值
        return value not in self.s[i]

    def check_col( self, i, j, value ):                   #確認同列是否有相同值
        col = [self.s[v][j] for v in range(9)] 
        return value not in col

    def check_small( self, i, j, value ):                 #確認小9宮格內是否有相同值
        small = [self.s[r][c] for r in range( int( i/3 )*3,int( i/3+1 )*3 ) for c in range( int( j/3 )*3,int( j/3+1 )*3 )]
        return value not in small


if '__main__' == __name__:
    
    sudo = []                                                #用來存放題目
    for i in range( 9 ):
        d = input()
        sudo.append( [int( d ) for d in d] )

    S = Suduko( sudo )
    S.srearch_fill()
    
    print('\n')
    for i in range( 9 ):
        for j in range( 9 ):
            print ( S.s[i][j], end = '' )
        print( end = '\n')

