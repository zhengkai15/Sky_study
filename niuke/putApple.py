def putApple(m,n):
    if m == 0 or n == 1:
        return 1
    elif n > m :
        return putApple(m,m)
    else :
        return putApple(m,n-1) + putApple(m-n,n)

while True:
    try:
        m,n=map(int,input().split())
        print(putApple(m,n))
    except:
        break
