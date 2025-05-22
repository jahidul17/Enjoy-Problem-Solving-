if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    
    unique=set(arr)
    sort=sorted(unique)
    print(sort[-2])
    


