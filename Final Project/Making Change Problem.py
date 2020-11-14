import numpy as np
'''
Algorithm Project2
1. Making Change Problem
10627134 許寓翔
10627149 許峯僑
10627235 呂緯祥

'''


def Cal_Money(money,Use_coin):
    all_value=[] 
    value=[]
    many=[]
    bool = False
    mlist = [[0] * 2]*(money+1)
    #print(mlist)
    while money:
       
        tmp=Use_coin[money]
#        for i in range(len(mlist)):
#            if mlist[i][0] == tmp:
#                mlist[2].append(3)
#                bool = True
#        if not bool:
#            mlist.append(tmp)
#            mlist[len(mlist)-1][2] = 1
        all_value.append(tmp)

        money-=tmp
    #print (mlist)
    
    size = len(all_value)
    for i in range(0,size):
        for j in range(0,len(value)):
            if value[j] == all_value[i]:
                many[j] += 1
                bool = True
                
        if not bool:
            value.append(all_value[i])
            many.append(1)
        bool = False
    
    
    size = len(value)
    for i in range(0,size):
        print(value[i],"元", many[i], "枚")
    return all_value
 





def dp_money(coins,money,dp,Use_coin):
   
    size = money + 1
    for i in range(1,size):

        for j in range(len(coins)):
            #剩餘零錢 >= 幣值
            if coins[j]<=i: #input的幣值    

                if dp[i-coins[j]]+1<dp[i]:

                    dp[i]=dp[i-coins[j]]+1

                    new_coin=coins[j] #紀錄新的組合
        Use_coin[i]=new_coin
 
    
    if dp[money] > money:
            dp[money] = money+1
            return -1
    else:
            return dp[money]
    
    

if __name__=='__main__' :

    money = input('Input the Money : ')
    money = int(money) #轉成interger
    case = 1
    while  money > 0:
        coins=list(map(int,input().split())) #input
        #print(coins)
        type(coins)
        type(money)
        dp = [money+1]*(money+1) #使用的數量
        dp[0] = 0
        Use_coin=[0]*(money+1) #使用的幣值
 
        total=dp_money(coins,money,dp,Use_coin)
        #size = len(all_value)
        print("\n","Case ",case)

        all_value=Cal_Money(money,Use_coin)
        print(all_value)

        print("Total : ", total, "枚")

        money = input('Input the Money : ')
        money = int(money)
        case += 1
























