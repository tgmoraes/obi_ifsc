mensagem = input()

feliz = mensagem.count(":-)")
triste = mensagem.count(":-(")

resultado = feliz - triste;

if(resultado ==0): print("neutro")
elif (resultado>0): print("divertido")
else: print("chateado")

