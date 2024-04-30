import os

restaurantes = [{'nome':'restaurante XP','categoria':'Alimento','ativo':False},
                {'nome':'Santa','categoria':'carne','ativo':True},
                {'nome':'CWB','categoria':'Sushi','ativo':False}] 
def exibir_nome_do_programa():
 ''' Está função é responsável por exibir o nome do programa
 '''
 
 print("""Oscar Alho
 """)
def exibir_opcoes():
 print('1. Cadastrar restaurante')
 print('2. Listar restaurante')
 print('3. Ativar restaurante')
 print('4. Sair')
 
def finaliza_app():
   '''Essa função é responsável por finalizar o Aplicativo
   output:
   - Aplicativo Finalizado
   '''

   exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
   '''Essa função é responsável por fazer voltar ao menu principal
     '''
   
   input('\n Digite a tecla "Enter" para voltar ao menu principal')
   main()
   
def opcao_invalida():
   '''Essa função é responsável por invalidar as opções
   '''

   print('Opção invalida!\n')
   voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir na tela o texto
      '''
    
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
   '''Essa função é responsável por cadastrar um novo restaurante
   Inputs:
   - Nome do restaurante
   - Categoria

   Output:
   - Adiciona um novo restaurante à lista de restaurantes
   '''

   exibir_subtitulo('Cadastro de novos restaurantes: ')
   nome_do_restaurante = input('Digite o nome do novo restaurante:')
   categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
   dado_do_restaurante ={'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
   restaurantes.append(dado_do_restaurante)
   print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
   voltar_ao_menu_principal()

def listar_restaurante():
   '''Essa função é responsável por exibir uma lista dos restaurantes na tela
   '''

   exibir_subtitulo('Listando os restaurantes')

   print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
   for restaurante in restaurantes:
      nome_restaurante = restaurante['nome']
      categoria = restaurante['categoria']
      ativo = 'ativado' if restaurante['ativo'] else 'desativado'
      print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

   voltar_ao_menu_principal()  

def alternar_estado_restaurante():
   '''Essa função é responsável po alternar o estado do restaurante 
   inputs:
   - nome do restaurante
   - categoria 

   output:
   - Estado do restaurante foi alterado
   '''

   exibir_subtitulo('Alternando estado do restaurante')
   nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado:')
   restaurante_encontrado = False

   for restaurante in restaurantes:
      if nome_restaurante == restaurante['nome']:
         restaurante_encontrado = True
         restaurante['ativo'] = not restaurante['ativo']
         mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
         print(mensagem)

   if not restaurante_encontrado:
      print('O restaurante não foi encontrado')
   voltar_ao_menu_principal()  
    
def escolher_opcao():
 '''Essa função é responsável por exibir as opções'''

 try:
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
        listar_restaurante()
    elif opcao_escolhida == 3:
         alternar_estado_restaurante()
    elif opcao_escolhida == 4:
       finaliza_app()    
    else:
       opcao_invalida()

 except:
    opcao_invalida()        

def main():
   '''Essa função é a principal responsavel por apresentar as opções do aplicativo
     '''
   
   os.system('clear')
   exibir_nome_do_programa()
   exibir_opcoes()
   escolher_opcao()

if __name__ == '__main__':
    main()
