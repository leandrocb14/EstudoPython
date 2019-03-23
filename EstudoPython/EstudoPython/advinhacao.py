import random

print("********************************")
print("Bem vindo ao jogo de advinhação!")
print("********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentiva {} de {}".format(rodada, total_de_tentativas))

    chute = input("Digite seu número: ")
    chute = int(chute);
    print("Você digitou o número {}".format(chute))

    if(chute < 0 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    else:
        print("Você errou")
        if(chute > numero_secreto):
            print("Você errou! Seu número chutado é maior que o número secreto.")
        elif(chute < numero_secreto):
            print("Você errou! Seu número chutado é menor que o número secreto.")   

print("Fim de Jogo")