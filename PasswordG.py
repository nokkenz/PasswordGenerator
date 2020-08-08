import string, random

P = random.choice(string.printable)

senha = []

while len(senha) < 12:
    random.shuffle(P)
    senha.append(P)
    if P in senha:
        P = random.choice(string.printable)
        senha.append(P)
        random.shuffle(senha)
    print(*senha,sep='') #imprimir sem virgulas e sem espaço