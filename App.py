import os

restaurante =['Girafus e a Dani','Xp']

def exibir_nome_do_programa():  
 print("""Oscar Alho
  """)
def exibir_opcoes():
 print('1. Cadastrar restaurante')
 print('2. Listar restaurante')
 print('3. Ativar restaurante')
 print('4. Sair')

def finalizar_app():
   exibir_subtitulos('finalizar App')
   
def voltar_ao_menu_principal():
   input('\n Digite a tecla "Enter" para voltar ao menu pŕincipal')
   main()



opcao_escolhida = int(input('Escolha uma opção: '))



def exibir_subtitulos(texto):
    os.system("cls")
    print(texto)
    print()

def escolher_opcao():
   
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()

def main():
    os.System('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
   
