
#Error

n,q=map(int,input().split())
s=input()

for _ in range(q):
    query=input().split()
    
    if query[0]=="pop_back":
        s=s[:-1]
        
    elif query[0]=="front":
        print(s[0])
        
    elif query[0]=="back":
        print(s[-1])
        
    elif query[0]=="sort":
        l=int(query[1])-1
        r=int(query[2])
        sorted_part=''.join(sorted(s[l:r]))
        s=s[:l]+sorted_part+s[r:]
        
    elif query[0]=="reverse":
        l=int(query[1])-1
        r=int(query[2])
        reversed_part=s[l:r][::-1]
        s=s[:l]+reversed_part+s[r:]
        
    elif query[0]=="print":
        pos=int(query[1])-1
        print(s[pos])
        
    elif query[0]=="substr":
        l=int(query[1])-1
        r=int(query[2])
        print(s[l:r])
        
    elif query[0]=="push_back":
        x=query[1]
        s+=x


