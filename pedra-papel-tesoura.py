import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lista = [pedra, papel, tesoura]

escolha_jogador = int(input("Qual a sua escolha? Digite 0 para pedra, 1 para tesoura e 2 para papel."))
print(lista[escolha_jogador])

escolha_bot = random.randint(0, 2)
print("Escolha do bot: ")
print(lista[escolha_bot])

if escolha_jogador >= 3 or escolha_jogador < 0:
    print("Você digitou um número invalido, você perdeu!")
elif escolha_jogador == 0 and escolha_bot == 2:
    print("Vitória.")
elif escolha_bot == 0 and escolha_jogador == 2:
    print("Derrota.")
elif escolha_bot > escolha_jogador:
    print("Derrota.")
elif escolha_jogador > escolha_bot:
    print("Vitória!")
elif escolha_bot == escolha_jogador:
    print("Empate!")











