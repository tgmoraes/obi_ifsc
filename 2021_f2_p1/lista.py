N = int(input())

lista = list(map(int, input().split(" ")))

cont = 0
i=0
while (i < (len(lista)//2)):
    if(lista[i]> lista[-i-1]): pos = -i-1
    elif (lista[i] < lista[-i-1]): pos = i
    else: 
        i+=1
        continue
   
    aux = int(lista.pop(pos))
    lista[pos] = str(int(lista[pos])+aux)
    cont+=1

print(cont)