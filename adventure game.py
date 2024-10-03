name = input("ola, digite seu nome:")
print("ola " + name + " bem vindo ao meu jogo!") 
devemos_jogar = input("voce quer jogar ele? ").lower()



if devemos_jogar == "sim":
    print("vamo jogar entao :)")

    direcao = input("voce quer ir pra <- esquerda ou direita -> ? ").lower()
    if direcao == "esquerda":
        print("ok, vamos para a <- esquerda")
        rio = input("voce encontrou um rio, esta disposto a nadar nele? ").lower()
        if rio == "sim":
            print("voce tomou um banho legal")
            
        elif rio == "nao":
            print("ok, voce passa reto")
        
        final = input("tem uma moça a sua frente, gostaria de comprimentar ela?").lower()
        if final == rio == "sim":
            print("voce ganhou um beijinho , ela disse que vc esta cheiroso, e pergunta se vc tomou banho, voces se casam no final dessa mesma semana ;)")
        elif rio == "nao" and final == "sim" :
            print("ela diz que vc ta fedendo e que provavelmente nunca tomou banho na vida, voce morre de coraçao partido :(")
        elif final == rio == "nao":
            print("ela te nota , e te acha grosseiro por voce nao comprimentar ela , e vc ainda ta fedendo, voce morre triste e fedendo :(")
        elif final == "nao" and rio == "sim":
            print("ela te nota, e te acha grosseiro por nao comprimentar ela, mas pelo menos vc ta cheiroso, ela te da um fora e voce morre de triste, mas morre cheiroso :|")
            

        

    else:
        print("ok, vamos para a direita -> entao.")
        perfume = input("tem um mano te vendendo um perfume, voce quer aceitar?").lower()
        if perfume == "nao":
            print("voce nega , e ele fica genuinamente chateado :(")
        elif perfume == "sim":
            print("voce aceita, ele diz pra voce que vai te retribuir de alguma forma algum dia")
        casamento = input("mais a frente, voce avista a mulher mais linda que vc ja viu , gostaria de falar com ela?").lower()
        if casamento == perfume == "sim":
            print("ela era filha do mano do perfume, ela te da um beijo por voce estar muito cheiroso, mas o pai dela era ciumento e acabou eliminando voce:( ")
        elif casamento == "sim" and perfume == "nao":
            print("ela era filha do mano do perfume , alem de vc estar fedendo ,o pai dela rejeita voce de forma que vc se mata de coraçao partido :(")
        elif casamento == perfume == "nao":
            print("ela ve que vc notou ela, mas o pai dela (que era o mano do perfume), nota voce tambem , eles te acham estranho por ficar encarando ela, os dois juntos assasinam voce :(")
        elif casamento == "nao" and perfume == "sim":
            print("ela era filha do mano do perfume , ambos notaram voce encarando eles, mas como vc decidiu nao falar com ela , o pai dele vem ate voce, sente seu cheiro , reconhece voce, e voces acabam se beijando e casando , vivendo assim felizes para sempre :)")

else:
    print("entao NAO vamos jogar... :(")

   
