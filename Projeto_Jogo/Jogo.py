
import random

def jogo():
    usuario = input("Qual a sua escolha? Digite 'p' se desejar a pedra, 'a' se desejar a papel e 't' se desejar a tesoura\n")
    maq = random.choice(['p', 'a', 't'])

    if usuario == maq:
        return 'Deu empate!'

   
    if vencer(usuario, maq):
        return 'Você venceu!'

    return 'Você perdeu!'

def vencer(jogador, oponente):
   
    if (jogador == 'p' and oponente == 't') or (jogador == 't' and oponente == 'a') \
        or (jogador == 'a' and oponente == 'p'):
        return True

print(jogo())