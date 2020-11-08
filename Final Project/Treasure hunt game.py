#import numpy as np


Map = [[]]
already = [[]]
def ReadMap(W,H):
    Map =[[0]*W for i in range(H)]  
    for i in range(H):
        str = input ( '請輸入尋寶遊戲的題目。EX: #######: ')
        Map[i] = str
    return Map
def FindWhereIsHunter( W, H, Map):
    for i in range(W):
        for j in range(H):
            if Map[i][j] == 'P' :return i,j
    return 0,0
def FindTrap(partX, partY, Map, already):
    if Map[partX][partY + 1] == 'T': return True
    elif Map[partX][partY - 1] == 'T': return True 
    elif Map[partX + 1][partY] == 'T': return True 
    elif Map[partX - 1][partY] == 'T': return True
    return False
def FindGold(partX, partY, Map, already, Gold):
    gold = 0
    currentgold = 0
    Pass = already
    #print(Map[partX][partY],partX,partY, already[partX][partY])
    if already[partX][partY] == True : return currentgold
    elif Map[partX][partY] == '.' or Map[partX][partY] == 'G' or Map[partX][partY] == 'P':
        already[partX][partY] = True
        if Map[partX][partY] == 'G' : 
            currentgold = currentgold + 1
            Map[partX][partY] == '.'
        if FindTrap(partX, partY, Map, already) == True : 
            already[partX][partY] = True
            return currentgold
        gold = gold + FindGold(partX, partY + 1, Map, already, Gold) + FindGold(partX, partY - 1, Map, already, Gold) + FindGold(partX + 1, partY, Map, already, Gold) + FindGold(partX - 1, partY, Map, already, Gold)
        return currentgold + gold
    elif Map[partX][partY] == 'T': 
        already[partX][partY] = True
        return currentgold
    elif Map[partX][partY] == '#' :
        already[partX][partY] = True
        return currentgold
    
    


# Create a graph given in the above diagram 
str = 1
#W = 0, H = 0
while str != '0 0':
    str = input ( '請輸入2個整數，第一個為列數，第二個為行數，備註:直行橫列。EX: 7 4: ')
    if str == '0 0': break
    num = str.split(' ')#    
    W = int(num[0])
    H = int(num[1])
    Max = W*H
    Map = ReadMap(W,H)# 雖然獵人不知道MAP 但我們還是要知道地圖 不然怎麼跑題目
    already = [[False]*(W + 1) for i in range(H + 1)]
    #print (already)
    Gold = 0
    PartX, PartY = FindWhereIsHunter( W, H, Map)
    Gold = FindGold(PartX, PartY, Map, already, Gold)
    print("Getting Gold = " , end = '')
    print(Gold)

                    
        