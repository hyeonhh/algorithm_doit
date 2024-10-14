n = int(input())

#공백 출력

for i in range(n-1,0,-1):
    blank = " " * (i)
    print(blank,end="")
    star = "*"  * ( (2*n-1)-(2*i))
    print(star,end="")
    print(blank)

for i in range(2,n):
    blank = " " * (i)
    print(blank,end="")
    star = "*"  * ((2*n-1)-(2*i))
    print(star,end="")
    print(blank)


# for i in range(1,n):
#     print(' '*(n-i) + "*"*(2-i-1))
# for i in range(n,0,-1):
#     print(' '*(n-i)+ '*'*(2*i-1))