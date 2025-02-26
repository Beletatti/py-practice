print('''
   _--_     _--_    _--_     _--_     _--_     _--_     _--_     _--_
  ( () )___( () )  ( () )___( () )   ( () )___( () )   ( () )___( () )
   \           /    \           /     \           /     \           /
    (  ' _ `  )      (  ' _ `  )       (  ' _ `  )       (  ' _ `  )
     \  ___  /        \  ___  /         \  ___  /         \  ___  /
   .__( `-' )          ( `-' )           ( `-' )        .__( `-' )  ___
  / !  `---' \      _--'`---_          .--`---'\       /   /`---'`-'   \
 /  \         !    /         \___     /        _>\    /   /          ._/   __
!   /\        !   /   /       !  \   /  /-___-'   ) /'   /.-----\___/     /  )
!   !_\______/\. (   <        !__/ /'  (        _/  \___//          `----'   !
 \    \       ! \ \   \      /\    \___/`------' )       \            ______/
  \___/   )  /__/  \--/   \ /  \  ._    \      `<         `--_____----'
    \    /   !       `.    )-   \/  ) ___>-_     \   /-\    \    /
    /   !   /         !   !  `.    / /      `-_   `-/  /    !   !
   !   /__ /___       /  /__   \__/ (  \---__/ `-_    /     /  /__
   (______)____)     (______)        \__)         `-_/     (______)
''')
print("Bem-vindo a ilha dos ursos!\nA partir de agora, tome as decisões certas para não ser morto por um urso gigante D:")

esquerda_direita = input('Esquerda ou direita? Digite "direita" ou "esquerda" ').lower()
if esquerda_direita == "direita":
    nadar_esperar = input('Nadar no rio ou esperar? Digite "nadar" ou "esperar" ').lower()
    if nadar_esperar == "esperar":
        porta = input('Escolha uma porta: Digite "Vermelha", "Azul" ou "Amarela" ').lower()
        if porta == "vermelha":
            print("Emboscado por um urso-preguiça, você morreu!")
        elif porta == "azul":
            print("Você caiu em um calabouço e ficou preso até morrer de fome. Game over!")
        elif porta == "amarela":
            print("Bom trabalho! Você achou um camiho para escapar da floresta.")
        else:
            print("Você escolheu um caminho que não existe e caiu no vazio. Até nunca mais!")
    else:
        print("Um urso marrom te encontrou no rio e te matou. Game over!")
else:
    print("Você foi brutalmente morto por um urso-negro. Game over!")


