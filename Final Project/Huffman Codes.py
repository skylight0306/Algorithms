import numpy as np


def reverse_r(s):
    if len(s) <= 1:
            return s
    else:
            return reverse_r(s[1:]) + s[0]


if __name__=='__main__' :
    
    
    num = input('Input the Quantity : ')
    num = int(num)
    count = 1
    while num != 0:
        huf = []
        code = [] #原始的code
        value = [] #原始的value
        sort_code =[] 
        for i in range(0,num):
            huf.append("")
            tmp1, tmp2 = input().split()
            code.append(tmp1)
            value.append(int(tmp2))

        decode = input()
        
        
    
            
        tmp = sorted(value)
        for i in range(0,len(tmp)):
            for j in range(0,num):
                if tmp[i] == value[j]:
                    sort_code.append(code[j])
        while len(tmp) > 1:


            for i in range(0,num):
                if code[i] in sort_code[0]:
                    huf[i] += "0"
                elif code[i] in sort_code[1]:
                    huf[i] += "1"
                    
            tmp[1] += tmp[0]
            sort_code[1] += sort_code[0]
            code.append(sort_code[1])
            value.append(tmp[1])
            del sort_code[0]
            del tmp[0]
            tmp = sorted(tmp)
            sort_code.clear()
            for i in range(0,len(tmp)):
                for j in range(0,len(value)):
                    if tmp[i] == value[j]:
                        sort_code.append(code[j])
            #print(sort_code)
            #print(decode)
            
            

        for i in range(0,len(huf)):
            huf[i] = reverse_r(huf[i])
            
        
        index = 0
        code_str = ""
        # i = 0
        while index < len(decode):
            for i in range(0,len(huf)):
                if decode[index:index + len(huf[i])] == huf[i]:
                    code_str += code[i]
                    index += len(huf[i])
                    break
            
        
        
        
            
        print("Huffman Codes #",count)
        for i in range(0,num):
            print(code[i]," ", huf[i])         
        
        print("Decode = ",code_str )
            
            
            
        num = input('Input the Quantity : ')
        num = int(num) 




        count+=1
        
    
    
    

    
            