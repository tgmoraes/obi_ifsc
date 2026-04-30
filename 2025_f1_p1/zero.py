n = int(input())

pilha =[];
for i in range(n):
    x = int(input())
    if x==0: pilha.pop()
    else: pilha.append(x)

cont = 0
while(len(pilha)>0): cont+=pilha.pop()

print(cont)