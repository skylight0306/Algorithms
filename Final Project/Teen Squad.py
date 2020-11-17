#!/usr/bin/env python
# coding: utf-8

# In[5]:



class inf:
    def __init__(self):  #存INPUT
        self.u = 0       #傳送人
        self.v = 0       #接收人
        self.w = 0       #權重
        
    def _init(self):      #存傳過人的資訊
        self.id = 0       #所有人的ID
        self.num = -1     #標示狀態 NUM > 0:指向樹根 ; NUM = -1:為樹根且只有自己 ; NUM < -1 :為樹根且有|NUM|個節點

def Drawgraph( list_MST, subset ):       #進行連結及找權重
    weight = 0;
    for i in range( len( list_MST ) ) :              #對每一筆INPUT找出傳送人及接送人在SUBSET裡的樹根
        root_u = findroot( subset, list_MST[i].u )
        root_v = findroot( subset, list_MST[i].v )
        
        if root_u.id != root_v.id :                     #如果這兩位的ROOT不是同一個人 代表兩位不再同一個集合 就傳
            root_u.num = ( root_u.num*(-1) + root_v.num*(-1) ) *(  -1 )   #將接收人作為樹根 NUM存取原本的結點數加上接收人的ROOT的節點數
            root_v.num = root_u.id                                        #接收人的NUM存取傳送人的ID 代表為傳送人的節點
            weight = weight + list_MST[i].w                  #計算到目前為止的所有權重
            
            # 如果兩位的ROOT相同代表在同一個集合 同宜個集合內已經傳過且是最小權重 不用再傳一次
    return weight

def findroot( subset, gid ) :               #找到這個ID的ROOT 並且回傳
    temp = inf()
    
    for i in range( len( subset ) ):            #找到id在subset的位置
        if subset[i].id == gid :
            temp = subset[i]

    while temp.num > 0:
        for i in range( len( subset ) ):            #找到id的root在subset的位置
            if subset[i].id == temp.num :
                temp = subset[i]    
    return temp    

def insertsubset( subset, id ):    #將INPUT裡面的ID存入SUBSET
    sus = inf()
    sus.id = id
    sus.num = -1                     #NUM初始為-1 代表各自為ROOT且只有自己
    subset.append( sus )

def insubset( subset, id ):              #確認ID是否已在SUBSET裡 
    for i in range( len(subset) ) :
        if subset[i].id == id :
            return True
    return False
        
        
if '__main__' == __name__:
    num, col = map( int, input().split() )
    j = 1
    
    while num != 0 and col != 0 :
        list_MST = []            #存取( u, v, w )
        subset = []              #存取( id, num )
        temp = []
        weight = 0
        for i in range( col ):
            ifo = inf()
            ifo.u, ifo.v, ifo.w = map( int, input().split() )
        
            if insubset( subset, ifo.u ) == False :
                insertsubset( subset, ifo.u )
        
            if insubset( subset, ifo.v ) == False:
                insertsubset( subset, ifo.v )
            list_MST.append( ifo )
        
        list_MST.sort( key = lambda i: i.w )       #對權重做排序 從小至大
        print("\n")
        weight = Drawgraph( list_MST, subset )
        
        print( "Case", j )
        print("Minimum Cost = ", weight )
        j = j + 1
        
        num, col = map( int, input().split() )


# In[ ]:




