def somadigitos(num):
    res=0
    div = 10000
    while div>=10:
        res += num//div
        num = num%div
        div = div/10

    return res+num


s=int(input())
a=int(input())
b=int(input())

cont= 0
for i in range (a,b+1):
    if somadigitos(i) == s: cont+=1

print(cont)