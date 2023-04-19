def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "Estojo".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto(True)
    while(not enforcou and not acertou):

        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Você só pode errar mais {6-erros} vez(es)")

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        print("Você ganhou!")
    else:
        print("VocÊ perdeu!")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
