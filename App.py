import os

print("""Oscar Alho
      """)

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair')

opcao_escolhida = int(input('Escolha uma opcao: '))

def finalizar_app():
    os.system("cls")
    print('Encerrando o programa\n')

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('listar restaurante')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    finalizar_app()