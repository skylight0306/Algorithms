#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


i = 1
j = 1 
l = 1 
zero = 1
num_0f_edge = 0
num_0f_edge = int ( input("輸入一個大於3小於100的正整數:") )

while num_0f_edge != 0 :
    while num_0f_edge == 0 or num_0f_edge < 3 or num_0f_edge > 100 :
        if num_0f_edge == 0:
            break;
        else:
            num_0f_edge = int ( input("你輸錯了喔! 請輸入一個大於3小於100的正整數:") )
    if num_0f_edge != 0:    
        count = 0
        for i in range( 1, num_0f_edge+1 ) :
            for j in range( i+1, num_0f_edge+1 ) :
                for k in range( j+1, num_0f_edge+1 ) :
                    if i + j > k :                         #確認最小兩邊和大於第三邊 若是就計數
                        count = count + 1;
        print( count, end = '\n' );
        if zero == 1:
            num_0f_edge = int ( input("輸入一個大於3小於100的正整數:") )
    
print( "END!" )

